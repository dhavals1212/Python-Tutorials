def greet_user(first_name, last_name):
    print(f'Welcome {first_name}, heir of {last_name}!')
    print('Welcome aboard!')


print("Start")
greet_user(last_name='Asgard', first_name='Dash')
#In here keyword arguments 'first_name' and 'last_name' is used to denote which is which.
#This way, even if the order if the order of the arguments is reversed, we get the same intended result.

print("Finish")