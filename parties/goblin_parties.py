from classes.party import *
from characters.goblins import *

goblin_p1 = Party()
goblin_p1.add_member( goblin, 3, 0 )
goblin_p1.add_member( goblin, 3, 2 )


goblin_p2 = Party()
goblin_p2.add_member( goblin, 4, 0 )
goblin_p2.add_member( goblin_mage, 3, 1 )
goblin_p2.add_member( goblin_shaman, 5, 2 )
