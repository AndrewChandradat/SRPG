class Square:
	def __init__( self ):
		self.occupant = None

	def getCharacter( self ):
		return self.occupant

	def addCharacter( self, new_person ):
		if( self.occupant ):
			return False
		else:
			self.occupant = new_person
			return True

	def isOccupied( self ):
		if( self.occupant ):
			return True
		else:
			return False

class Grid:
	def __init__(self, num_cols, num_rows ):
		self.height = num_rows
		self.width = num_cols
		self.spaces = [ [ Square() for x in range(num_rows) ] for y in range(num_cols) ]

	def addCharacter( self, person, col_num, row_num ):
		return self.spaces[col_num][row_num].addCharacter( person )

	def addParty( self, party ):
		for person in party.members:
			if( not self.addCharacter( person[0], person[1], person[2] ) ):
				return False
		return True

	def getCharacter( self, col_num, row_num ):
		return self.spaces[col_num][row_num].getCharacter()

	def spaceIsOccupied( self, col_num, row_num ):
		return self.spaces[ col_num ][ row_num ].isOccupied()

	def characterIsDead( self, col_num, row_num ):
		return self.spaces[ col_num ][ row_num ].getCharacter().isDead()

	def characterIsAlive( self, col_num, row_num ):
		return self.spaces[ col_num ][ row_num ].getCharacter().isAlive()
