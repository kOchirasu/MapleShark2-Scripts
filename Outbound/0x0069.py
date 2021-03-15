from script_api import *

f = AddByte("Function")

if f == 4: # request maid craft item
    AddInt("RecipeId")
    AddLong("RecipeUid")
elif f == 10: # cancel craft
    AddLong("RecipeUid")
