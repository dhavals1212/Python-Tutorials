def greet_user(first_name, last_name):
    #In the above function, 'name' was added as a parameter.
    #Parameters are the placeholders. They execute according when the function calls them.
    #Multiple parameters can be written and seperated inside the function, with comma.

    print(f'Welcome {first_name}, heir of {last_name}!')
    print('Welcome aboard!')


print("Start")
greet_user('Dash', 'Asgard')
#Here 'Dash' argument was called in the use.
#If the argument is not called in the function it will call the error.
#Multiple arguments can be used in the calling of the function.

print("Finish")