from tkinter import *
from config import *
import time

def populate_action_list( fight ):
	action_count = 0
	for action in fight.active_character().movelist():
		action_frame = Frame( fight.action_bar_frame, height=ACTION_HEIGHT, width=ACTION_WIDTH, cursor="hand2")
		action_frame.grid( row=0, column=action_count, padx=ACTION_SIDE_MARGIN, pady=ACTION_TOP_MARGIN )
		action_frame.grid_propagate( 0 )
		action_frame.columnconfigure(0, weight=1)

		if( action_count == fight.active_action_index ):
			fight.set_action( action_frame, action_count )
			action_frame.config( highlightbackground="red", highlightcolor="red" )

		action_name = Label( action_frame, text=action.name, bg="white" )
		action_name.grid()
		action_frame.bind( "<Button-1>", lambda e, f=fight, index=action_count: select_action( e, f, index ))
		action_count = action_count + 1


def get_containing_frame( event ):
	if( event.widget.winfo_class() == "Frame" ):
		return event.widget
	else:
		return event.widget.master

def target_char( event, fight, pos):
	frame = get_containing_frame( event )
	if( fight.active_target_frame ):
		fight.active_target_frame.config( highlightbackground="black", highlightcolor="black" )
	fight.set_target( frame, pos )
	frame.config( highlightbackground="blue", highlightcolor="blue" )

def select_action(event, fight, index):
	frame = get_containing_frame( event )
	if( fight.active_action_frame ):
		fight.active_action_frame.config( highlightbackground="black", highlightcolor="black" )
	fight.set_action( frame, index )
	frame.config( highlightbackground="red", highlightcolor="red" )

def execute_action( event, fight ):
	if( fight.active_target_frame and fight.active_action_frame ):
		dmg = fight.execute()
		fight.active_target_frame.winfo_children()[1].config( text=fight.target().hp_meter )

		fight.active_target_frame.config( highlightbackground="black", highlightcolor="black" )
		if( fight.playable_turn() ):	#this frame is never set by ai
			fight.active_action_frame.config( highlightbackground="black", highlightcolor="black" )

		#need to move this to right pane
		print( "%s uses %s on %s! (%+d)" % (fight.active_character().name(), fight.selected_action().name, fight.target().name(), 0 - dmg  )  )

		go_next_turn( event, fight )

def go_next_turn( event, fight ):

	root = event.widget.winfo_toplevel()
	#reset active_character border color
	fight.active_character_frame.config( highlightbackground="black", highlightcolor="black" )
	fight.next_turn()

	if( fight.playable_turn() ):
		player_turn( event, fight )
	else:
		ai_turn( event, fight )

def player_turn( event, fight ):
	root = event.widget.winfo_toplevel()
	#get the frame of the new active character and make its border red
	active_character_frame_number = fight.turn[0] + ( fight.battlefield.width * fight.turn[1])
	fight.active_character_frame = root.winfo_children()[ active_character_frame_number ]
	fight.active_character_frame.config( highlightbackground="red", highlightcolor="red" )
	#get the frame of the default target and make its frame blue
	target_frame_number = fight.active_target_pos[0] + ( fight.battlefield.width * fight.active_target_pos[1] )
	fight.active_target_frame = root.winfo_children()[ target_frame_number ]
	fight.active_target_frame.config( highlightbackground="blue", highlightcolor="blue" )
	#clear action list and fill it with actions of new active character
	for w in fight.action_bar_frame.winfo_children():
		w.destroy()
	populate_action_list( fight )


def ai_turn( event, fight ):
	root = event.widget.winfo_toplevel()
	#get the frame of the new active character and make its border red
	active_character_frame_number = fight.turn[0] + ( fight.battlefield.width * fight.turn[1])
	fight.active_character_frame = root.winfo_children()[ active_character_frame_number ]
	fight.active_character_frame.config( highlightbackground="red", highlightcolor="red" )
	#have the ai pick its attack and target
	fight.active_character().automate( fight )
	#get the frame of the default target and make its frame blue
	target_frame_number = fight.active_target_pos[0] + ( fight.battlefield.width * fight.active_target_pos[1] )
	fight.active_target_frame = root.winfo_children()[ target_frame_number ]
	fight.active_target_frame.config( highlightbackground="blue", highlightcolor="blue" )
	#clear action list
	for w in fight.action_bar_frame.winfo_children():
		w.destroy()
	#display combat text
	combat_text = "%s uses %s on %s!" % (fight.active_character().name(), fight.selected_action().name, fight.target().name() )
	combat_message_f = Frame( fight.action_bar_frame, height=ACTION_AREA_HEIGHT - 5, width=BATTLE_AREA_WIDTH+(2*SIDE_MARGIN) - 5,
								highlightbackground="white", highlightcolor="white")
	combat_message_f.grid_propagate( 0 )
	combat_message_f.grid()
	combat_message = Label( combat_message_f, text=combat_text, font=("", 20), bg="white" )
	combat_message.grid()
	#refresh window
	#fight.action_bar_frame.update_idletasks()
	#pause
	#time.sleep( 1 )

	#execute_action( event, fight )
