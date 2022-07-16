def sumNum(num):
    if(num > 0):
        sumList = []
        while(num > 10): #якщо отримане число більше за 10, тобто більше одного розряду
            dopNum = num
            while(dopNum > 10):
                countDigit = 1  
                while(dopNum > 10 ** countDigit):
                    countDigit = countDigit + 1 #кількість розрядів у числі
                k = dopNum // (10 ** (countDigit - 1)) #отримати перший розряд
                sumList.append(k) #додати значення розряду до списку
                dopNum = dopNum % (10 ** (countDigit - 1)) #отримати залишок
                if(dopNum < 10): #якщо залишок менший за нуль, додати його до списку
                    sumList.append(dopNum) 
            num = 0
            #порахувати суму списку
            for i in sumList:
                num = num + i
            sumList.clear()
        return num
    else:
        return "Введіть, будь ласка, додатнє число"
    
print(sumNum(38))
print(sumNum(40))
print(sumNum(48))
print(sumNum(2))
print(sumNum(3000007826732)) 
print(sumNum(-6)) 