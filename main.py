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



canvas_width = 1300
battle_area_height = 400
action_area_height = 150
canvas_height = battle_area_height + action_area_height
num_cols = 6
num_rows = 3
rec_width = 175
rec_height = 100
side_margin = 25
top_margin = 25

inter_horiz_margin = calc_inter_margin( canvas_width, side_margin, num_cols, rec_width )
inter_vert_margin = calc_inter_margin( battle_area_height, top_margin, num_rows, rec_height )

root = Tk()
canvas = Canvas( root, width=canvas_width, height=canvas_height, cursor="arrow" )
canvas.pack()

for y in range( 0, fight.battlefield.height ):
	for x in range( 0, fight.battlefield.width ):
		topleft_x = side_margin + ( x * ( rec_width + inter_horiz_margin ) ) 	#calculating rect positions
		topleft_y = top_margin + ( y * ( rec_height + inter_vert_margin ) )		#calculating rect positions
		rect_id = canvas.create_rectangle( topleft_x, topleft_y, topleft_x + rec_width, topleft_y + rec_height, fill="white", width=2)
		fight.add_rect_id( rect_id, x, y )

		if( fight.space_is_occupied( x, y ) ):
			if( fight.turn == ( x, y ) ):
				canvas.itemconfigure( rect_id, outline="red" )

			if( fight.active_target == ( x, y) ):
				canvas.itemconfigure( rect_id, dash=( 10, 5 ) )

			canvas.itemconfig( rect_id, tags="combatant" )
			text_id = canvas.create_text( topleft_x + (rec_width/2), topleft_y + (rec_height/2), text=fight.get_character( x, y ).name() )
			fight.add_text_id( text_id, x, y )

canvas.itemconfigure( "combatant", activewidth=3 )
canvas.tag_bind( "combatant", '<Enter>', lambda event: change_cursor( event, True ) )
canvas.tag_bind( "combatant", '<Leave>', lambda event: change_cursor( event, False ) )
canvas.tag_bind( "combatant", '<Button-1>', lambda event: target_char( event, fight ) )



root.mainloop()
