import sys

def transformStr(str):
    str = str.strip()
    if(len(str) > 5):
        str = str[:5] + "..."
    if(str[0].lower() == 'u'):
        str = str.upper()
    elif(str[0].lower() == 'l'):
        str = str.lower()
    print(str)

transformStr('Testing string') # 'Testi...' (довжина більше 5 символів)
transformStr('Lux') # 'lux' (Починается на L)
transformStr('up') # 'UP' (Починается на U)
transformStr('Luxery') # 'luxer...' (Починается на L + довжина більше 5 символів)
transformStr('party')