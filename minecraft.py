
import time
import random
import sys
inventory = {"Wood": 0, "Stick": 0, "Coal": 0, "Wool": 0, "Cobblestone": 0, "Iron": 0, "Gold": 0, "Diamond": 0,}
ores = {"Iron Ore": 0, "Gold Ore": 0,}
loot_check = {"Village":False, "Shipwreck":False}
weapons = {"Fists": 0, "Wooden Sword": 1, "Stone Sword": 2, "Iron Sword": 3, "Diamond Sword": 4,}
pickaxes = {"Fists": 0, "Wooden Pickaxe": 1, "Stone Pickaxe": 2, "Iron Pickaxe": 3, "Diamond Pickaxe": 5,} 
player_weapon = "Fists"
player_pickaxe = "Fists"
weapon_dmg = {"Fists": 1, "Wooden Sword": 2, "Stone Sword": 3, "Iron Sword": 4, "Diamond Sword": 5,}
player_damage = weapon_dmg.get(player_weapon, 0)

recipes = {
    "Wooden Pickaxe": {"Wood": 3, "Stick": 2},
    "Stone Pickaxe": {"Stick": 2, "Cobblestone": 3},
    "Iron Pickaxe": {"Stick": 2, "Iron": 3},
    "Diamond Pickaxe": {"Diamond": 3, "Stick": 2,},
    "Furnace": {"Cobblestone": 8},
    "Bed": {"Wood": 3, "Wool": 3},
    "Sticks": {"Wood": 1},
    "Torches":{"Stick": 1, "Coal": 1},
    "Wooden Sword": {"Stick": 1, "Wood": 2},
    "Stone Sword": {"Stick": 1, "Cobblestone": 2},
    "Iron Sword": {"Stick": 1, "Iron": 2},
    "Diamond Sword": {"Diamond": 2, "Stick": 1,}
}

tools_check = {
    "Wooden Pickaxe": False,
    "Stone Pickaxe":False,
    "Iron Pickaxe":False,
    "Diamond Pickaxe":False,
    "Furnace":False, 
    "Bed":False, 
    "Wooden Sword":False, 
    "Stone Sword":False, 
    "Iron Sword":False, 
    "Diamond Sword":False,
}

descendcount = 0
findtimer = 3

