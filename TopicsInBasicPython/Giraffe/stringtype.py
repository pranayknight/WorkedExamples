s="You are awesome. "    #just a normal string in double quotes can also be in single quotes
print(s)

s1="""You are
the creator
of your
own destiny"""      #to create multiline string in python we use three double quotes or three single quotes
print(s1)

print(s1[8])         #accessing a particular index of a string starts from 0

print(s*2)         #* is used for repetition how many times the string has to be repeated

print(len(s1))     #this len() function gives the length of the object or the no. of items in a container
print(len(s))

print(s1[0:5])     #it's called slicing where we provide starting and end index to get the values within that index
                                # also it doesn't take in the value of the ending index provided
print(s[0:])      #if we don't provide the end value it will give all data from the begining index mentioned
print(s[:8])      # here it starts from start and ends upto the index specified
print(s[-3:-1])

print(s[0:8:2])    #here step function is introduced, it's default value is 1
print(s[::-1])     #we can use slicing alongwith step function to reverse a string
print(s[12::-1])


print(s.strip())   #strip() function removes any spaces that's there at the beginning and the end of the string
print(s.lstrip())  #removes spaces from the left side
print(s.rstrip())  #removes the right hand spaces
# If we just type s. and press ctrl+space it will show all the function that we can use with that

print(s.find("awe"))  # to show the index of the thing mentioned
print(s.find("awe",0,len(s)))  #just to show we can specify the index within which it's commanded to look into
print(s.count("a"))  #it is used to find the no. of occurences of the things specified

print(s.replace("awesome","super"))

print(s.upper())    #prints in uppercase
print(s.lower())    #prints in lowercase
print(s.title())    #prints in title case means every word will start with uppercase
