# LİST

x = ["Yusuf", "Ege", "Eren", "Apo"]

# List store multiple items.
# List items are ordered, changeable, and allow duplicate.
# list items are indexed, first item index is 0.

# I want to call Ege
print(x[1])
# I want to call Apo
print(x[3])

print(len(x)) # shows how many items in the list

# List items can be of any data type
list1 = ["Yusuf", "Ege", "Eren", "Apo"] # str
list2 = [4, 5, 6, 7, 8] # int
list3 = [True, False, False] # boolean

# list() constructor
list4 = list(("Yusuf", "Ege", "Eren", "Apo"))
print(list4)

# negative indexing
list1 = ["Yusuf", "Ege", "Eren", "Apo"]
print(list1[-1])

list5 = ["Yusuf", "Ege", "Eren", "Apo","Mete","Omer"]
print(list5[2:5])
# the search will start at index 2 (included), and end at index 5 (excluded)
# index start with 0

list5 = ["Yusuf", "Ege", "Eren", "Apo","Mete","Omer"]
if "Ömer" in list5:
    print("yes, 'Omer is in the list")

################
# Python Collection (Arrays)
###############
# There are four collection data type
# List is collection which is ordered and changeable. Allow duplicates
# Tuple is collection which is ordered and unchangeable. Allow duplicates

# Changing datas
list6 = ["Yusuf", "Ege", "Eren", "Apo","Mete","Omer"]
list6[0] = "Rana"
print(list6)

# example
list6 = ["Yusuf", "Ege", "Eren", "Apo","Mete","Omer"]
list6[1:2] = ["Mustafa", "Kuzey"]
print(list6)

list6 = ["Yusuf", "Ege", "Eren", "Apo","Mete","Omer"]
list6[1:4] = ["Abdurahman"]
print(list6)

# insert() method
list7 = ["Yusuf", "Ege", "Eren", "Apo","Mete","Omer"]
list7.insert(2, "Abdurahman")
print(list7)

list7 = ["Yusuf", "Ege", "Eren", "Apo","Mete","Omer"]
list7.insert(3, "Melike Rana")
print(list7)

list7 = ["Yusuf", "Ege", "Eren", "Apo","Mete","Omer", "Melike Rana"]
print(list7)

list8 = ["Yusuf", "Ege", "Eren", "Apo","Mete","Omer"]
list9 = ["Melon", "Avocado"]
list8.extend(list9)
print(list8)

list8 = ["Kemal", "Ömer", "Ozan", "Ege","Mete","Eren"]
tuple = ("Melon", "Avocado")
list8.extend(tuple)
print(list8)

list7 = ["Yusuf", "Ege", "Eren", "Apo","Mete","Omer"]
list7.remove("Yusuf")
print(list7)