class Methods():
 def __init__(self, choice):
    self._weapon = player_weapon
    self._pickaxe = player_pickaxe
    self._action = choice
 
 def __str__(self):
   ...

 def craft_item(self, item):
   global inventory, player_weapon
   item = item.lower()
   matched_item = None
   for recipe_name in recipes:
        if recipe_name.lower() == item:
            matched_item = recipe_name
            break
   if not matched_item:
      print("What are you trying to craft?")
      return
   required = recipes[matched_item]
   for res, qty in required.items():
      if inventory.get(res, 0) < qty:
         print(f"Not enough {res} to craft {matched_item}.")
         return
   for res, qty in required.items():
      inventory[res] -= qty

   inventory[matched_item] = inventory.get(matched_item, 0) + 1
   print(f"You crafted a/an {matched_item}!")
   return matched_item
    
 def upgrade_weapon(new_weapon):
     global player_weapon, player_damage
     current_rank = weapons.get(player_weapon, 0)
     new_rank = weapons.get(new_weapon, 0)
     if new_rank > current_rank:
      player_weapon = new_weapon
      print(f"Your current weapon now is {new_weapon}")
      player_damage = weapon_dmg.get(player_weapon, 0)

     else:
      print("You already have a better weapon than this...")

 def upgrade_pick(new_pickaxe):
     global player_pickaxe
     current_rank = pickaxes.get(player_pickaxe, 0)
     new_rank = pickaxes.get(new_pickaxe, 0)
     if new_rank > current_rank:
      player_pickaxe = new_pickaxe
      print(f"Your current pickaxe now is {new_pickaxe}")
     else:
      print("You already have a better pickaxe than this...")

 def wood(self):
    resource1 = random.randint(2,5)
    print("Mining wood...")
    time.sleep(0.7)
    print(f"You got {resource1} wood!")
    inventory["Wood"] = inventory["Wood"] + resource1

 def stone(self):
    resource2 = random.randint(4,10)
    resource7roll = random.randint(5,10)
    print("Mining stone...")
    time.sleep(0.7)
    print(f"You got {resource2} cobblestones!")
    inventory["Cobblestone"] = inventory["Cobblestone"] + resource2
    time.sleep(1)
    if resource7roll == 1:
       resource7 = random.randint(1,2)
       print(f"You also got {resource7} coal!")
       inventory["Coal"] = inventory["Coal"] + resource7


 def stick(self):
    if inventory.get("Wood", 0) >=1:
        inventory["Wood"] -= 1
        inventory["Stick"] = inventory.get("Stick", 0) + 4
        print("You crafted 4 Sticks!")
    else:
        print("You don't have wood...")

 def actions_based_on_location(self, choice):
    if choice in ["desert", "ocean"]:
        return "Find", "Try to find a structure"
    elif choice in ["village", "shipwreck"]:
        return "Loot", "Loot the nearby structure"
    elif choice in ["cave", "ravine"]:
        return "Descend", "Go deeper in the caves, who knows what you'll find?"
    elif choice in ["forest", "plains"]:
        return "Hunt", "Try to find some animals"
    else:
        return "Unknown location.", "Invalid."

 def action(self, specifics1, specifics2):
    player_action = input(f"""What would you like to do?
 [ 
  * Mine    - You get a resource depending on the area
  * Explore - Choose another set of areas
  * Tools   - Check what tools you have currently
  * Craft   - Craft something from a recipe
  * Smelt   - Smelt the ores you got
  * {specifics1} - {specifics2}  
  * Quit    - Prematurely end the game                                          
 ] 
 > """).lower().strip()
    return player_action

 def sheep_hunt(self, sheep_hp, original_hp):
     print(f"Sheep HP: {sheep_hp}/{original_hp}")
     attack = input(f"""What do you want to do?,
     [ 
     * Attack - Attack the sheep, Your current weapon is {player_weapon}
     * Run    - Leave it for another day...
     ]
     > """).lower()
     if attack == "run":
          return "player_ran"
     if attack == "attack" and player_weapon == "Fists":
          print("You tried to attack the sheep with your fists!...")
          time.sleep(1)
          print("You missed... The sheep ran away...")
          return "fist_sheep"
     
     if attack == "attack": 
          while sheep_hp >= 0:
             sheep_hp -= player_damage 
             print(f"You dealt {player_damage} damage!")
             time.sleep(1)
             print(f"Sheep HP {max(sheep_hp, 0)}/{original_hp}")
             time.sleep(1)
             sheep_run = random.randint(1,8)
             
             if attack == "run":
                 return "player_ran"
                 

             if sheep_hp <= 0:
                resource4 = random.randint(1,2)
                print(f"You found {resource4} Wool!")
                inventory["Wool"] = inventory["Wool"] + resource4
                return "Slain"
             
             attack = input(f"""The sheep is attempting to run away..,
              [ 
               * Attack - Attack the sheep, Your current weapon is {player_weapon}
               * Run    - Leave it for another day...
              ]
              > """).lower()

             if sheep_run == 1:
                 print("The sheep ran away...")
                 return "Ran"
                            

 def looting(self, structure):
   print(f"You're looting the {structure}...")
   time.sleep(1)
   resource5 = random.randint(2,4)
   print(f"You found {resource5} iron!")
   time.sleep(1)
   inventory["Iron"] = inventory["Iron"] + resource5
   if structure == "Blacksmith":
      resource6 = random.randint(1,10)
      if resource6 == 7:
         print("Oh? Theres something else inside...")
         time.sleep(1)
         print("A lucky find! You found a Diamond!")
      else:
         print("Oh? Theres something else inside...")
         time.sleep(1)
         print("Nevermind, It was just trash...")

 def descend(self):
   global descendcount, ores, inventory
   if inventory.get("Torches", 0) < 1:
      print("It's too dark too see anything...")
      time.sleep(1)
      print("You can't pass through")
   else:
      while inventory.get("Torches") >=1 :
         inventory["Torches"] -= 1
         print(f"Descending into the caves... (Times descended: {descendcount}.) Remaining Torches:",inventory["Torches"])
         descendcount += 1
         if 3 <= descendcount <= 5:
            ironchance = random.randint(1,2)
            if ironchance == 1 and (player_pickaxe == "Stone Pickaxe" or player_pickaxe == "Iron Pickaxe"):
               print("You found Iron!")
               time.sleep(1)
               ironcount = random.randint(2,5)
               print(f"You got {ironcount} iron ore!")
               time.sleep(1)
               ores["Iron Ore"] = ores.get("Iron Ore", 0) + ironcount
            elif ironchance == 1 and (player_pickaxe == "Fists" or player_pickaxe == "Wooden Pickaxe"):
               print("You found Iron! But you failed to mine it...")
            else:
               pass
         else:
            pass      

         if descendcount >= 5:
            goldchance = random.randint(1,2)
            if goldchance == 1 and (player_pickaxe == "Stone Pickaxe" or player_pickaxe == "Iron Pickaxe"):
               print("You found Gold!")
               time.sleep(1)
               goldcount = random.randint(2,5)
               print(f"You got {goldcount} gold ore!")
               time.sleep(1)
               ores["Gold Ore"] = ores.get("Gold Ore", 0) + goldcount
            elif goldchance == 1 and (player_pickaxe == "Fists" or player_pickaxe == "Wooden Pickaxe"):
               print("You found Gold! But you failed to mine it...")
            else:
               pass
         else:
            pass 
         
         if descendcount >= 10:
            diachance = random.randint(1,3)
            if diachance == 1 and player_pickaxe == "Iron Pickaxe":
               print("You found Diamonds!")
               time.sleep(1)
               diacount = random.randint(1,4)
               print(f"You got {diacount} diamond/s!")
               time.sleep(1)
               inventory["Diamond"] = inventory.get("Diamond", 0) + diacount
            elif diachance == 1 and (player_pickaxe == "Fists" or player_pickaxe == "Wooden Pickaxe" or player_pickaxe == "Stone Pickaxe"):
               print("You found Diamonds! But you failed to mine it...")
            else:
               pass
         else:
            pass 
         print("""What would you like to do?
         [ 
           * Descend - Descend even further for better ores
           * Leave - Leave the caves
          ]     
         """)
         descend_choice = input("What would you like to do?: ").lower()
         if descend_choice == "leave":
            print("You went back up the caves.")
            print(f"Your current ores are: Iron Ore - {ores.get('Iron Ore', 0)}, Gold Ore - {ores.get('Gold Ore', 0)}")
            descendcount = 0
            break
         if descend_choice == "descend":
            pass
         else:
            print("Invalid response!")

 def smelting(self, ore, ingot):
   global inventory, ores
   print(ores)
   print(f"Remaining coal:",inventory.get("Coal", 0))
   print(f"You have {ores.get(ore, 0)} {ore}")
   try:
       howmanysmelt = int(input("How many are you going to smelt?: "))
   except ValueError:
        print("Invalid number!")
        return
   while howmanysmelt > ores.get(ore, 0) or howmanysmelt > inventory.get("Coal", 0):
        print("You're trying to smelt more than you have!")
        try:
            howmanysmelt = int(input("How many are you going to smelt?: "))
        except ValueError:
            print("Invalid number!")
            return
   ores[ore] -= howmanysmelt
   inventory["Coal"] -= howmanysmelt
   inventory[ingot] = inventory.get(ingot, 0) + howmanysmelt
   print(f"You smelted {howmanysmelt} {ore} into {ingot}!")

 def find(self):
   global inventory, findtimer
   print("You are now in the middle of the desert."
   "You might find a structure if you keep going.")
   time.sleep(1)       
   
   while findtimer > 0:
      print("""What would you like to do?
         [ 
           * Explore - Try to keep finding a structure
           * Leave - Leave it be
          ]     
         """)
      findchoice = input("Your choice?:" ).lower()
      if findchoice == "leave":
            print("You decided to stop trying to find it.")
            findtimer = 3
            break
      
      elif findchoice == "explore":
       findtimer -= 1
       findchance = random.randint(1,5)
       if findchance == 1:
         survivechance = random.randint(1,4)
         print("You actually found the desert pyramid!")
         print(f"You're looting the pyramid...")
         if survivechance == 1:
            print("You fell into the trap!")
            time.sleep(1)
            print("You got out alive but all the loot is gone...")
            break
         
         else:   
          time.sleep(1)
          resource5 = random.randint(5,8)
          print(f"You found {resource5} iron!")
          time.sleep(1)
          inventory["Iron"] = inventory["Iron"] + resource5
          print("You stopped exploring as you found the pyramid...")
          break
       else:
          print("You didn't find anything yet...")
      else:
         print("invalid choice")   
   if findtimer == 0:
        print("You got tired of exploring and went back.")
        findtimer = 3
   

