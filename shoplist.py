shoplist=['apple','mango','carrot','bannana']
print("I have ",len(shoplist), 'item to buy ')
print("These items are ==>")
for item in shoplist :
    print(item, ' ')
print('///////////////////////////////////////////////////////////')
print("I also have to buy rice .")
shoplist.append('rice')
print("My updated shopping list is ==>", shoplist)
print('//////////////////////////////////////////////////////////')
print("I WANT TO SORT MY LIST NOW !! ")
shoplist.sort()
print("sorted shopping list is ==>" , shoplist)
print('//////////////////////////////////////////////////////////')
#remove an element from the list with del(delete) 
print("The first item that i will buy is : ", shoplist[0])
old_item=shoplist[0]
del shoplist[0]
print("I bought the : " , old_item)
print("My new updated shopping list is ==> ",shoplist ,"\n")
