while True:
    print('Would you like questions for: ')
    print('1: Converting Denary to Binary')
    print('2: Converting Binary to Denary')
    choice = input('Choose an option: ')
    if choice == '1':
        count = 1
        from random import randint
        while True:
            convertme = randint(1,256)
            print(f'Question {count}: What is {convertme} in binary?')
            correct = bin(convertme)
            asastring = str(correct)
            wozerob = asastring[2:]
            if len(wozerob) == 1:
                print('.')
            else:
                if len(wozerob) == 1:
                    wozerob = "0000000" + wozerob
                    print('.')
                elif len(wozerob) == 2:
                    wozerob = "000000" + wozerob
                    print('.')
                elif len(wozerob) == 3:
                    wozerob = "00000" + wozerob
                    print('.')
                elif len(wozerob) == 4:
                    wozerob = "0000" + wozerob
                    print('.')
                elif len(wozerob) == 5:
                    wozerob = "000" + wozerob
                    print('.')
                elif len(wozerob) == 6:
                    wozerob = "00" + wozerob
                    print('.')
                elif len(wozerob) == 7:
                    wozerob = "0" + wozerob
            while True:
                answer = input("Enter Answer: ")
                if answer == wozerob:
                    print('Well done, you\'re right!')
                    count +=1
                    break
                else:
                    print('Wrong, try again!')
    if choice == '2':
        count = 0
        from random import randint
        number = randint(1,256)
        asbin = bin(number)
        asastring = str(asbin)
        wozerob = asastring[2:]
        if len(wozerob) == 8:
            print('.')
        else:
            if len(wozerob) == 1:
                wozerob = "0000000" + wozerob
                print('.')
            elif len(wozerob) == 2:
                wozerob = "000000" + wozerob
                print('.')
            elif len(wozerob) == 3:
                wozerob = "00000" + wozerob
                print('.')
            elif len(wozerob) == 4:
                wozerob = "0000" + wozerob
                print('.')
            elif len(wozerob) == 5:
                wozerob = "000" + wozerob
                print('.')
            elif len(wozerob) == 6:
                wozerob = "00" + wozerob
                print('.')
            elif len(wozerob) == 7:
                wozerob = "0" + wozerob
            print(f'Question {count}: What is {asbin} in denary?')
            answer = input('Enter Answer: ')
            while True:
                if answer == str(number):
                    print('Correct!')
                    count += 1
                    break
                else:
                    print('Try again!')
    print('Invalid option, try again.\n')