from classes.grid import Grid

class Battle:
	def __init__( self, allies, enemies, num_cols, num_rows ):
		self.battlefield = Grid( num_cols, num_rows )
		self.allies = allies
		self.enemies = enemies
		self.battlefield.addParty( self.allies )
		self.battlefield.addParty( self.enemies )
		self.turn = (0, 0)
		self.activeAction = 0
		self.activeTarget = ( 0, 0 )
		self.nextTurn()


	def nextTurn( self ):
		x = self.turn[0]
		y = self.turn[1]
		while( True ):
			x = x + 1
			if( x == self.battlefield.width ):
				x = 0
				y = y + 1
			if( y == self.battlefield.height ):
				y = 0
			if( ( self.spaceIsOccupied( x, y ) and self.battlefield.characterIsAlive( x, y ) )
				or 	( x == self.turn[0] and y == self.turn[1] ) ):
				break
		self.turn = ( x, y )
		self.activeAction = 0
		self.activeTarget = self.enemies.getFirstLiving()

	def isAllyTurn( self ):
		return self.turn[0] < self.battlefield.width / 2

	def spaceIsOccupied( self, col_num, row_num ):
		return self.battlefield.spaceIsOccupied( col_num, row_num )

	def getCharacter( self, col_num, row_num ):
		return self.battlefield.getCharacter( col_num, row_num )

	def ActiveCharacter( self ):
		return self.battlefield.getCharacter( self.turn[0], self.turn[1] )

	def SelectedAction( self ):
		return self.ActiveCharacter().getAction( self.activeAction )

	def Target( self ):
		return self.battlefield.getCharacter( self.activeTarget[0], self.activeTarget[1] )

	def execute():
		dmg = self.calcDamage( self.ActiveCharacter(), self.selectedAction() )
		self.chooseTarget( dmg, self.selectedAction().target )
		self.nextTurn()

	def calcDamage( person, action ):
		if( action.modifier == Stat.STRENGTH ):
			return action.damage + person.strength
		else:
			return action.damage

	def chooseTarget( dmg, target ):
		if( target == Target.SINGLE ):
			self.Target().takeDamage( dmg )
		elif( target == Target.ALL ):
			self.enemies.takeAoE( dmg )
		elif( target == Target.COLUMN ):
			self.enemies.takeColDmg( dmg, self.activeTarget[1] )
		elif( target == Target.ROW ):
			self.enemies.takeRowDmg( dmg, self.activeTarget[2] )
		elif( target == Target.SELF ):
			self.activeCharacter().takeDamage( dmg );
		elif( target == Target.ALLY ):
			self.getTarget().takeDamage( dmg )
		elif( target == Target.PARTY ):
			self.allies.takeAoE( dmg )
