'''list dipython'''

thislist =['jambu','nanas','rambutan']
print (thislist)
#outputnya : ['jambu','nanas','rambutan']
list1 = ["apple", "banana", "cherry"]
list2 = [1, 5, 7, 9, 3]
list3 = [True, False, False]
print(list1)

mylist = ['jambu','nanas','rambutan']
print(type(mylist))

thislist = ["apple", "banana", "cherry"]
print(thislist)
#outputnya ["apple", "banana", "cherry"]


#append()
thislist = ["apple", "banana", "cherry"]
thislist.append("orange")
print(thislist)
'''output :["apple", "banana", "cherry","orange"]'''

#insert()
thislist = ["apple", "banana", "cherry"]
thislist.insert(1, "orange")
print(thislist)
'''output:["apple","orange","banana", "cherry"]'''

#extend()
thislist = ["apple", "banana", "cherry"]
tropical = ["mango", "pineapple", "papaya"]
thislist.extend(tropical)
print(thislist)
'''output :["apple", "banana", "cherry","mango", "pineapple", "papaya"]'''

#remove
thislist = ["apple", "banana", "cherry"]
thislist.remove("banana")
print(thislist)
'''akan menhapus banana dalam list'''

#del
thislist = ["apple", "banana", "cherry"]
del thislist[0]
print(thislist)
'''akan menhpus indeks ke 0 yaitu apple'''

#pop()
thislist = ["apple", "banana", "cherry"]
thislist.pop()
print(thislist)
'''akan menghapus item terakhir dari list yaitu cherry'''

#loop di list mengunakan for
thislist = ["apple", "banana", "cherry"]
for x in thislist:
  print(x)

'''selain for juga bisa menggunakan range,len,dan while'''

#shot di list
thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort()
print(thislist)
'''selain () juga bisa mengunakan (reverse = True) dan (key = myfunc)'''



#tuple python
thistuple = ("apple", "banana", "cherry")
print(thistuple)

#mengakses tuple dengan indeks
thistuple = ("apple", "banana", "cherry")
print(thistuple[1])

#update tuple
x = ("apple", "banana", "cherry")
y = list(x)
y[1] = "kiwi"
x = tuple(y)

print(x)

#unpacking tuple
fruits = ("apple", "banana", "cherry")

(green, yellow, red) = fruits

print(green)
print(yellow)
print(red)

#loop tuple dengan for
thistuple = ("apple", "banana", "cherry")
for x in thistuple:
  print(x)

'''sets python'''
thisset = {"apple", "banana", "cherry"}
print(thisset)

#access items 
'''karna kita tidak bisa mengakses item melalui indek
kita bisa mengunkan loop for dan mengunakan kata kunci in
'''
thisset = {"apple", "banana", "cherry"}

for x in thisset:
  print(x)

#add items
'''bisa mengunakan add()
sedikit catatan kita bisa mengunakan update() untuk menabahkan 
item dari sets
'''
thisset = {"apple", "banana", "cherry"}

thisset.add("orange")

print(thisset)

#remove sets
'''di sets remove tidak jauh berbeda dengan yang ada di list '''

#loop sets 
'''sama juga di loop pengulangan di sets juga bisa mengunakan for'''

#join sets
'''mengabungkan semua item dari kedua sets'''
  #union()
set1 = {"a", "b", "c"}
set2 = {1, 2, 3}
  
set3 = set1.union(set2)
print(set3)
  #update()
set1 = {"a", "b" , "c"}
set2 = {1, 2, 3}

set1.update(set2)
print(set1)
  
'''python dictionaries'''
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

#access
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
x = thisdict["model"]

#change
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict["year"] = 2018

#add distionary
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict["color"] = "red"
print(thisdict)

#remove
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.pop("model")
print(thisdict)

#loop
for x in thisdict:
  print(x)
  
#copy
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
mydict = thisdict.copy()
print(mydict)

#nested
myfamily = {
  "child1" : {
    "name" : "Emil",
    "year" : 2004
  },
  "child2" : {
    "name" : "Tobias",
    "year" : 2007
  },
  "child3" : {
    "name" : "Linus",
    "year" : 2011
  }
}

