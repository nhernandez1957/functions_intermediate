#Update Values in Dictionaries and Lists

x = [ [5,2,3], [10,8,9] ] 
x[1][0] = 15
print(x)


students = [
    {'first_name':  'Michael', 'last_name' : 'Jordan'},
    {'first_name' : 'John', 'last_name' : 'Rosales'}
]
students[0]['last_name'] = 'Bryant'
print(students)



sports_directory = {
    'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
    'soccer' : ['Messi', 'Ronaldo', 'Rooney']
}
sports_directory['soccer'][0] = 'Andres'
print(sports_directory['soccer'])

z = [ {'x': 10, 'y': 20} ]
z[0]['y'] = 30
print(z)



#part2

students = [
        {'first_name':  'Michael', 'last_name' : 'Jordan'},
        {'first_name' : 'John', 'last_name' : 'Rosales'},
        {'first_name' : 'Mark', 'last_name' : 'Guillen'},
        {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ]

def iterateDictionary(students):   
    for i in students:
        if 'first_name' in i:
            for a, b in i.items():
                print("{} - {}".format(a, b))


iterateDictionary(students)

print("==============================")
# should output: (it's okay if each key-value pair ends up on 2 separate lines;
# bonus to get them to appear exactly as below!)
# first_name - Michael, last_name - Jordan
# first_name - John, last_name - Rosales
# first_name - Mark, last_name - Guillen
# first_name - KB, last_name - Tonel

# part 3

def iterateDictionary2(key_name, some_list):
    for d in some_list:
        print(d[key_name])


iterateDictionary2('first_name', students)

print("==============================")

iterateDictionary2('last_name', students)

print("================================")

def printInfo(dojo):
    print(len(dojo['locations']), "LOCATIONS")
    for location in dojo['locations']:
        print(location)
    print(len(dojo['instructors']), "INSTRUCTORS")
    for location in dojo['instructors']:
        print(location)

dojo = {
    'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
    'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}
printInfo(dojo)