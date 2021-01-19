try:
    age = int(input('Age: '))
    income = 10000000
    risk = income/age
    print(age)

except ZeroDivisionError:
    print('Age cannot be zero!')

except ValueError:
    print('Invalid value!')

#In this 'try' and 'except' it's all about the output result.
#A successful code returns the code value 0.
#ValueError is when a user enters invalid value when prompted.
#In such cases it will show code error 1. Telling that the appropriate value is not entered.
#But the whole program crashes because of the value error. Which is not warranted.
#To avoid this ang get a clean code value 0, we 'try' and 'except' as repurposing.
#When there is a wrong value entered afterwards it will not crash the code, but will show what we want it to.
#After 'try' is written code. After except the value is recognised in this case a ValueError.