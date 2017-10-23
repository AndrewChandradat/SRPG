from tkinter import *

from classes.character import Character, CharacterInstance
from classes.party import Party
from classes.battle import Battle

andrew = Character( "Andrew" )
bob = Character( "Bob" )
goblin = Character( "Goblin" )

p1 = Party()
p1.addMember( andrew, 2, 1 )
p1.addMember( bob, 1, 0 )

p2 = Party()
p2.addMember( goblin, 4, 0 )
p2.addMember( goblin, 3, 1 )
p2.addMember( goblin, 5, 2 )

fight = Battle( p1, p2, 6, 3 )

def calc_inter_margin( total_length, end_margins, num_spaces, space_width ):
	return ( total_length - ( 2 * end_margins ) - ( num_spaces * space_width ) ) / ( num_spaces - 1 )

root = Tk()

canvas_width = 1400
canvas_height = 550

num_rows = 3
num_cols = 6

rec_width = 200
rec_height = 125

side_margin = 50
top_margin = 50

inter_horiz_margin = calc_inter_margin( canvas_width, side_margin, num_cols, rec_width )
inter_vert_margin = calc_inter_margin( canvas_height, top_margin, num_rows, rec_height )

w = Canvas( root, width=canvas_width, height=canvas_height )
w.pack()

for y in range( 0, fight.battlefield.height ):
	for x in range( 0, fight.battlefield.width ):
		topleft_x = side_margin + ( x * ( rec_width + inter_horiz_margin ) )
		topleft_y = top_margin + ( y * ( rec_height + inter_vert_margin ) )
		w.create_rectangle( topleft_x, topleft_y, topleft_x + rec_width, topleft_y + rec_height, fill="white" )
		if( fight.spaceIsOccupied( x, y ) ):
			w.create_text( topleft_x + (rec_width/2), topleft_y + (rec_height/2), text=fight.getCharacter( x, y ) )

root.mainloop()
