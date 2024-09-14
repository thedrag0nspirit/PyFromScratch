#This one will be about the string slicing
# as well as string methods
a = "!!harry!! !! HARRY"
print(len(a))
print (a.upper())
# strings are immutable 
print(a.lower())
print(a.rstrip("!"))
print(a.replace("harry","john"))

print(a.split (" "))

b= "deepanshu"
print (b.capitalize())#first char to upper and others in the lower case
str1="Welcome to the console !!!"
print(len(str1))
print(len(str1.center(50)))

#Count
c="Thakur","Thakur","Deepanshu","12345"
print(c.count("Thakur"))

#endswith()

str1="Welcome to the console !!!"
print(str1.endswith("!!!"))

print(str1.endswith("to",4,10))

#find
str1= "he's name is Dan. He is an honest man."
print(str1.find("is"))

#isprintable
