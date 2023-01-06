import random
num=0
# counting=int(input('부를 숫자의 개수를 입력하세요(1, 2, 3만 입력 가능) :'))

while True:
    try:
        counting=int(input('부를 숫자의 개수를 입력하세요(1, 2, 3만 입력 가능) :'))
        if not 1<=counting<=3:
            raise Exception
        break
    except ValueError:
        print('정수를 입력하세요')    
    except Exception as notrightnum:
        print('1,2,3 중 하나를 입력하세요')

while num<counting:
    num+=1
    print('playerA : ',format(num))