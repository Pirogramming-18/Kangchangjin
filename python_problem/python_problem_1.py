import random as R

def brGame():
    num=0
    player_change=0 #a는 0 / b는 1

    while True:
        if player_change==0:
            counting=R.randint(1,3)
        elif player_change==1:
            try:
                counting=int(input('부를 숫자의 개수를 입력하세요(1, 2, 3만 입력 가능) :'))
                if not 1<=counting<=3:
                    raise Exception('1,2,3 중 하나를 입력하세요')
            except ValueError:
                print('정수를 입력하세요') 
                continue   
            except Exception as e:
                print(e)
                continue

        if player_change==0:
            player_change=1
            counting_all=counting+num
            while num<counting_all:
                num+=1
                print('computer : ',num)
                if num>=31:
                    # print('playerB win!')
                    return player_change
                

        elif player_change==1:
            player_change=0
            counting_all=counting+num
            while num<counting_all:
                num+=1
                print('player : ',num)
                if num>=31:
                    # print('playerB win!')
                    return player_change
            
br=brGame()
if br==0:
    print('computer win!')
elif br==1:
    print('player win!')