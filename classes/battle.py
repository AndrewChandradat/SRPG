from classes.grid import Grid

'''
__init__( self, allies, enemies, num_cols, num_rows )
next_turn( self )								#goes to next character in turn order
set_turn( self, col, row )
set_action( self, action )
set_target( self, new_target )
is_ally_turn( self )
space_is_occupied( self, col_num, row_num )
get_character( self, pos )						# returns character instance at that position
active_character( self )						# returns active character instance
selected_action( self )							# returns actual action
target( self )									# returns the targeted character instance
execute( self )									# executes the active action on the active target
calc_damage( self, person, action )
choose_target( self, dmg, target )
'''

class Battle:
	def __init__( self, allies, enemies, num_cols, num_rows ):
		self.battlefield = Grid( num_cols, num_rows )
		self.allies = allies
		self.enemies = enemies
		self.battlefield.add_party( self.allies )
		self.battlefield.add_party( self.enemies )
		self.turn = (0, 0)

		self.active_action_frame = None
		self.active_action_index = None
		self.active_target_frame = None
		self.active_target_pos = None

		self.active_target = None
		self.next_turn()

	def next_turn( self ):		#goes to next character in turn order
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
		self.active_target_frame = None
		self.active_target_pos = None

	def set_turn( self, col, row ):
		self.turn = ( col, row )
		self.active_action_frame = None
		self.active_action_index = None

	def set_action( self, frame, index ):
		self.active_action_frame = frame
		self.active_action_index = index

	def set_target( self, frame, pos ):
		self.active_target_frame = frame
		self.active_target_pos = pos

	def is_ally_turn( self ):
		return self.turn[0] < self.battlefield.width / 2

	def space_is_occupied( self, col_num, row_num ):
		return self.battlefield.space_is_occupied( col_num, row_num )

	def get_character( self, pos ):
		return self.battlefield.get_character( pos[0], pos[1] )

	def active_character( self ):
		return self.battlefield.get_character( self.turn[0], self.turn[1] )

	def selected_action( self ):
		return self.active_character().get_action( self.active_action_index )

	def target( self ):
		return self.battlefield.get_character( active_target_pos[0], active_target_pos[1] )

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
			self.enemies.take_col_dmg( dmg, self.active_target_pos[1] )
		elif( target == Target.ROW ):
			self.enemies.take_row_dmg( dmg, self.active_target_pos[2] )
		elif( target == Target.SELF ):
			self.activeCharacter().take_damage( dmg );
		elif( target == Target.ALLY ):
			self.getTarget().take_damage( dmg )
		elif( target == Target.PARTY ):
			self.allies.take_aoe( dmg )



	# def add_rect_id( self, new_id, col, row ):
	# 	self.rect_ids[ new_id ] = ( col, row )
    #
	# def add_text_id( self, new_id, col, row ):
	# 	self.text_ids[ new_id ] = ( col, row )
    #
	# def get_pos( self, rect_id ):
	# 	return self.rect_ids[ rect_id ]
    #
	# def get_rect_id( self, col, row ):
	# 	return self.battlefield.get_rect_id( col, row )
	# #
	# # def get_text_id( self, col, row ):
	# # 	return self.battlefield.get_text_id( col, row )
