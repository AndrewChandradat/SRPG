from classes.character import *
from actions.spells import *

goblin = Character( "Goblin", False )

goblin_mage = Character( "Goblin Mage", False )
goblin_mage.add_action( fireball )

goblin_shaman = Character( "Goblin Shaman", False )
goblin_shaman.add_action( heal )


def goblin_ai( fight ):
	fight.active_target_pos = fight.allies.get_first_living()
	fight.active_action_index = 0

def goblin_mage_ai( fight ):
	fight.active_target_pos = fight.allies.get_first_living()
	fight.active_action_index = 1

def goblin_shaman_ai( fight ):
	target_pos = fight.enemies.get_lowest_hp()
	if( target_pos ):
		fight.active_target_pos = target_pos
		fight.active_action_index = 1
	else:
		fight.active_target_pos = player_party.get_first_living()
		fight.active_action_index = 0



goblin.ai = goblin_ai
goblin_mage.ai = goblin_mage_ai
goblin_shaman.ai = goblin_shaman_ai
