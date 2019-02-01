
#Display all of the contents of the list

list=["Apples", "Pears", "Oranges","Peaches"]

for i in range(len(list)):
    
    print(list[i])

print("display another list")
print(*list)

#Add another fruit end of the list and display it
print("\n")
print("add fruits to the end of list")
list.append("Grape")
print(list,"\n")

#Add another fruit to the first of the list and display it
a= "melon"
new_list= [a]+list
print(new_list)

#Add another fruit to the first of the list and display it

list_1=["Melon"]
new_list = list_1 + list
print(new_list,"\n")

#Add another fruit to the first of the list and display it

print("Add fruits begining of list ")
list.insert(0,"Melon")
print(list,"\n")

#Task-6

for i in range(len(list)):
    
    
    if(list[0]=="p"):
        print(list[0])
       
        
       



