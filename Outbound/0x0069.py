from script_api import *

f = add_byte("Function")

if f == 4: # request maid craft item
    add_int("RecipeId")
    add_long("RecipeUid")
elif f == 10: # cancel craft
    add_long("RecipeUid")
