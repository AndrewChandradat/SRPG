from tkinter import *

from classes.character import Character, CharacterInstance
from classes.party import Party
from classes.battle import Battle
from classes.action import Action, Target, Stat
from ui import *

#Game creation stuff

andrew = Character( "Andrew" )
bob = Character( "Bob" )
goblin = Character( "Goblin" )

heal = Action("Heal", "Heal one target", -1, Target.SINGLE, Stat.STRENGTH )
bob.add_action( heal )

p1 = Party()
p1.add_member( andrew, 2, 1 )
p1.add_member( bob, 1, 0 )

p2 = Party()
p2.add_member( goblin, 4, 0 )
p2.add_member( goblin, 3, 1 )
p2.add_member( goblin, 5, 2 )

fight = Battle( p1, p2, 6, 3 )
#//////////////////////////



CANVAS_WIDTH = 1200
BATTLE_AREA_HEIGHT = 380
ACTION_AREA_HEIGHT = 150
CANVAS_HEIGHT = BATTLE_AREA_HEIGHT + ACTION_AREA_HEIGHT
NUM_COLS = 6
NUM_ROWS = 3
REC_WIDTH = 175
REC_HEIGHT = 100
ACTION_TOP_MARGIN = 25
ACTION_SIDE_MARGIN = 20
ACTION_HEIGHT = ACTION_AREA_HEIGHT - (2*ACTION_TOP_MARGIN)
ACTION_WIDTH = 150
SIDE_MARGIN = 25
TOP_MARGIN = 25

inter_horiz_margin = calc_inter_margin( CANVAS_WIDTH, SIDE_MARGIN, NUM_COLS, REC_WIDTH )
inter_vert_margin = calc_inter_margin( BATTLE_AREA_HEIGHT, TOP_MARGIN, NUM_ROWS, REC_HEIGHT )

root = Tk()
root.configure( bg="white" )
#BATTLEFIELD
for y in range( 0, fight.battlefield.height ):
	for x in range( 0, fight.battlefield.width ):

		frame = Frame( root, height=REC_HEIGHT, width=REC_WIDTH, bg="white",
						highlightbackground="black", highlightcolor="black", highlightthickness=2, )
		frame.grid( column=x, row=y, padx=inter_horiz_margin, pady=inter_vert_margin )
		frame.grid_propagate(0)

		if( fight.space_is_occupied( x, y ) ):
			configure_character_space( fight, frame, x, y )


#ACTION BAR
action_bar = Frame( root, height=ACTION_AREA_HEIGHT, width=CANVAS_WIDTH+(2*SIDE_MARGIN), bg="white",
					highlightbackground="black", highlightcolor="black", highlightthickness=2, )
action_bar.grid( row=fight.battlefield.height+1, columnspan=fight.battlefield.width, pady=10 )
action_bar.grid_propagate( 0 )

action_count = 0
for action in fight.active_character().movelist():

	action_frame = Frame( action_bar, height=ACTION_HEIGHT, width=ACTION_WIDTH, bg="white",
							highlightbackground="black", highlightcolor="black", highlightthickness=1,
							cursor="hand2")
	action_frame.grid( row=0, column=action_count, padx=SIDE_MARGIN, pady=ACTION_TOP_MARGIN )
	action_frame.grid_propagate( 0 )
	action_frame.columnconfigure(0, weight=1)

	if( action_count == fight.active_action_index ):
		action_frame.config( highlightbackground="red", highlightcolor="red", highlightthickness=1 )

	action_name = Label( action_frame, text=action.name, bg="white" )
	action_name.grid()

	action_frame.bind( "<Button-1>", lambda e, f=fight, index=action_count: select_action( e, f, index ))


	action_count = action_count + 1

root.mainloop()
