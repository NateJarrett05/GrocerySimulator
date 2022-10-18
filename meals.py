
def mealChoice(shoppingCartCost, shoppingCart):
  loop = 1

  Spaghetti = ["Box of Spaghatti","Marinara Sauce","Ground Beef","Pepper","Salt","Onions","Shredded Cheese"]
  SpaghettiCost = 14.25
  Salad = ["Lettuce","Tomatoes","Cucmbers","Onions","Carrots","Shredded Cheese"]
  SaladCost = 12.75
  Steak = ["Sirlion Steak","Stick of Butter","Cloves of Garlic","Asparagus","Olive Oil","Potatoes","Sour Cream"]
  SteakCost = 26.75
  FriedChicken = ["Chicken","Eggs","Flour","Vegtable Oil","Salt","Pepper"]
  FriedChickenCost = 16.5
  SearedFish = ["Fillet of Salmon","Lemon","Salt","Pepper","Olive Oil"]
  SearedFishCost = 19.0 
 
  while loop == 1:
    mealChoice = int(input("\nWhat meal would you like today? Our Options are:\n 1. Spaghetti \n 2. Salad \n 3. Steak \n 4. Fried Chicken\n 5. Seared Fish \n"))
    if(mealChoice == 1):
      shoppingCartCost.append(SpaghettiCost)
      shoppingCart.append(Spaghetti)

    if(mealChoice == 2):
      shoppingCartCost.append(SaladCost)
      shoppingCart.append(Salad)

    if(mealChoice == 3):
      shoppingCartCost.append(SteakCost)
      shoppingCart.append(Steak)

    if(mealChoice == 4):
      shoppingCartCost.append(FriedChickenCost)
      shoppingCart.append(FriedChicken)

    if(mealChoice == 5):
      shoppingCartCost.append(SearedFishCost)   
      shoppingCart.append(SearedFish) 

    if(mealChoice > 5):
      print("Please enter a valid meal number")

    confirmation = int(input("\nWould you like to add anything else? \n 1. Yes \n 2. No\n"))

    if(confirmation == 2):
      loop = 0

    if(mealChoice == "end"):
      loop = 0