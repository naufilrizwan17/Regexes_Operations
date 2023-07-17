# First we import the module 're'
import re

sentence = "The sun has finally set down"
# '^' matches the start of the string
x = re.search("^The",sentence)
print(x)
y = re.search("^Y",sentence)
print(y)
# '+' matches one or more occurrence of the character in the string
z = re.search("f+",sentence)
print(z)
# '\A' matches the start of the string
a = re.search("\AThe",sentence)
print(a)
# '.' matches any character
b = re.search("s.*n",sentence)
print(b)
c = re.search("s.n",sentence)
print(c)
# '\' escapes the character after it
d = re.search("\Asun",sentence)
print(d)
$ '\d' means it matches any digit (0-9) 
e = re.search("\d",sentence)
print(e)
f = re.search("sun",sentence)
print(f)
g = re.search("f.y",sentence)
print(g)
h = re.search("f.n",sentence)
print(h)
i = re.search("f.n*",sentence)
print(i)
j = re.search("l+",sentence)
print(j)
k = re.search("T.n",sentence)
print(k)
l = re.search("T.sun*",sentence)
print(l)
# '?' matches zero or one occurrence of the character in the string
m = re.search("f?n",sentence)
print(m)
$ [a-z] is a character class which matches the lowercase letters
o = re.search("Can[a-z]", "Can you tell me what is wrong with my shadow")
print(o)
p = re.search("r[a-z]tailor", "The tailor was terrible")
print(p)

