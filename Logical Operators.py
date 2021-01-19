high_income = True
good_credit = False
criminal_record = True

if high_income and good_credit and not criminal_record:
    #Here 'and' operator gives a condition that two conditions altogether have to be true.
    #Only then and then it will be executed.
    #'not' operator defines if the variable in condition should not have something.
    #In not if it is True, it will not be executed, if False, it will be executed.

    print("Your loan application can be approved. Give us your documents for processing.")
elif high_income or good_credit:
    #In here or statement is ok with either one or another.
    #If either of the conditions satisfy, this will get executed.

    print("You might have to give extra down payment of the loan.")
    print("It's because your application has one of the two lesser.")
else:
    print("Apologies, but both are really low. Perhaps you'd like one of our policies?")