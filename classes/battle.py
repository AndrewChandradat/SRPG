from classes.grid import Grid

'''
__init__( self, allies, enemies, num_cols, num_rows )
next_turn( self )
is_ally_turn( self )
space_is_occupied( self, col_num, row_num )
get_character( self, col_num, row_num )
active_character( self )
selected_action( self )
target( self )									#returns the character instance
execute( self )
calc_damage( self, person, action )
choose_target( self, dmg, target )
set_target( self, new_id )
add_rect_id( self, new_id, col, row )
add_text_id( self, new_id, col, row )
get_pos( self, rect_id )
# get_rect_id( self, col, row )
# get_text_id( self, col, row )
'''

class Battle:
	def __init__( self, allies, enemies, num_cols, num_rows ):
		self.battlefield = Grid( num_cols, num_rows )
		self.allies = allies
		self.enemies = enemies
		self.battlefield.add_party( self.allies )
		self.battlefield.add_party( self.enemies )
		self.turn = (0, 0)
		self.active_action = 0
		self.active_target = None
		self.next_turn()
		self.rect_ids = {}
		self.text_ids = {}

	def next_turn( self ):
		x = self.turn[0]
		y = self.turn[1]
		while( True ):
			x = x + 1
			if( x == self.battlefield.width ):
				x = 0
				y = y + 1
			if( y == self.battlefield.height ):
				y = 0
			if( ( self.space_is_occupied( x, y ) and self.battlefield.character_is_alive( x, y ) )
				or 	( x == self.turn[0] and y == self.turn[1] ) ):
				break
		self.set_turn( x, y )
		self.active_target = None

	def set_turn( self, col, row ):
		self.turn = ( col, row )
		self.active_action = 0

	def is_ally_turn( self ):
		return self.turn[0] < self.battlefield.width / 2

	def space_is_occupied( self, col_num, row_num ):
		return self.battlefield.space_is_occupied( col_num, row_num )

	def get_character( self, col_num, row_num ):
		return self.battlefield.get_character( col_num, row_num )

	def active_character( self ):
		return self.battlefield.get_character( self.turn[0], self.turn[1] )

	def selected_action( self ):
		return self._active_character().get_action( self.active_action )

	def target( self ):
		return self.battlefield.get_character( rect_ids[ active_target ][0], rect_ids[ active_target ][1] )

	def execute( self ):
		dmg = self.calc_damage( self.active_character(), self.selected_action() )
		self.choose_target( dmg, self.selected_action().target )
		self.next_turn()

	def calc_damage( self, person, action ):
		if( action.modifier == Stat.STRENGTH ):
			return action.damage + person.strength
		else:
			return action.damage

	def choose_target( self, dmg, target ):
		if( target == Target.SINGLE ):
			self.Target().take_damage( dmg )
		elif( target == Target.ALL ):
			self.enemies.take_aoe( dmg )
		elif( target == Target.COLUMN ):
			self.enemies.take_col_dmg( dmg, self.activeTarget[1] )
		elif( target == Target.ROW ):
			self.enemies.take_row_dmg( dmg, self.activeTarget[2] )
		elif( target == Target.SELF ):
			self.activeCharacter().take_damage( dmg );
		elif( target == Target.ALLY ):
			self.getTarget().take_damage( dmg )
		elif( target == Target.PARTY ):
			self.allies.take_aoe( dmg )

	def set_target( self, new_target ):
		self.active_target = new_target

	def add_rect_id( self, new_id, col, row ):
		self.rect_ids[ new_id ] = ( col, row )

	def add_text_id( self, new_id, col, row ):
		self.text_ids[ new_id ] = ( col, row )

	def get_pos( self, rect_id ):
		return self.rect_ids[ rect_id ]

	def get_rect_id( self, col, row ):
		return self.battlefield.get_rect_id( col, row )
	#
	# def get_text_id( self, col, row ):
	# 	return self.battlefield.get_text_id( col, row )
