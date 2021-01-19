print(10+20)
#'+' will add the two numbers.
print(20-50)
#'-' will subtract the two numbers.
print(40*3)
#'*' will multiply the two numbers.
print(10/4)
#'/' will divide the first number by second and return the float value as result.
print(10//4)
#'//' will divide the first number by second and return the integer value a result.
print(10%3)
#Here, '%' also known as modulance operator will give the remainder value of the division operation.
print(10**3)
#'**' indicate the exponent operator which will give first number power to the second number as result.

x=10
x+=3
#Here '+=' means increment operator which means to increment value of variable x with 3 and store in x.

y=15
y-=5
#Now '-=' is decrement operator which will decrease the value of y and store in y.
print(x)
print(y)

z=16
z/=5
#'/=' is to first divide value of z with 5 and store it in z.
print(z)

k=30
k*=4
#'*=' will multiply 'k' variable with 4 and add store it in k.
print(k)

j=15
j//=4
#'//=' will divide j variable with 4 and return the integer value and store in j.
print(j)

m=5
m%=2
#'%=' will divide 5/2 and store the remainder in the m back.
print(m)

n=6
n**=2
#'**=' will just exponent 2 to 6, and resultant 36 will be stored in n.
print(n)

#OPERATOR PRECEDENCE

l = 5 * 3 - 4 ** 2 / 2 * 3 + 4
#First precedence is expoent '**' that will be operated first. so, 4**2 will become 16.
#Second precedence comes to division. Which will generate 16 / 2 will become 8.
#Third precedence is multiplication. Which will get 5*3 and 8*3.
#The operation is now, 15-24+4.
#Last are addition/subtraction. the value returned will be -5.0 since it's a float operation. ['/' not '//']
#Use of parenthesis means that operation covered by parenthesis will be done first.
print(l)