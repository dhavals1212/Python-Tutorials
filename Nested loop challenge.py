numbers = [5,2,5,2,2]
for number in numbers:
    print('*'*number)

#NESTED LOOP METHOD

for star_count in numbers:
    output=''
    for count in range(star_count):
        output+='*'
    print(output)