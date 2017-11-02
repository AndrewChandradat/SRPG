from classes.grid import Grid

'''
__init__( self, allies, enemies, num_cols, num_rows )
nextTurn( self )
isAllyTurn( self )
spaceIsOccupied( self, col_num, row_num )
getCharacter( self, col_num, row_num )
ActiveCharacter( self )
SelectedAction( self )
Target( self )
execute( self )
calcDamage( self, person, action )
chooseTarget( self, dmg, target )
setTarget( self, coord )
get_rect_id( self, col, row )
get_text_id( self, col, row )
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
		self.active_target = ( 0, 0 )
		self.next_turn()

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
		self.active_target = self.enemies.get_first_living()

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
		return self.battlefield.get_character( self.active_target[0], self.active_target[1] )

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

	def setTarget( self, coord ):
		self.active_target = coord

	def get_rect_id( self, col, row ):
		return self.battlefield.get_rect_id( col, row )

	def get_text_id( self, col, row ):
		return self.battlefield.get_text_id( col, row )
