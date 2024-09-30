#word counter

s = input("Enter any sentence or paragraph: ")
#splitting the string
strlist = s.split()
#counting the numbers of word in string 
if (len(strlist)!=0):
   print("Total number of words are: ",len(strlist))
else:
   print("This is an empty string")

