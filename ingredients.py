
ingredientName = ["Salt", "Pepper","Milk","Box of Spaghatti","Marinara Sauce","Ground Beef","Lettuce","Tomatoes","Cucumbers","Onions","Carrots","Shredded Cheese","Sirlion Steak","Stick of Butter","Cloves of Garlic","Asparagus","Olive Oil","Potatoes","Sour Cream","Chicken","Eggs","Flour","Vegtable Oil","Fillet of Salmon","Lemon"]
ingredientCost = [1.0, 1.0, 3.5, 2.0, 2.0, 3.5, 2.0, 2.0, 2.0, 2.0, 2.0, 3, 7.0, 3.0, 2.0, 2.0, 5.0, 5.0, 2.75, 7.0, 2.75, 2.75, 2.0, 10.0, 2.0]

def ingredientChoice(shoppingCart, shoppingCartCost):
  print("\nWhich of the individual ingredients would you like to add to your shopping cart today? Your options are: \n Salt \n Pepper \n Milk \n Box of Spaghetti \n Marinara Sauce \n Ground Beef \n Lettuce \n Tomatoes \n Cucumbers \n Onions \n Carrots \n Cheese \n Steak \n Butter \n Garlic \n Asparagus \n Olive Oil \n Potatoes \n Sour Cream \n Chicken \n Eggs \n Flour \n Vegtable Oil \n Salmon \n Lemon\n Or type end to return back to the main option menu\n")

  loop = 1
  
  while(loop == 1): 
    ingredientChoice = input("Please input enter the name of the item you want.\n\n")

    if(ingredientChoice in ingredientName):
      ingredientIndex = ingredientName.index(ingredientChoice)  
      shoppingCart.append(ingredientName[ingredientIndex])
      shoppingCartCost.append(ingredientCost[ingredientIndex])

    if(ingredientChoice == "end"):
      loop = 0