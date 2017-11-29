from tkinter import *
import PIL.Image
from PIL import ImageTk
from ui.events import *
from config import *


def create_battlefield( root, fight ):
	set_defaults( root )
	create_character_spaces( root, fight )
	create_action_bar( root, fight )
	create_sidebar( root, fight )

def set_defaults( root ):
	root.configure( bg = "white" )
	root.option_add( "*Frame.background", "white" )
	root.option_add( "*Frame.HighlightBackground", "black" )
	root.option_add( "*Frame.HighlightColor", "black" )
	root.option_add( "*Frame.HighlightThickness", "2" )

def create_character_spaces( root, fight ):
	for y in range( 0, fight.battlefield.height ):
		for x in range( 0, fight.battlefield.width ):
			frame = Frame( root, height = REC_HEIGHT, width = REC_WIDTH )
			frame.grid( column = x, row = y, padx = INTER_HORIZ_MARGIN, pady = INTER_VERT_MARGIN )
			frame.grid_propagate( 0 )

			if( fight.space_is_occupied( x, y ) ):
				configure_character_space( fight, frame, x, y )

def configure_character_space( fight, frame, x, y ):
	#highlighting based on target and turn status
	if( fight.turn == (x, y) ):
		frame.configure(  highlightbackground="red", highlightcolor="red" )
		fight.active_character_frame = frame
	if( fight.active_target_pos == ( x, y ) ):
		frame.configure( highlightbackground="blue", highlightcolor="blue" )
		fight.active_target_frame = frame
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


def create_action_bar( root, fight ):
	action_bar = Frame( root, height = ACTION_AREA_HEIGHT, width = BATTLE_AREA_WIDTH + ( 2 * SIDE_MARGIN ) )
	action_bar.grid( row = fight.battlefield.height + 1, columnspan = fight.battlefield.width, pady = 10 )
	action_bar.grid_propagate( 0 )
	fight.action_bar_frame = action_bar
	populate_action_list( fight )


def create_sidebar( root, fight ):
	sidebar = Frame( root, height = SIDEBAR_HEIGHT, width = SIDEBAR_WIDTH )
	sidebar.grid( row = 0, rowspan = 7, column = fight.battlefield.width + 1, padx = 20 )
	sidebar.grid_propagate( 0 )
	#execute button
	execute_frame = Frame( sidebar, height = EXECUTE_HEIGHT, width = SIDEBAR_WIDTH - 4, cursor = "hand2", highlightthickness = 0 )
	execute_frame.grid()
	execute_frame.grid_propagate( 0 )
	#execute icon
	execute_icon = load_and_resize_image( EXECUTE_ICON_PATH, 64, 64 )
	execute_label = Label( execute_frame, image = execute_icon, height = EXECUTE_HEIGHT, width = SIDEBAR_WIDTH-10, bg="white" )
	execute_label.image = execute_icon
	execute_label.grid()
	execute_label.bind( "<Button-1>", lambda e, f = fight: execute_action( e, f ) )
	root.bind( "<space>", lambda e, f = fight: execute_action( e, f ) )
	# border beneath execute button
	bottom_execute_border = Frame( sidebar, height=2, width=SIDEBAR_WIDTH-4, )
	bottom_execute_border.grid()

def load_and_resize_image( path, height, width ):
	img = PIL.Image.open(path).resize( (height, width), PIL.Image.NEAREST )
	return ImageTk.PhotoImage( img )
