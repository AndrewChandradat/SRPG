from classes.action import Target, Stat, Action
from actions.attacks import attack
'''
Character
__init__( self, name, hp = 10, strength = 1 )
add_action( self, new_action )
copy( self )

CharacterInstance
__init__( self, original )
__str__( self )
take_damage( self, dmg )
change_hp(self)
is_alive( self )
is_dead( self )
is_npc( self )
actions( self )
get_action( self, index )
name( self )
'''

class Character:
	def __init__( self, name, playable=True, hp = 10, strength = 1, intelligence = 1,   ):
		self.name = name
		self.hp = hp
		self.strength = strength
		self.intelligence = intelligence
		self.movelist = []
		self.add_action( attack )
		self.playable = playable

	def add_action( self, new_action ):
		self.movelist.append( new_action )

	def copy( self ):
		return CharacterInstance( self )

	def ai( self, fight ):
		print("Called non-existant ai")



class CharacterInstance:
	def __init__( self, original, ):
		self.original = original
		self.max_hp = original.hp
		self.curr_hp = original.hp
		self.hp_meter = ""
		self.change_hp()
		self.strength = original.strength
		self.intelligence = original.intelligence


	def __str__( self ):
		return self.original.name

	def take_damage( self, dmg ):
		self.curr_hp -= dmg;
		if( self.curr_hp < 1 ):
			self.curr_hp = 0
		elif( self.curr_hp > self.max_hp ):
			self.curr_hp = self.max_hp
		self.change_hp()

	def change_hp(self):
		self.hp_meter = str( self.curr_hp) + "/" + str( self.max_hp)

	def is_alive( self ):
		return self.curr_hp > 0

	def is_dead( self ):
		return not self.is_alive()

	def is_npc( self ):
		return not self.original.playable

	def actions( self ):
		return self.original.movelist

	def get_action( self, index ):
		return self.original.movelist[index]

	def name( self ):
		return self.original.name

	def movelist( self ):
		return self.original.movelist

	def automate( self, fight ):
		self.original.ai( fight )
		#just setting the frame to something so that ui.execute_action() works
		fight.active_action_frame = 1
