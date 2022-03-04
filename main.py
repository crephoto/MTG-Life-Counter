from setuptools import setup
import MTG_Life_Counter_Functions as mtg
pl_index = 3
player_num = mtg.startup()
life = mtg.setup(player_num)
players = mtg.player_names(player_num)
mtg.request_query(players, life)