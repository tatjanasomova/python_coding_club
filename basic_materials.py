def some_random_function(some_name):
    a = some_name + ' is great!'
    return (a)

def some_more_difficult_function(name_one, name_two):
    a = name_one + ' says hello to ' + name_two
    return (a)

def a_very_complicated_function(name_three):
    a = name_three + str(2+3)
    return (a)

def i_cannot_believe_there_is_still_more(name_four, what_function):
    a = name_four + what_function
    return (a)

def yet_more_functions(name_five, name_six):
    a = name_five + ' says hi'
    b = name_six + ' says bye'
    c = name_five + ' says hello'
    return a, b

some_random_function('Tanya')
some_more_difficult_function('Riga', 'Auckland')
a_very_complicated_function('what is ')
i_cannot_believe_there_is_still_more(
    'did someone say ', some_random_function('Python'))

yet_more_functions('john', 'mary')[1]
yet_more_functions('john', 'mary')[0]
len(yet_more_functions('john', 'mary'))

