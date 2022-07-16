def oddOrEven(num):
    if (num > 0):
        if(num % 2 == 0):
            print(f'Число {num} є парним')
        else:
            print(f'Число {num} є непарним')
    else:
        print('Число має бути більше за 0')
oddOrEven(1) 
oddOrEven(20) 
oddOrEven(-20) 