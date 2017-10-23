class Party:
	def __init__( self ):
		self.members = []

	def addMember( self, newMember, col_num, row_num ):
		if( self.checkPosition( col_num, row_num ) ):
			self.members.append( ( newMember.copy(), col_num, row_num ) )
			return True
		else:
			return False

	def checkPosition( self, col_num, row_num ):
		for person in self.members:
			if( person[1] == col_num and person[2] == row_num ):
				return False
		return True

	def getPos( self, index ):
		if( index < self.members.length ):
			return (self.members[index][1], self.members[index][2])
		else:
			return ( 0, 0 )

	def isAlive( self ):
		for person in self.members:
			if( person[0].isAlive() ):
				return True
		return False

	def takeAoE( self, dmg ):
		for person in self.members:
			person[0].takeDamage( dmg )

	def takeRowDmg( self, dmg, row_num ):
		for person in self.members:
			if( person[2] == row_num ):
				person[0].takeDamage( dmg )

	def takeColDmg( self, dmg, col_num ):
		for person in self.members:
			if( person[1] == col_num ):
				person[0].takeDamage( dmg )

	def getFirstLiving( self ):
		for person in self.members:
			if( person[0].isAlive ):
				return ( person[1], person[2] )
		return (0,0)
