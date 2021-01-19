names = ['Dash','Bash','Smash','Clash','Flash']
#Here the '[]' displays the lists. Lists can be characters, strings or numbers.
# Each entity is seperated by a comma.

print(names[0])
#This will print the first entity since the lists start from 0 onwards.
#'[]' in a list is called 'indexing'.

print(names[0:3])
#The use of ':' denotes range. Here all entities from 0 to 3 will be displayed.
#3rd entity will be excluded.

print(names[:2])
#Here '[:2]' dictates all entities from beginning upto 2nd, exluding second.

print(names[1:])
#Here '[1:]' dictates all entities from 1st entity to all entities afterwards.

print(names[:])
#In this, there will be all entities printed.

names[2] = 'Splash'
#This will replace the 2nd entity with the newer entity defined above.

print(names)