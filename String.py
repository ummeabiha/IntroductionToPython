# STRING
# String Functions

s="Good Morning Everyone Today Is A Good Day"
p="   Weather Is Nice"
print(s)

# Index
for i in p:
   print(i,"\t",p.index(i))

# Split (print each word Separately)
# 1
print(s.split())

# 2
s="0123456789"
s.split()
print(s)
print (s[2:5])
print(s[7:9]) #OR  print(s[-3:-1])

# 3
p="This is very cold today"
print(p.split())
l1=["this","is","Karachi"]
print(" ".join(l1))
# !join is only applicable for strings!

# Strip (Remove Unnecessary Spaces)
print(p.strip())

# join (join splitted string)
print("".join(s))   #Only applicable for strings

# Count (No Of occurences of mentioned word)
print(s.count("Good"))

# Find (Check if the Mentioned word is in the str or not)
print(s.find("Good"))
print(s.find("Class"))  #If it not finds a word in string then it will give output as -1

# Replace
print(s.replace("Morning","Evening"))
print(s+" and"+p)

# Translate
s=str.maketrans("a,b,c,d,e,f","u,v,w,x,y,z")
print("fade".translate(s))

# Concatenation
x="Hello"
y="World"
print(x+""+y+"!")

#NAME STYLING
n=input("Enter Your Name")
print(n.upper()) #HI I AM ABIHA
print(n.lower()) #hi i am abiha
print(n.title()) #Hi I Am Abiha
print(n.capitalize()) #Hi i am abiha
print(n.casefold()) #hi i am abiha

# PRACTICE
# 1
# Print 4 Letter Word Only:
n=int(input("Enter the no of words you want to enter:"))
l=[]
for i in range(1,n+1):
    print("Enter Word",i,":")
    l.append(str(input()))
print(l)

for i in l:
    print(i)

print("")
for i in range(0,len(l)):
    if len(l[i])==4:
        print(l[i])

# replace
# 2
forecast=("Today will be a Sunny day").casefold()
print(forecast.count("day"))
weather=forecast.index("sunny")
print(weather)
m=forecast.replace("sunny","cloudy")
print(m)

# 3
#STRING IS PALINDROME OR NOT:
str=input("Enter any string:")
str=str.casefold()
#reversing the string:
rev=reversed(str)

if list(str)==list(rev):
    print("YES!,Your string is 'Palindrome' ")
else:
    print("Sorry!,Your string is not a Palindrome")

#4
# sep (SEPARATES THE 2 VARIABLES)
s="1234"
l=[1,2,3,4]
print(s,l,sep=";")

# Middle Element of word capital:
from math import ceil
def cap(word):
    words = word.split()
    data=""
    for i in words:
        length=len(i)
        y=ceil(length/2)
        data+=(i[0:y]+i[y].upper())+i[y+1:]+" "
    return data
phrase=input("Enter a phrase:")
print("The middle element capital is:",cap(phrase))


# Alternate letters capital
phrase='my name is abiha'
word=list(phrase)
letter=""
for i in range(len(word)):
    if i%2==0:
        letter+=word[i].upper()
    else:
        letter+=word[i].lower()

print(letter)


# Last Element of Word Capital:
def cap(word):
    words = word.split()
    for i in words:
        x = len(i)
        y = x - 1
        print(i[0:y]+i[y].upper(),end=" ")

phrase=input("Enter a phrase:")
cap(phrase)
