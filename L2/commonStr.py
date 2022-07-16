def commonStr(str1, str2):
    charList = []
    while(len(str1) > 0): #якщо строка має символів більше за нуль
        i=0
        while(i<len(str2)): #індекс строки менше довжини строки
            if(str1[0] == str2[i]):
                charList.append(str1[0]) #символ, що співпадає з першою та другою строкою додати до масиву
                str2 = str2.replace(str2[i],'') #замінити цей символ на пусте значення
            else:
                i=i+1 #якщо символ не існує в другій строчці, то збільшити індекс на 1
        if(len(str2) == 0): #якщо друга має нуль символів, то вийти з циклу
             break
        str1 = str1.replace(str1[0],'') #замінити символ першої строки на пусте значення
    return ' '.join(charList)

print(commonStr('loli', 'luck'))
print(commonStr('good day', 'good morning'))
print(commonStr('moloko', 'okorok'))
print(commonStr('ua', 'facebook'))
print(commonStr('facebook', 'ua'))
print(commonStr('makaka', 'melon'))