from tkinter import *
import PIL.Image
from PIL import ImageTk
from classes.character import Character, CharacterInstance
from classes.party import Party
from classes.battle import Battle
from classes.action import Action, Target, Stat
from characters.goblins import *
from ui import *
from config import *
#Game creation stuff

andrew = Character( "Andrew" )
bob = Character( "Bob" )

#bob.add_action( heal )


p1 = Party()
p1.add_member( andrew, 2, 1 )
p1.add_member( bob, 1, 0 )

p2 = Party()
p2.add_member( goblin, 4, 0 )
p2.add_member( goblin_mage, 3, 1 )
p2.add_member( goblin_shaman, 5, 2 )

fight = Battle( p1, p2, 6, 3 )
#//////////////////////////


root = Tk()
root.configure( bg="white" )
root.option_add("*Frame.background", "white")
root.option_add("*Frame.HighlightBackground", "black")
root.option_add("*Frame.HighlightColor", "black")
root.option_add("*Frame.HighlightThickness", "2")

#images
execute_icon = PIL.Image.open("assets/execute4.png").resize( (64, 64), PIL.Image.NEAREST )
execute_final = ImageTk.PhotoImage( execute_icon )


#BATTLEFIELD
for y in range( 0, fight.battlefield.height ):
	for x in range( 0, fight.battlefield.width ):
		frame = Frame( root, height=REC_HEIGHT, width=REC_WIDTH )
		frame.grid( column=x, row=y, padx=INTER_HORIZ_MARGIN, pady=INTER_VERT_MARGIN )
		frame.grid_propagate(0)

		if( fight.space_is_occupied( x, y ) ):
			configure_character_space( fight, frame, x, y )


#ACTION BAR
action_bar = Frame( root, height=ACTION_AREA_HEIGHT, width=BATTLE_AREA_WIDTH+(2*SIDE_MARGIN) )
action_bar.grid( row=fight.battlefield.height+1, columnspan=fight.battlefield.width, pady=10 )
action_bar.grid_propagate( 0 )
fight.action_bar_frame = action_bar

#populate action list
populate_action_list( fight )


#SIDEBAR
sidebar = Frame( root, height=SIDEBAR_HEIGHT, width=SIDEBAR_WIDTH )
sidebar.grid( row=0, rowspan=7, column=fight.battlefield.width + 1, padx=20 )
sidebar.grid_propagate(0)

execute_frame = Frame( sidebar, height=EXECUTE_HEIGHT, width=SIDEBAR_WIDTH-4, cursor="hand2", highlightthickness=0 )
execute_frame.grid()

execute_label = Label( execute_frame, image=execute_final, height=EXECUTE_HEIGHT, width=SIDEBAR_WIDTH-10, bg="white" )
execute_label.grid()
execute_label.bind( "<Button-1>", lambda e, f = fight: execute_action( e, f ) )

#put border beneath execute button
bottom_execute_border = Frame( sidebar, height=2, width=SIDEBAR_WIDTH-4, )
bottom_execute_border.grid()



root.mainloop()
