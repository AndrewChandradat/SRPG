from enum import Enum

class Stat( Enum ):
	NONE = 0
	HP = 1
	MP = 2
	STRENGTH = 3

class Target( Enum ):
	SINGLE = 1
	ALL = 2
	ROW = 3
	COLUMN = 4
	SELF = 5
	ALLY = 6
	PARTY = 7

class Action:
	def __init__( self, name, description, damage, target, stat ):
		self.name = name
		self.desc = description
		self.damage = damage
		self.target = target
		self.modifier = stat

	def ally_targeted( self ):
		return ( self.target == Target.SELF ) or ( self.target == Target.ALLY ) or ( self.target == Target.PARTY )

	def enemy_targeted( self ):
		return not self.ally_targeted()
