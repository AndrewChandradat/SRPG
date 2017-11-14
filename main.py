from tkinter import *

from classes.character import Character, CharacterInstance
from classes.party import Party
from classes.battle import Battle
from ui import *

#Game creation stuff

andrew = Character( "Andrew" )
bob = Character( "Bob" )
goblin = Character( "Goblin" )

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
SIDE_MARGIN = 25
TOP_MARGIN = 25

inter_horiz_margin = calc_inter_margin( CANVAS_WIDTH, SIDE_MARGIN, NUM_COLS, REC_WIDTH )
inter_vert_margin = calc_inter_margin( BATTLE_AREA_HEIGHT, TOP_MARGIN, NUM_ROWS, REC_HEIGHT )

root = Tk()
root.configure( bg="white" )

for y in range( 0, fight.battlefield.height ):
	for x in range( 0, fight.battlefield.width ):

		frame = Frame( root, height=REC_HEIGHT, width=REC_WIDTH, bg="white",
						highlightbackground="black", highlightcolor="black", highlightthickness=2, )
		frame.grid( column=x, row=y, padx=inter_horiz_margin, pady=inter_vert_margin )
		frame.grid_propagate(0)

		if( fight.space_is_occupied( x, y ) ):
			if( fight.turn == (x, y) ):
				frame.configure(  highlightbackground="red", highlightcolor="red" )

			if( fight.active_target == ( x, y ) ):
				frame.configure( highlightbackground=None, highlightcolor=None, relief="groove", bd=5 )

			frame.configure( cursor="hand2" )
			frame.columnconfigure(0, weight=1)
			frame.rowconfigure( 0, weight=1 )
			frame.rowconfigure( 1, weight=2 )
			char = fight.get_character( (x, y) )
			name = Label( frame, text=char.name(), bg="white" )
			hp = Label( frame, text=char.hp_meter, bg="white" )
			name.grid( sticky=S, columnspan=2 )
			hp.grid( )

			frame.bind("<Button-1>", lambda e, f=fight, pos=(x,y): target_char( e, f, pos ))

root.mainloop()
