##day3
print("manoj")#variable declaration
name="Hello world"
print(name)
print(2+3)
print("2+3")
# Data Types in python are 14 types
# Numerical datatypes->  int float string boolean set listset tuple dictionary complex
# mutable and immutable datatypes and strings are immutable
# String Concatenation : adding two or more strings by using + symbol
a="Python"
b='Programming'
print(a+" "+b)
print("Python"+" "+"Programming")
# String Repetation : repeating the string required number of times by using *
c="PYTHON "
repeatedresult=c*4
print(repeatedresult)
# string Length : implies to find length of the string using len() built in function
d=len(c)
print(d)
# string Indexing : to find the position of the character in a string using [] brackets
e=c[0]
print(e)
f=c[1]
print(f)
g=c[2]
print(g)
h=c[3]
print(h)
i=c[4]
print(i)
j=c[5]
print(j)
k=c[6]
print(k)
# string Slicing
print("manoj") 


##day 4
name="Python"
name="Programming"
print(name)
# naming conventions->camel case notation(example:myName,firstName,elementId),pascal case notation(example:MyName,FirstName,ElementId) and snake case notation(example:_myname,_my_name,_first_name,first_name)
# comments->single line comments and multiline comments(can be done using """ """)
"""hello there this is a multiline comment"""
# DataTypes
'''1.fundamental datatype which are int,float,boolean,complex'''
'''2.sequential datatype are immutable which are string,byte,byte array,range'''
'''3.list datatype which is list'''
'''4.set datatype which are set,frozen set'''
'''5.dictionary datatype are'''
'''6.none datatype'''
# to display multiple lines in python
sentence='''1.fundamental datatype which are int,float,boolean,complex
2.sequential datatype are immutable which are string,byte,byte array,range
3.list datatype which is list
4.set datatype which are set,frozen set
5.dictionary datatype are
6.none datatype'''
print(sentence)
name="Rohith Reddy Gali"
age=34
print(f"I am {name} and i am {age} years old")
#we can access charecters in the string by using indexing,slicing,step index and negative index
a="Programming"
b=a[0]
print(b)
#string slicing
c=a[4:7]
print(c)
d=a[3:]
print(d)
e=a[:8]
print(e)
f=a[1:9:1]#step index example
print(f)
g=a[-5:-1]#negative index example
print(g)
f=a[::-1]#example to reverse the string with out using built in functions
print(f)
#some of the string methods
"""Capitalize(),uppercase(),lowercase(),replace(),check the string present or not """
g=a.capitalize()
print(g)
f=a.upper()
print(f)
g=a.lower()
print(g)
line="Hello World"
h=line.replace("World","Everyone")
print(h)
line1="Hello python programmers"
i="python" in line1
print(i)
j="python" not in line1
print(j)


n= int(input())
b= n>7
print(b)
print(n)