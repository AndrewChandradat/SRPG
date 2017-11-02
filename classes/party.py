lata = 2

'''
__init__( self )
add_member( self, new_member, col_num, row_num )
check_position( self, col_num, row_num )
get_pos( self, index )
is_alive( self )
take_aoe( self, dmg )
take_row_dmg( self, dmg, row_num )
take_col_dmg( self, dmg, col_num )
get_first_living( self )
'''


class Party:
	def __init__( self ):
		self.members = []

	def add_member( self, new_member, col_num, row_num ):
		if( self.check_position( col_num, row_num ) ):
			self.members.append( ( new_member.copy(), col_num, row_num ) )
			return True
		else:
			return False

	def check_position( self, col_num, row_num ):
		for person in self.members:
			if( person[1] == col_num and person[2] == row_num ):
				return False
		return True

	def get_pos( self, index ):
		if( index < self.members.length ):
			return (self.members[index][1], self.members[index][2])
		else:
			return ( 0, 0 )

	def is_alive( self ):
		for person in self.members:
			if( person[0].is_alive() ):
				return True
		return False

	def take_aoe( self, dmg ):
		for person in self.members:
			person[0].take_damage( dmg )

	def take_row_dmg( self, dmg, row_num ):
		for person in self.members:
			if( person[2] == row_num ):
				person[0].take_damage( dmg )

	def take_col_dmg( self, dmg, col_num ):
		for person in self.members:
			if( person[1] == col_num ):
				person[0].take_damage( dmg )

	def get_first_living( self ):
		for person in self.members:
			if( person[0].is_alive() ):
				return ( person[1], person[2] )
		return (0,0)
