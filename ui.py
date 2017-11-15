from tkinter import *

def calc_inter_margin( total_length, end_margins, num_spaces, space_width ):
	return ( total_length - ( 2 * end_margins ) - ( num_spaces * space_width ) ) / ( num_spaces - 1 )


def configure_character_space( fight, frame, x, y ):
	#highlighting based on target and turn status
	if( fight.turn == (x, y) ):
		frame.configure(  highlightbackground="red", highlightcolor="red" )
	if( fight.active_target == ( x, y ) ):
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
	char = fight.get_character( pos )
	if( fight.active_target_frame ):
		fight.active_target_frame.config( highlightbackground="black", highlightcolor="black" )

	fight.set_target( frame, pos )
	frame.config( highlightbackground="blue", highlightcolor="blue" )

	#this is damaging the new target
	char.take_damage( 1 )
	frame.winfo_children()[1].config( text=char.hp_meter )

def select_action(event, fight, index):
	frame = get_containing_frame( event )
	if( fight.active_action_frame ):
		fight.active_action_frame.config( highlightbackground="black", highlightcolor="black" )
	fight.set_action( frame, index )
	frame.config( highlightbackground="red", highlightcolor="red" )
