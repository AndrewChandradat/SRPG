from tkinter import *
from config import *

def calc_inter_margin( total_length, end_margins, num_spaces, space_width ):
	return ( total_length - ( 2 * end_margins ) - ( num_spaces * space_width ) ) / ( num_spaces - 1 )

INTER_HORIZ_MARGIN = calc_inter_margin( BATTLE_AREA_WIDTH, SIDE_MARGIN, NUM_COLS, REC_WIDTH )
INTER_VERT_MARGIN = calc_inter_margin( BATTLE_AREA_HEIGHT, TOP_MARGIN, NUM_ROWS, REC_HEIGHT )


def configure_character_space( fight, frame, x, y ):
	#highlighting based on target and turn status
	if( fight.turn == (x, y) ):
		frame.configure(  highlightbackground="red", highlightcolor="red" )
		fight.active_character_frame = frame
	if( fight.active_target_pos == ( x, y ) ):
		frame.configure( highlightbackground="blue", highlightcolor="blue", relief="groove", bd=5 )
	#configurations
	frame.configure( cursor="hand2" )
	frame.columnconfigure(0, weight=1)
	frame.rowconfigure( 0, weight=1 )
	frame.rowconfigure( 1, weight=2 )
	#displaying character info
	char = fight.get_character( (x, y) )
	name = Label( frame, text=char.name(), bg="white" )
	hp = Label( frame, text=char.hp_meter, bg="white" )
	name.grid( sticky=S, columnspan=2 )
	hp.grid( )
	#target binding
	frame.bind("<Button-1>", lambda e, f=fight, pos=(x,y): target_char( e, f, pos ))
	name.bind("<Button-1>", lambda e, f=fight, pos=(x,y): target_char( e, f, pos ))
	hp.bind("<Button-1>", lambda e, f=fight, pos=(x,y): target_char( e, f, pos ))

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

def populate_action_list( action_bar, fight ):
	action_count = 0
	for action in fight.active_character().movelist():
		action_frame = Frame( action_bar, height=ACTION_HEIGHT, width=ACTION_WIDTH, cursor="hand2")
		action_frame.grid( row=0, column=action_count, padx=ACTION_SIDE_MARGIN, pady=ACTION_TOP_MARGIN )
		action_frame.grid_propagate( 0 )
		action_frame.columnconfigure(0, weight=1)
		if( action_count == fight.active_action_index ):
			fight.set_action( action_frame, action_count )
			action_frame.config( highlightbackground="red", highlightcolor="red", highlightthickness=1 )

		action_name = Label( action_frame, text=action.name, bg="white" )
		action_name.grid()
		action_frame.bind( "<Button-1>", lambda e, f=fight, index=action_count: select_action( e, f, index ))
		action_count = action_count + 1


def select_action(event, fight, index):
	frame = get_containing_frame( event )
	if( fight.active_action_frame ):
		fight.active_action_frame.config( highlightbackground="black", highlightcolor="black" )
	fight.set_action( frame, index )
	frame.config( highlightbackground="red", highlightcolor="red" )

def execute_action( event, fight ):
	if( fight.active_target_frame and fight.active_action_frame ):
		fight.execute()
		fight.active_target_frame.winfo_children()[1].config( text=fight.target().hp_meter )
		fight.active_target_frame.config( highlightbackground="black", highlightcolor="black" )
		fight.active_action_frame.config( highlightbackground="black", highlightcolor="black" )
		go_next_turn( event.widget.winfo_toplevel(), fight )

def go_next_turn( root, fight ):
	fight.active_character_frame.config( highlightbackground="black", highlightcolor="black" )
	action_bar = fight.active_action_frame.master
	fight.next_turn()
	new_frame_number = fight.turn[0] + ( fight.battlefield.width * fight.turn[1])
	fight.active_character_frame = root.winfo_children()[ new_frame_number ]
	fight.active_character_frame.config( highlightbackground="red", highlightcolor="red" )

	for w in action_bar.winfo_children():
		w.destroy()
		
	populate_action_list( action_bar, fight )
