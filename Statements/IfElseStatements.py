# If, elif, else Statements.
# Control Flow - We often only want a certain code to execute when a particular condition has been met.
# Control Flow syntax makes use of colons and indentation. (whitespace)
# Indentation system is CRUCIAL to Python and is what sets it apart from other programming languages.

hungry = False

if hungry:
    print('Give me Food!')    
elif hungry == False:
    print('Its false')
elif hungry == 'Now':
    print('Im hungry now!')
else:
    print('Everything else')
