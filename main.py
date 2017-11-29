from tkinter import Tk
from classes.battle import Battle
from parties.player_party import player_party
from parties.goblin_parties import goblin_p1
from ui.display import create_battlefield



fight = Battle( player_party, goblin_p1, 6, 3 )
root = Tk()
create_battlefield( root, fight )
root.mainloop()
