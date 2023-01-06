import random
num=0

while True:
    try:
        counting_a=int(input('부를 숫자의 개수를 입력하세요(1, 2, 3만 입력 가능) :'))
        if not 1<=counting_a<=3:
            raise Exception('1,2,3 중 하나를 입력하세요')
        # break
        counting_b=int(input('부를 숫자의 개수를 입력하세요(1, 2, 3만 입력 가능) :'))
        if not 1<=counting_b<=3:
            raise Exception('1,2,3 중 하나를 입력하세요')
        # break
    except ValueError:
        print('정수를 입력하세요')    
    except Exception as e:
        print(e)
    num+=counting_a
    counting_all=counting_a+counting_b
    while num<counting_all:
        num+=1
        print('playerB : ',num)
    break