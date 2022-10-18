import random
import ingredients as ingredients

loop = 8
repeat = 1
selection = []
selectionCost = []


def MealGeneratorInput(shoppingCart, shoppingCartCost):
  print("Is there any ingredients you would like to specifically have in your random meal? Your options are: \n Salt \n Pepper \n Milk \n Box of Spaghetti \n Marinara Sauce \n Ground Beef \n Lettuce \n Tomatoes \n Cucumbers \n Onions \n Carrots \n Cheese \n Steak \n Butter \n Garlic \n Asparagus \n Olive Oil \n Potatoes \n Sour Cream \n Chicken \n Eggs \n Flour \n Vegtable Oil \n Salmon \n Lemon\n Or type end to finish your selection\n")

  while(repeat == 1):
    MealIngredientChoice = input("Please enter here the ingredient you want: ")

    if(MealIngredientChoice in ingredients.ingredientName):
      ingredientIndex = ingredients.ingredientName.index(MealIngredientChoice)  
      selection.append(ingredients.ingredientName[ingredientIndex])
      selectionCost.append(ingredients.ingredientCost[ingredientIndex])

    if(MealIngredientChoice == "end"):
      MealGenerator(shoppingCart, shoppingCartCost, selection, selectionCost)
      return

def MealGenerator(shoppingCart, shoppingCartCost, selection, selectionCost):
  fact = 1
  while(fact == 1):
    randomMeal = []
    randomMealCost = []
    
    loop = 8 - len(selection)

    selectionCostTotal = sum(selectionCost)

    if(len(selection) >= 1):
      randomMeal.append(selection)
      randomMealCost.append(selectionCostTotal)

    while(loop > 0):
      randomIngredient = random.randint(0, len(ingredients.ingredientName)-1)
      if ingredients.ingredientName[randomIngredient] not in randomMeal:
        randomMeal.append(ingredients.ingredientName[randomIngredient])
        randomMealCost.append(ingredients.ingredientCost[randomIngredient])
        loop -= 1

    randomMealCostTotal = sum(randomMealCost)

    while(loop == 0):
      choice = int(input("\nYour selected ingredients are %s and that comes out to a total of %d dollars.\n Is this satisfactory or would you like to go again? \n 1. Go again \n 2. Exit\n\n" % (randomMeal, randomMealCostTotal)))

      if(choice == 1):
          loop = 8 - len(selection)

      if(choice == 2):
          shoppingCart.append(randomMeal)
          shoppingCartCost.append(randomMealCostTotal)
          return

  