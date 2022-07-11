## Method of List###

# remove()

clean_cities=["Indore","Surat","Vijaywada","Navi Mumbai","Pune","Raipur","Bhopal","Vadodara"]

print(type(clean_cities))
print(len(clean_cities))

clean_cities.remove("Pune")
print(len(clean_cities))

#################################################
#  pop()
#################################################

clean_cities.pop(0)
print(clean_cities)

clean_cities.pop(2)
print(clean_cities)

print("******************Using negative indexing****************")

print(clean_cities)

# ['Surat', 'Vijaywada', 'Raipur', 'Bhopal', 'Vadodara']
#################################################
#  clear()
#################################################


clean_cities.clear()# empty list
print(clean_cities)

#################################################
#  del()
#################################################

del clean_cities
#print(clean_cities) # 'clean_cities' is not defined

#  sort()

list1=[2,4,3,5,6,6,7,8,9,7]
list1.sort()
print(list1)#[2, 3, 4, 5, 6, 6, 7, 7, 8, 9]

list1.sort(reverse=True)#Descending order
print(list1)# [9, 8, 7, 7, 6, 6, 5, 4, 3, 2]

list1.sort(reverse=False)
print(list1)#[2, 3, 4, 5, 6, 6, 7, 7, 8, 9]

list_alpha= ["w","f","r","t","d","v","F"]

list_alpha.sort()
print(list_alpha)

list_alpha.sort(reverse=True) # in reverse order
print(list_alpha)

list_alpha.sort(key=str.lower) #not case sensitive
print(list_alpha)


#  nested list

list1 = [ [56, 98],[1,3] , [5,4] ,[5,24]]
list1.sort()
print(list1)#[[1, 3], [5, 4], [5, 24], [56, 98]]

list_num1 = [["z,x"],["p,d"],["s,r"],["t,w"]]
list_num1.sort()
print(list_num1)#[['p,d'], ['s,r'], ['t,w'], ['z,x']]


print("#*****************HOMEWORK*********************************#")

#################################################
# HW
#################################################
# 👇 SHARE THE  OUTPUT SCREEN SHOT 

# remove 34 from the list  using remove 
list5  = [1,4,5,66,34,21]
list5.remove(34)
print(list5)
# remove 2nd element from the list  using  pop() 
list6  = [1,4,5,66,34,21]
list6.pop(2)
print(list6)
# remove the last  element from the list  using  pop() 
list7  = [1,4,5,66,34,21,65,67,]
list7.pop(7)
print(list7)
# clean the list using clear()
list7  = [1,4,5,66,34,21,65,67,]
list7.clear()
print(list7)
# sort below list in ascending order
list_alpha1 =["p","d","s","r","t","w"]
list_alpha1.sort()
print(list_alpha1)
# sort below list in descending oreder
list_alpha4 =["p","d","s","r","t","w"]
list_alpha4.sort(reverse=True)
print(list_alpha4)
# sort below list in ascending order ingnoring case
list_alpha3 =["p","d","S","T","t","w"]


# sort below list in descending/reverse order using sort()
list2 = [ [34,56, 98],[112,34] , [12,12] ,[124,254]]


# sort below list in ascending order using sort()
list_alpha1 = [["z,x"],["p,d"],["s,r"],["t,w"]]

# sort below list in ascending order using sort()
list3 = [ [5,4] ,[5,24] ,["a","d"]]