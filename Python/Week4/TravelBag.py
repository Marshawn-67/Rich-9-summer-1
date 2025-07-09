packItem = ["sunscreen , headphones , music , socks,clothes,food,"]
bedroom = ["things in room"]
print ("PACK YOUR BAG")
print("Enter the index of an item you'd like to move from your room to you b")
print("Type 'done' when you are done packing./n")
print("Your Bedroom")
travelBag = []

for item in Bedroom:
 print(item)

 item = int (input("Item: "))

 while item != 100:
  travelBag.append(packItem[item])
  packItem.remove(packItem(item))
  print("\nyour Bedrooom")
  print(bedroom)
  print("\n your travel Bag")
  print(travelBag)
  item= int (input("Item Index"))

  



