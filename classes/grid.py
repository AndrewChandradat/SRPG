lata = 2

'''
Square
__init__( self )
get_character( self )
add_character( self, new_person )
is_occupied( self )


Grid
__init__(self, num_cols, num_rows )
add_character( self, person, col_num, row_num )
add_party( self, party )
get_character( self, col_num, row_num )
space_is_occupied( self, col_num, row_num )
character_is_dead( self, col_num, row_num )
character_is_Alive( self, col_num, row_num )
# set_rect_id( self, col_num, row_num, rectID )
# get_rect_id( self, col_num, row_num )
# set_text_id( self, col_num, row_num, textID )
# get_text_id( self, col_num, row_num )
'''

class Square:
	def __init__( self ):
		self.occupant = None
		self.rectID = None
		self.textID = None

	def get_character( self ):
		return self.occupant

	def add_character( self, new_person ):
		if( self.occupant ):
			return False
		else:
			self.occupant = new_person
			return True

	def is_occupied( self ):
		if( self.occupant ):
			return True
		else:
			return False

class Grid:
	def __init__(self, num_cols, num_rows ):
		self.height = num_rows
		self.width = num_cols
		self.spaces = [ [ Square() for x in range(num_rows) ] for y in range(num_cols) ]

	def add_character( self, person, col_num, row_num ):
		return self.spaces[col_num][row_num].add_character( person )

	def add_party( self, party ):
		for person in party.members:
			if( not self.add_character( person[0], person[1], person[2] ) ):
				return False
		return True

	def get_character( self, col_num, row_num ):
		return self.spaces[col_num][row_num].get_character()

	def space_is_occupied( self, col_num, row_num ):
		return self.spaces[ col_num ][ row_num ].is_occupied()

	def character_is_dead( self, col_num, row_num ):
		return self.spaces[ col_num ][ row_num ].get_character().is_dead()

	def character_is_alive( self, col_num, row_num ):
		return self.spaces[ col_num ][ row_num ].get_character().is_alive()

	#
	# def set_rect_id( self, col_num, row_num, rectID ):
	# 	self.spaces[ col_num ][ row_num ].rectID = rectID
	#
	# def get_rect_id( self, col_num, row_num ):
	# 	return self.spaces[ col_num ][ row_num ].rectID
	#
	# def set_text_id( self, col_num, row_num, textID ):
	# 	self.spaces[ col_num ][ row_num ].textID = textID
	#
	# def get_text_id( self, col_num, row_num ):
	# 	return self.spaces[ col_num ][ row_num ].textID
