#Defining and Declaring and array
arr =[10,20,30,40,50]
print(arr)

#Accessing Array Elements
print(arr[0])
print(arr[1])
print(arr[2])
print(arr[-1])
print(arr[-2])

#Menerapkan concepts append
brand = ["Cocacola", "Sprite", "Fanta", "Kopi Kenangan"]

#Finding the length of the array
num_brand = len(brand)
print(num_brand)

#Adding an element to an array using append()
brand.append("Leminerale")
print(brand)
new_num_brand = len(brand)
print(new_num_brand)

#Removing elements from an array
colors = ["violet", "blue", "yellow", "red", "green", "black", "indigo", "orange"]

print(colors)
del colors[4]
print(colors)

colors.remove("blue")
print(colors)

colors.pop(3)
print(colors)

#Modifying elements of an array using indexing
fruits = ["Banana", "Mango", "Apple", "Guava", "Cherry", "Papaya"]
print(fruits)

fruits[1] = "Melon"
print(fruits)

fruits[-1] = "Watermelon"
print(fruits)

#Concatenating two arrays using the + operator
concat = [1, 2, 3]
concat = concat + [4, 5, 6]
print(concat)

#Repeating elements in an array
repeat = ["a"]
repeat = repeat * 5
print(repeat)


#Slicing an array
fruits2 = ["Apple", "Mango", "Cherry", "Blueberry", "Orange", "Watermelon", "Guava"]
print(fruits2[1:4])
print(fruits2[:3])
print(fruits2[-4:])
print(fruits2[-3:-1])

#Declaring and Defining multidimenional array
multd = [[1,2], [3,4], [5,6], [7,8]]
print(multd)
print(multd[0])
print(multd[3])
print(multd[2][1])
print(multd[3][0])
