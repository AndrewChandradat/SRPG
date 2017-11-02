from classes.action import Target, Stat, Action

'''
Character
__init__( self, name, hp = 10, strength = 1 )
add_action( self, new_action )
copy( self )

CharacterInstance
__init__( self, original )
__str__( self )
take_damage( self, dmg )
is_alive( self )
is_dead( self )
actions( self )
get_action( self, index )
name( self )
'''

attack = Action( "Attack", "", 1, Target.SINGLE, Stat.STRENGTH )

class Character:
	def __init__( self, name, hp = 10, strength = 1 ):
		self.name = name
		self.hp = hp
		self.strength = strength
		self.movelist = []
		self.add_action( attack )


	def add_action( self, new_action ):
		self.movelist.append( new_action )

	def copy( self ):
		return CharacterInstance( self )


class CharacterInstance:
	def __init__( self, original ):
		self.original = original
		self.maxHP = original.hp
		self.currHP = original.hp
		self.strength = original.strength

	def __str__( self ):
		return self.original.name

	def take_damage( self, dmg ):
		self.currHP -= dmg;
		if( self.currHP < 1 ):
			self.currHP = 0
		elif( self.currHP > self.maxHP ):
			self.currHP = self.maxHP

	def is_alive( self ):
		return self.currHP > 0

	def is_dead( self ):
		return not self.is_alive()

	def actions( self ):
		return self.original.movelist

	def get_action( self, index ):
		return self.original.movelist[index]

	def name( self ):
		return self.original.name
