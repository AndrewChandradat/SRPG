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

def hello( event, name ):
	print( name )

def target_char( event, coord):
	fight.set_target( coord )

def change_cursor( event, canvas, is_enter ):
	if (is_enter):
		canvas.config( cursor="hand2" )
	else:
		canvas.config( cursor="arrow" )

def callsomethingaboutnewturn( event, canvas ):
	canvas.itemconfigure( fight.get_rect_id( fight.target()[0], fight.target()[1] ), outline="red" )

root = Tk()


canvas_width = 1400
canvas_height = 550
num_cols = 6
num_rows = 3
rec_width = 200
rec_height = 125
side_margin = 50
top_margin = 50

inter_horiz_margin = calc_inter_margin( canvas_width, side_margin, num_cols, rec_width )
inter_vert_margin = calc_inter_margin( canvas_height, top_margin, num_rows, rec_height )

canvas = Canvas( root, width=canvas_width, height=canvas_height, cursor="arrow" )
#canvas.event_add("<NextTurn>")
canvas.pack()

for y in range( 0, fight.battlefield.height ):
	for x in range( 0, fight.battlefield.width ):
		topleft_x = side_margin + ( x * ( rec_width + inter_horiz_margin ) ) 	#calculating rect positions
		topleft_y = top_margin + ( y * ( rec_height + inter_vert_margin ) )		#calculating rect positions
		rect_id = canvas.create_rectangle( topleft_x, topleft_y, topleft_x + rec_width, topleft_y + rec_height, fill="white")
		fight.battlefield.set_rect_id( x, y, rect_id )

		if( fight.space_is_occupied( x, y ) ):
			if( fight.turn == ( x, y ) ):
				canvas.itemconfigure( rect_id, outline="red", width=2 )

			text_id = canvas.create_text( topleft_x + (rec_width/2), topleft_y + (rec_height/2), text=fight.get_character( x, y ).name() )
			fight.battlefield.set_text_id( x, y, text_id )
			canvas.itemconfigure( rect_id, activewidth=2 )
			canvas.tag_bind( rect_id, '<Enter>', lambda event, c=canvas: change_cursor( event, canvas, True ) )
			canvas.tag_bind( rect_id, '<Leave>', lambda event, c=canvas: change_cursor( event, canvas, False ) )
			#canvas.tag_bind( rect_id, '<Button-1>', lambda event, name=fight.getCharacter( x, y ).name(): hello( event, name ) )
			#canvas.tag_bind( rect_id, '<Button-3>', lambda event, coord=(x, y): hello( event, coord ) )




root.mainloop()
