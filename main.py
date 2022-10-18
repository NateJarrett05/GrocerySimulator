import ingredients as ingredients
import meals as meals
import MealGenerator as MealMaker

loop = 1

shoppingCart = []
shoppingCartCost = []

print("Welcome to your own virtual grocery store. You can purchase whole meals with all the ingredients, the ingredients themselves, or you can go for a challenge and get random ingredients use it to make a meal.")

while(loop == 1):
  intro = int(input("\nWhat would you lke to do? \n 1. Ingredients \n 2. Meals \n 3. Meal Generator\n\n"))

  if(intro == 1):
    ingredients.ingredientChoice(shoppingCart, shoppingCartCost)

  if(intro == 2):
    meals.mealChoice(shoppingCartCost, shoppingCart)

  if(intro == 3):
    option = int(input("Select an option:\n 1. For completely random meal\n 2. For select ingredients you want included in your random meal\n\n"))
    
    if(option == 1):
      MealMaker.MealGenerator(shoppingCart, shoppingCartCost, MealMaker.selection, MealMaker.selectionCost)

    if(option == 2):
      MealMaker.MealGeneratorInput(shoppingCart, shoppingCartCost)

  choice = int(input("\nIs there anything else you would like to purchase today? 1.Yes 2.No"))

  if(choice == 2):
    loop = 0
    if(len(shoppingCart) > 1):
      total = sum(shoppingCartCost)
      print("Your cart includes %s and comes out to a total of %d. Have a nice day!" % (shoppingCart, total))

    else:
      print("Your cart includes %s and comes out to a total of %s. Have a nice day!" % (shoppingCart, shoppingCartCost))
    