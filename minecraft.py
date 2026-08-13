import time
import random
import sys




#player_damage = weapon_dmg.get(player_weapon, 0)

descendcount = 0
findtimer = 3

class Player():
   def __init__(self):
      self.health = 20
      self.inventory = {"Wood": 0, 
                        "Sticks": 0, 
                        "Coal": 0, 
                        "Wool": 0, 
                        "Raw Meat": 0,
                        "Cooked Meat": 0,
                        "Leather": 0,
                        "Cobblestone": 0, 
                        "Iron": 0, 
                        "Gold": 0,
                        "Diamond": 0,
                          }
      self.tools = {
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
      self.weapon = "Fists"
      self.tool = "Fists"
     
      self.ores =  {"Iron Ore": 0, "Gold Ore": 0,}
      self.weaprank = {"Fists": 0, "Wooden Sword": 1, "Stone Sword": 2, "Iron Sword": 3, "Diamond Sword": 4,}
      self.pickrank = {"Fists": 0, "Wooden Pickaxe": 1, "Stone Pickaxe": 2, "Iron Pickaxe": 3, "Diamond Pickaxe": 5,} 
      self.weapdmg =  {"Fists": 1, "Wooden Sword": 2, "Stone Sword": 3, "Iron Sword": 4, "Diamond Sword": 5,}

      @property
      def dmg(self):
         return self.weapdmg.get(self.weap, 1)

      def upgrade_weapon(self, new_weapon):
           if self.weaprank.get(new_weapon, 0) > self.weaprank.get(self.weapon, 0):
            print(f"Your current weapon now is {new_weapon}")
            self.weapon = new_weapon
           else:
            print("You already have a better weapon than this...")

      def upgrade_pick(self, new_pickaxe):
        if self.pickrank.get(new_pickaxe, 0) > self.pickrank.get(self.tool, 0):
          print(f"Your current pickaxe now is {new_pickaxe}")
          self.tool = new_pickaxe
        else:
         print("You already have a better pickaxe than this...")
      
class Game():
 def __init__(self):
    self.player = Player()
    self.lootcheck = {"Village":False, "Shipwreck":False}
    self.descendcount = 0
    self.findtimer = 3
    self._daycount = 0
    self.recipes = {
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
    self.pois = ["Forest", "Forest", "Forest", "Forest", "Forest","Forest", "Forest",
        "Plains", "Plains", "Plains", "Plains", "Plains","Plains", "Plains",
        "Cave", "Cave", "Cave", "Cave", "Cave",
        "Village", 
        "Desert", "Desert",
        "Shipwreck", 
        "Ravine", "Ravine"]
    

 def craft_item(self, item):
   item = item.lower()
   matched_item = None
   for recipe_name in self.recipes:
        if recipe_name.lower() == item:
            matched_item = recipe_name
            break
   if not matched_item:
      print("What are you trying to craft?")
      return
   required = self.recipes[matched_item]
   for res, qty in required.items():
      if self.player.inventory.get(res, 0) < qty:
         print(f"Not enough {res} to craft {matched_item}.")
         return
   for res, qty in required.items():
      self.player.inventory[res] -= qty
      
   self.player.inventory[matched_item] = self.player.inventory.get(matched_item, 0) + 1
   print(f"You crafted a/an {matched_item}!")
   return matched_item
    

 def wood(self):
    resource1 = random.randint(2,5)
    self.player.inventory["Wood"] = self.player.inventory["Wood"] + resource1
    return resource1
    

 def stone(self):
    resource2 = random.randint(4,10)
    resource7roll = random.randint(5,10)
    print("Mining stone...")
    time.sleep(0.7)
    print(f"You got {resource2} cobblestones!")
    self.player.inventory["Cobblestone"] = self.player.inventory["Cobblestone"] + resource2
    time.sleep(1)
    if resource7roll == 1:
       resource7 = random.randint(1,2)
       print(f"You also got {resource7} coal!")
       self.player.inventory["Coal"] = self.player.inventory["Coal"] + resource7
       return

 def stick(self):
    if self.player.inventory.get("Wood", 0) >=1:
        self.player.inventory["Wood"] -= 1
        self.player.inventory["Stick"] = self.player.inventory.get("Stick", 0) + 4
        print("You crafted 4 Sticks!")
        time.sleep(1)
        return
    else:
        print("You don't have wood...")
        time.sleep(1)
        return
    
 def actions_based_on_location(self, loc):
    if loc in ["desert", "ocean"]:
        return "Find", "Try to find a structure"
    elif loc in ["village", "shipwreck"]:
        return "Loot", "Loot the nearby structure"
    elif loc in ["cave", "ravine"]:
        return "Descend", "Go deeper in the caves, who knows what you'll find?"
    elif loc in ["forest", "plains"]:
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
  * Smelt   - Smelt ores or cook food!
  * {specifics1} - {specifics2}  
  * Quit    - Prematurely end the game                                          
 ] 
 > """).lower().strip()
    return player_action

 def sheep_hunt(self, sheep_hp, original_hp):
     print(f"Sheep HP: {sheep_hp}/{original_hp}")
     attack = input(f"""What do you want to do?,
     [ 
     * Attack - Attack the sheep, Your current weapon is {self.player.weapon}
     * Run    - Leave it for another day...
     ]
     > """).lower()
     if attack == "run":
          return "player_ran"
     if attack == "attack" and self.player.weapon == "Fists":
          print("You tried to attack the sheep with your fists!...")
          time.sleep(1)
          print("You missed... The sheep ran away...")
          return "fist_sheep"
     
     if attack == "attack": 
          while sheep_hp >= 0:
             sheep_hp -= self.player.weapdmg 
             print(f"You dealt {self.player.weapdmg} damage!")
             time.sleep(1)
             print(f"Sheep HP {max(sheep_hp, 0)}/{original_hp}")
             time.sleep(1)
             sheep_run = random.randint(1,8)
             
             if attack == "run":
                 return "player_ran"
                 

             if sheep_hp <= 0:
                resource4 = random.randint(1,2)
                print(f"You found {resource4} Wool!")
                self.player.inventory["Wool"] = self.player.inventory["Wool"] + resource4
                return "Slain"
             
             attack = input(f"""The sheep is attempting to run away..,
              [ 
               * Attack - Attack the sheep, Your current weapon is {self.player.weapon}
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
   self.player.inventory["Iron"] = self.player.inventory["Iron"] + resource5
   if structure == "Shipwreck": 
      r = random.randint(3, 5)
      print(f"You also found {r} gold!")
      self.player.inventory["Gold"] = self.player.inventory["Gold"] + r
   if structure == "Village":
      resource6 = random.randint(1,10)
      print("Oh? Theres something else inside...")
      if resource6 == 7:
         print("Oh? Theres something else inside...")
         time.sleep(1)
         print("A lucky find! You found a Diamond!")
         return
      time.sleep(1)
      print("Nevermind, it was just trash...")
      return

 def descend(self):
   if self.player.inventory.get("Torches", 0) < 1:
      print("It's too dark too see anything...")
      time.sleep(1)
      print("You can't pass through...")
      return
   else:
      while self.player.inventory.get("Torches") >=1 :
         self.player.inventory["Torches"] -= 1
         print(f"Descending into the caves... (Times descended: {self.descendcount}.) Remaining Torches:",self.player.inventory["Torches"])
         self.descendcount += 1
         if 3 <= self.descendcount <= 5:
            ironchance = random.randint(1,2)
            if ironchance == 1 and (self.player.tool == "Stone Pickaxe" or self.player.tool == "Iron Pickaxe"):
               print("You found Iron!")
               time.sleep(1)
               ironcount = random.randint(2,5)
               print(f"You got {ironcount} iron ore!")
               time.sleep(1)
               self.player.ores["Iron Ore"] = self.player.ores.get("Iron Ore", 0) + ironcount
               return
            elif ironchance == 1 and (self.player.tool == "Fists" or self.player.tool == "Wooden Pickaxe"):
               print("You found Iron! But you failed to mine it...")
               return
            else:
               pass
         else:
            pass      

         if self.descendcount >= 5:
            goldchance = random.randint(1,2)
            if goldchance == 1 and (self.player.tool == "Stone Pickaxe" or self.player.tool == "Iron Pickaxe"):
               print("You found Gold!")
               time.sleep(1)
               goldcount = random.randint(2,5)
               print(f"You got {goldcount} gold ore!")
               time.sleep(1)
               self.player.ores["Gold Ore"] = self.player.ores.get("Gold Ore", 0) + goldcount
            elif goldchance == 1 and (self.player.tool == "Fists" or self.player.tool == "Wooden Pickaxe"):
               print("You found Gold! But you failed to mine it...")
            else:
               pass
         else:
            pass 
         
         if self.descendcount >= 10:
            diachance = random.randint(1,3)
            if diachance == 1 and self.player.tool == "Iron Pickaxe":
               print("You found Diamonds!")
               time.sleep(1)
               diacount = random.randint(1,4)
               print(f"You got {diacount} diamond/s!")
               time.sleep(1)
               inventory["Diamond"] = inventory.get("Diamond", 0) + diacount
            elif diachance == 1 and (self.player.tool != ["Iron Pickaxe", "Diamond Pickaxe"]):
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
            print(f"Your current ores are: Iron Ore - {self.player.ores.get('Iron Ore', 0)}, Gold Ore - {self.player.ores.get('Gold Ore', 0)}")
            self.descendcount = 0
            break
         if descend_choice == "descend":
            pass
         else:
            print("Invalid response!")

 def smelting(self, ore, ingot):
   print(self.player.ores)
   print(f"Remaining coal:",self.player.inventory.get("Coal", 0))
   print(f"You have {self.player.ores.get(ore, 0)} {ore}")
   try:
       howmanysmelt = int(input("How many are you going to smelt?: "))
   except ValueError:
        print("Invalid number!")
        return
   while howmanysmelt > self.player.ores.get(ore, 0) or howmanysmelt > self.player.inventory.get("Coal", 0):
        print("You're trying to smelt more than you have!")
        try:
            howmanysmelt = int(input("How many are you going to smelt?: "))
        except ValueError:
            print("Invalid number!")
            return
   self.player.ores[ore] -= howmanysmelt
   self.player.inventory["Coal"] -= howmanysmelt
   self.player.inventory[ingot] = self.player.inventory.get(ingot, 0) + howmanysmelt
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
   
 def main(self):
 
  print("Welcome to my game! The current objective to win is to get a Diamond Pickaxe and Diamond Sword!")
  time.sleep(0.5)
  print("Goodluck!")
  time.sleep(1)
  print("You just spawned in a minecraft world, you see a/an...")
  time.sleep(1)
  poiss = random.sample(list(set(self.pois)), 3)
  print(poiss)
  poiss_lower = [p.lower() for p in poiss]
  choice = input("Where would you like to go?: ").lower()
  while choice not in poiss_lower:
    print("You don't see that anywhere...")
    print(poiss)
    choice = input("Where would you like to go?: ").lower()
  print(f"You chose {choice}")
  time.sleep(1)
  print(f"You currently have {self.player.inventory}")
  time.sleep(1)


  while True:
    if self.player.weapon == "Diamond Sword" and self.player.weapon == "Diamond Pickaxe":
     print("You got a diamond sword and a diamond pickaxe! Congrats!")
     time.sleep(0.5)
     print("Thanks for playing!")
     break
    
    spe1, spe2 = self.actions_based_on_location(choice)
    player_action = self.action(spe1, spe2)

    if player_action == "quit":
     sys.exit("See you next time!")

    if player_action == "explore":
      poiss = random.sample(list(set(self.pois)), 3)
      print(poiss)
      poiss_lower = [p.lower() for p in poiss]
      choice = input("Where would you like to go next?: ").lower()
      while choice not in poiss_lower:
         print("You don't see that anywhere...")
         print(poiss)
         choice = input("Where would you like to go next?: ").lower()
      
      print(f"You chose {choice}")
      time.sleep(1)
      print(f"You currently have {self.player.inventory}")
      time.sleep(1)
      player_action = self.actions_based_on_location(choice)
 
    if player_action == "mine" and choice == "desert":
     print("Nothing but sand...")
     player_action = self.actions_based_on_location(choice)
    if player_action == "mine" and choice in ("forest", "plains", "village", "shipwreck"):
       print(f"You got {self.wood()} wood!")
       time.sleep(1)
       player_action = self.actions_based_on_location(choice)
   
    if player_action == "mine" and (choice == "cave" or choice =="ravine"):
       if self.player.tool == "Fists":
          print("You don't even have a pickaxe...")
       else:
          self.stone()
       player_action = self.actions_based_on_location(choice)

    if player_action == "hunt":
       print("You found a sheep!")
       time.sleep(1)
       sheep_hp = random.randint(5,10)
       original_hp = sheep_hp 
       self.sheep_hunt(sheep_hp, original_hp)
       player_action = self.actions_based_on_location(choice)

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
       print(f"You currently have {self.player.inventory}")
       crafting = input("What would you like to craft?: ").lower()
       if crafting == "sticks" or crafting == "stick":
          self.stick()
       else:
          weap = self.craft_item(crafting)
          if weap in self.player.weaprank:
                  self.player.upgrade_weapon(weap)
          if weap in self.player.pickrank:
                  self.player.upgrade_pick(weap)
       player_action = self.actions_based_on_location(choice)
    
    if player_action == "loot":
         choice = choice.capitalize().strip()
         if choice in self.lootcheck:
             if self.lootcheck[choice]:
                print("You've already looted this area.")
                time.sleep(1)
                player_action = self.actions_based_on_location(choice)
             else:
                self.looting(choice)
                self.lootcheck[choice] = True
                time.sleep(1)
                player_action = self.actions_based_on_location(choice)
         else:
           print("There's nothing to loot here.")
           time.sleep(1)
           player_action = self.actions_based_on_location(choice)

    if player_action == "descend":
       self.descend()
       player_action = self.actions_based_on_location(choice)

    if player_action == "givemetorches":
       inventory["Torches"] = inventory.get("Torches", 0) + 80
       player_action = self.actions_based_on_location(choice)

    if player_action == "tools":
       print(f"Your current weapon is {self.player.weapon}")
       print(f"Your current pickaxe is {self.player.tool}")
       time.sleep(1)
       player_action = self.actions_based_on_location(choice)

    if player_action == "smelt":  
        if self.player.inventory.get("Furnace", 0) == 0:  
          print("You don't have a Furnace...")
        elif self.player.inventory.get("Coal", 0) == 0:
          print("You don't have coal...")
        else:
          print(self.player.ores)
          whatsmelt = input("Which ore are you going to smelt?: ").lower()
          if whatsmelt == "iron" or whatsmelt == "iron ore":
            self.smelting("Iron Ore", "Iron")
          elif whatsmelt == "gold" or whatsmelt == "gold ore":
            self.smelting("Gold Ore", "Gold")
          else:
           print("lmao fk u tryna smelt?? ")
        player_action = self.actions_based_on_location(choice)


    if player_action == "find":
       self.find()
       player_action = self.actions_based_on_location(choice)

    

if __name__ == "__main__":
    game = Game()
    game.main()