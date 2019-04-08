lst=[10,20,"Pranay",-10,30.5]     # list is defined within square brackets
print(lst)
print(lst[2])           #indexing
print(lst[3:5])    #slicing
print(lst*4)       #repetition
print(len(lst))    #getting length

lst.append(40)     #adds the element to the end of the list
lst.remove("Pranay")    #removes the element specicified within the parentheses
del(lst[1])
print(lst)

#lst.clear()       #this will clear the list of the lst
#print(lst)

print(max(lst))     #prints the maximum value in the list
print(min(lst))     #prints the minimum value in the list

lst.insert(3,99)    #inserts the value in the specified index
print(lst)

lst.sort()         #sorts in an orderly fashion
print(lst)

lst.sort(reverse=True)
print(lst)
