from classes.action import Target, Stat, Action

heal = Action("Heal", "Heal one target", -1, Target.SINGLE, Stat.INTELLIGENCE)
fireball = Action( "Fireball", "Deal fire damage to one target", 2, Target.SINGLE, Stat.INTELLIGENCE )
