import random
num=0

player_change=0 #a는 0 / b는 1
while True:
    try:
        counting=int(input('부를 숫자의 개수를 입력하세요(1, 2, 3만 입력 가능) :'))
        if not 1<=counting<=3:
            raise Exception('1,2,3 중 하나를 입력하세요')
    except ValueError:
        print('정수를 입력하세요')    
    except Exception as e:
        print(e)
    
    if player_change==0:
        num+=counting
        player_change=1
        if num>=31:
            print('playerB win!')
            break

    elif player_change==1:
        num+=counting
        player_change=0
        if num>=31:
            print('playerA win!')
            break
