"""animals = ['man', 'bear', 'pig']
print(animals[0])
print(animals[1])
print(animals[2])

animals = ['man', 'bear', 'pig']
print(animals[0])
animals[0] = 'cat'
print(animals[0])"""

"""animals = ['man', 'bear', 'pig']
animals.append('cow')
print(animals[-1])"""

"""animals = ['man', 'bear', 'pig']
animals.extend (['aaa','bbb'])
animals.extend(['cow', 'duck'])
print(animals)
more_animals = ['horse', 'dog']
more_animals= ['ccc', 'nnn']
animals.extend(more_animals)
print(animals) """

"""animals = ['man', 'bear', 'pig', 'cow', 'duck', 'horse']
some_animals = animals[0:1]
some= animals[:-3]
print('Some animals: {}'.format(some_animals))
print(some)"""

"""animals = ['man', 'bear', 'pig']
try:
  cat_index = animals.index('cat')
except:
  cat_index = 'No cats found.'
print(cat_index)
"""

"""a= [1 ,2 ,3,4 ,5 ,7 ]

i=3
while i< len(a):
   print(a[i])
   i= i+1 """

"""a= [134 ,28 ,35,4 ,56 ,7 ]
b= sorted(a)
c=[1111,2223,44444,5566]
print (a)
print(b)
print(" numbers  : {}".format(b))
a.sort()
print(a)
print( a+ c)"""


"""for n in range(4):
    print(n)

for number in range(1, 6):
    print(number)    

fruits = ["Ae", "Baa", "Or"]

for fruit in fruits:
    print(fruit)    

for number in range(2, 11, 3):
    print(number)    

name = "aki"

for letter in name:
    print(letter)    


total = 0
for number in range(1, 6):
    total = number+ total
print(total)

name = input("Enter your name: ")

for letter in name:
    print(letter)


number = int(input("number :"))

for i in range (-1, 8, 2):
   print (number / i)
"""

def alltasks():

    tasks=[]

    while True:

        task= input ("enter task : ")

        if task != "" :
            tasks.append(task)

        else :
            break
    return(tasks)



print(alltasks())



        
