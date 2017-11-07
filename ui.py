def calc_inter_margin( total_length, end_margins, num_spaces, space_width ):
	return ( total_length - ( 2 * end_margins ) - ( num_spaces * space_width ) ) / ( num_spaces - 1 )


def change_cursor( event, is_enter ):
	if (is_enter):
		event.widget.config( cursor="hand2" )
	else:
		event.widget.config( cursor="arrow" )

def target_char( event, fight):
	canvas = event.widget
	prev_target = fight.active_target
	new_target = canvas.find_closest( event.x, event.y )
	
	canvas.itemconfig( prev_target, dash=(), activedash=() )
	fight.set_target( new_target )
	canvas.itemconfig( new_target, dash=( 10, 5 ), activedash=( 15, 10 ) )
