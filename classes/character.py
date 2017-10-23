#import action

from classes.action import Target, Stat, Action

attack = Action( "Attack", "", 1, Target.SINGLE, Stat.STRENGTH )

class Character:
	def __init__( self, name, hp = 10, strength = 1 ):
		self.name = name
		self.hp = hp
		self.strength = strength
		self.movelist = []
		self.addAction( attack )


	def addAction( self, new_action ):
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

	def takeDamage( self, dmg ):
		self.currHP -= dmg;
		if( self.currHP < 1 ):
			self.currHP = 0
		elif( self.currHP > self.maxHP ):
			self.currHP = self.maxHP

	def isAlive( self ):
		return self.currHP > 0

	def isDead( self ):
		return not self.isAlive()

	def actions( self ):
		return self.original.movelist

	def getAction( self, index ):
		return self.original.movelist[index]

	def name( self ):
		return self.original.name
