lst=[10,2,33,45,89,2]
                                    #we used it in list but it can be used with any sequence data type
result=filter(lambda x:x%2==0,lst)  #this filter function will use the lambda function against each element in the list
print(result) #itonly displays the location of the filtered value since it is jusrt a filter

print(list(result)) #we converted the filter to list form to print the values
