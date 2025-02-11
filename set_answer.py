"""
This is the challenge file for Data structure - Set
Chloe Huang
July, 2021
"""



"""
Set: You are hosting a potluck in the end of the semester. You plan to prepare three dishes and write down the receipes. 
You are going to walmart and need to find out what do you need to buy.

Create a function to perform the union between 2 sets. 
Problem 1: Figure out what you need to buy at walmart
"""
def union_list(set1, set2):
    result = set(set1)
    for i in set2:
        if i not in result:
            result.add(i)
    
    final_list = list(result)
    return final_list





# Current have
mykitchen = {"oil", "salt", "sugar", "soy sause", "black paper", "honey", "rice"}
myfridge = {"egg", "milk", "yogurt", "blueberry", "ground beef", "mayo", "butter"}

# Receipe for potluck 
koreanBBQ = {"onion", "ribeye steak", "pear", "brown sugar", "sesame oil", "sesame seed"}
firedRice = {"butter", "egg", "carrot", "onion", "frozen peas", "garlic", "salt", "black pepper", "rice", "soy sauce", "sesame oil"}
blueberryIce = {"blueberry", "heavy whipping cream", "half-and-half cream", "sugar", "vanilla extract"}



print("======Test 1 -  get the list of the items that you don't need to buy, CAN't USE BUILD IN UNION FUNCTION =======")
# Don't use union this
print(union_list(mykitchen, myfridge)) #Expect output- ['oil', 'mayo', 'honey', 'milk', 'soy sause', 'butter', 'black paper', 'egg', 'ground beef', 'sugar', 'yogurt', 'rice', 'salt', 'blueberry']



print("======Test 2 - get the shopping list use union =======")
# Union all the things you currently have 
current_all = mykitchen.union(myfridge)
#print(current_all)

shopping_list = koreanBBQ.union(firedRice, blueberryIce)
#print(shopping_list)

walmart_list = shopping_list - current_all
print(walmart_list)

# Expect output: 14 items - 'ribeye steak', 'vanilla extract', 'onion', 'pear', 'sesame seed', 'soy sauce', 'sesame oil', 'black pepper', 'garlic', 'brown sugar', 'carrot', 'frozen peas', 'half-and-half cream', 'heavy whipping cream'