pois = ["Forest", "Forest", "Forest", "Forest", "Forest","Forest", "Forest",
        "Plains", "Plains", "Plains", "Plains", "Plains","Plains", "Plains",
        "Cave", "Cave", "Cave", "Cave", "Cave",
        "Village", 
        "Desert", "Desert",
        "Shipwreck", 
        "Ravine", "Ravine"]

def main():
 
 print("Welcome to my game! The current objective to win is to get a Diamond Pickaxe and Diamond Sword!")
 time.sleep(0.5)
 print("Goodluck!")
 time.sleep(1)
 print("You just spawned in a minecraft world, you see a/an...")
 time.sleep(1)
 poiss = random.sample(list(set(pois)), 3)
 print(poiss)
 poiss_lower = [p.lower() for p in poiss]
 choice = input("Where would you like to go?: ").lower()
 while choice not in poiss_lower:
    print("You don't see that anywhere...")
    print(poiss)
    choice = input("Where would you like to go?: ").lower()
 methods = Methods(choice)
 print(f"You chose {choice}")
 time.sleep(1)
 print(f"You currently have {inventory}")
 time.sleep(1)


 while player_weapon != "Diamond Sword" and player_pickaxe != "Diamond Pickaxe": 
    spe1, spe2 = methods.actions_based_on_location(choice)
    player_action = methods.action(spe1, spe2)

    if player_action == "quit":
     break

    if player_action == "explore":
      poiss = random.sample(list(set(pois)), 3)
      print(poiss)
      poiss_lower = [p.lower() for p in poiss]
      choice = input("Where would you like to go next?: ").lower()
      while choice not in poiss_lower:
         print("You don't see that anywhere...")
         print(poiss)
         choice = input("Where would you like to go next?: ").lower()
      for p in poiss:
        if p.lower() == choice:
          choice = p
          break 
      print(f"You chose {choice}")
      time.sleep(1)
      print(f"You currently have {inventory}")
      time.sleep(1)
      player_action = methods.actions_based_on_location(choice).lower() 
 
    if player_action == "mine" and choice == "desert":
     print("Nothing but sand...")
     player_action = methods.actions_based_on_location(choice)
    if player_action == "mine" and (choice == "forest" or choice == "plains"):
       methods.wood()
       player_action = methods.actions_based_on_location(choice)
    if player_action == "mine" and (choice == "village" or choice == "shipwreck"):
       methods.wood()
       player_action = methods.actions_based_on_location(choice)
    if player_action == "mine" and (choice == "cave" or choice =="ravine"):
       if player_pickaxe == "Fists":
          print("You don't even have a pickaxe...")
       else:
          methods.stone()
       player_action = methods.actions_based_on_location(choice)

    if player_action == "hunt":
       print("You found a sheep!")
       time.sleep(1)
       sheep_hp = random.randint(5,10)
       original_hp = sheep_hp 
       methods.sheep_hunt(sheep_hp, original_hp)
       player_action = methods.actions_based_on_location(choice)

    if player_action == "craft":
       print("""Here are the craftable items,
       [ 
       * Wooden Pickaxe: 3 Wood and 2 Sticks, Allows you to mine in ravines and caves      
       * Stone Pickaxe - 2 Sticks and 3 Cobblestone, Allows you to mine Iron
       * Iron Pickaxe - 2 Sticks and 3 Iron, Allows you to mine Diamond
       * Furnace - 8 Cobblestone, Allows you to last longer when finding structures (since u cooked food)
       * Bed - 3 Wood and 3 Wool
       * Sticks - 1 Wood
       * Torches - 1 Coal and 1 Stick
       * Wooden Sword - 1 stick and 2 Wood, Deals 1 damage 
       * Stone Sword - 1 stick and 2 Cobblestone, Deals 2 damage
       * Iron Sword - 1 stick and 2 Iron, Deals 4 damage                                        
        ] 
       """)
       time.sleep(1)
       print(f"You currently have {inventory}")
       crafting = input("What would you like to craft?: ").lower()
       if crafting == "sticks" or crafting == "stick":
          methods.stick()
       else:
          weap = methods.craft_item(crafting)
          if weap in weapons:
                  methods.upgrade_weapon(weap)
          if weap in pickaxes:
                  methods.upgrade_pick(weap)
       player_action = methods.actions_based_on_location(choice)
    
    if player_action == "loot":
         if choice in loot_check:
             if loot_check[choice]:
                print("You've already looted this area.")
                time.sleep(1)
                player_action = methods.actions_based_on_location(choice)
             else:
                methods.looting(choice)
                loot_check[choice] = True
                time.sleep(1)
                player_action = methods.actions_based_on_location(choice)
         else:
           print("There's nothing to loot here.")
           time.sleep(1)
           player_action = methods.actions_based_on_location(choice)

    if player_action == "descend":
       methods.descend()
       player_action = methods.actions_based_on_location(choice)

    if player_action == "givemetorches":
       inventory["Torches"] = inventory.get("Torches", 0) + 80
       player_action = methods.actions_based_on_location(choice)

    if player_action == "tools":
       print(f"Your current weapon is {player_weapon}")
       print(f"Your current pickaxe is {player_pickaxe}")
       time.sleep(1)
       player_action = methods.actions_based_on_location(choice)

    if player_action == "smelt":
       if inventory.get("Furnace", 0) == 0:  
          print("You don't have a Furnace...")
       elif inventory.get("Coal", 0) == 0:
          print("You don't have coal...")
       else:
          print(ores)
          whatsmelt = input("Which ore are you going to smelt?: ").lower()
          if whatsmelt == "iron" or whatsmelt == "iron ore":
            methods.smelting("Iron Ore", "Iron")
          elif whatsmelt == "gold" or whatsmelt == "gold ore":
            methods.smelting("Gold Ore", "Gold")
          else:
           print("lmao fk u tryna smelt?? ")
       player_action = methods.actions_based_on_location(choice)

    if player_action == "find":
       methods.find()
       player_action = methods.actions_based_on_location(choice)

    else:
       print("Invalid input, try again.")
       time.sleep(0.5)
       

if player_weapon == "Diamond Sword" and player_pickaxe == "Diamond Pickaxe":
   print("Thanks for playing")

else:
   print("thanks for playing!")

    
if __name__ == "__main__":
   main()