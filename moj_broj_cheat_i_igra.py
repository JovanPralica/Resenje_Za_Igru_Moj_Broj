import random
import time
from time import sleep
import sys
import keyboard
import threading
import os

# ASCII LOGO
print('\n')
print(r"""   _____             __   __________                   __      _____    _______   
  /     \   ____    |__|  \______   \_______  ____    |__|    /  |  |   \   _  \  
 /  \ /  \ /  _ \   |  |   |    |  _/\_  __ \/  _ \   |  |   /   |  |_  /  /_\  \ 
/    Y    (  <_> )  |  |   |    |   \ |  | \(  <_> )  |  |  /    ^   /  \  \_/   \
\____|__  /\____/\__|  |   |______  / |__|   \____/\__|  |  \____   | /\ \_____  /
        \/      \______|          \/              \______|       |__| \/       \/ """)
print('\n')
print('********************************************************************************************************')
print('\n')
print('* Predmet: Informatika')
print('\n')
print('* Tema: Najbolje resenje za moj broj')
print('\n')
print('* Godina: 2021/2022')
print('\n')
print('********************************************************************************************************')
print('\n')

def cheat():

    mbNumbers = input('\n* Unesite brojeve: ').split(',')
    mbSol = int(input('\n* Unesite resenje: '))
    mbOps = ['+','-','*','/']

    def bruteForce(array):

        while True:

            # FUNNEL METHOD

            num1 = random.choice(array)
            array.remove(num1)
            num2 = random.choice(array)
            array.remove(num2)
            num3 = random.choice(array)
            array.remove(num3)
            num4 = random.choice(array)
            array.remove(num4)
            num5 = random.choice(array)
            array.remove(num5)
            num6 = array[0]
            array.remove(num6)

            # RE-FILLING ARRAY
            array.append(num1)
            array.append(num2)
            array.append(num3)
            array.append(num4)
            array.append(num5)
            array.append(num6)

            # PATTERNS AND SPEED OPTIMIZATIONS

            # SMART PATTERN PLACEMENT

            easy_pattern1 = f'{num1} {random.choice(mbOps)} {num2}'
            easy_pattern2 = f'{num1} {random.choice(mbOps)} {num2} {random.choice(mbOps)} {num3}'
            easy_pattern3 = f'{num1} {random.choice(mbOps)} {num2} {random.choice(mbOps)} {num3} {random.choice(mbOps)} {num4}'

            pattern1 = f'{num1} {random.choice(mbOps)} ({num2} {random.choice(mbOps)} {num3} {random.choice(mbOps)} {num4})'
            pattern30 = f'({num1} {random.choice(mbOps)} {num2} {random.choice(mbOps)} ({num3} {random.choice(mbOps)} {num4}) {random.choice(mbOps)} {num5}) {random.choice(mbOps)} {num6}'

            pattern2 = f'{num1} {random.choice(mbOps)} ({num2} {random.choice(mbOps)} {num3}) {random.choice(mbOps)} {num4}'
            pattern29 = f'(({num1} {random.choice(mbOps)} {num2}) {random.choice(mbOps)} {num3}) {random.choice(mbOps)} ({num4} {random.choice(mbOps)} {num5} {random.choice(mbOps)} {num6})'
            pattern3 = f'{num1} {random.choice(mbOps)} {num2} {random.choice(mbOps)} {num3} {random.choice(mbOps)} {num4}'
            pattern28 = f'(({num1} {random.choice(mbOps)} {num2}) {random.choice(mbOps)} {num3}) {random.choice(mbOps)} ({num4} {random.choice(mbOps)} {num5})'
            pattern4 = f'{num1} {random.choice(mbOps)} ({num2} {random.choice(mbOps)} {num3} {random.choice(mbOps)} {num4})'
            pattern27 = f'({num1} {random.choice(mbOps)} ({num2} {random.choice(mbOps)} {num3}) {random.choice(mbOps)} {num4}) {random.choice(mbOps)} {num5} {random.choice(mbOps)} {num6}'
            pattern5 = f'({num1} {random.choice(mbOps)} {num2}) {random.choice(mbOps)} ({num3} {random.choice(mbOps)} {num4} {random.choice(mbOps)} {num5})'
            pattern26 = f'{num1} {random.choice(mbOps)} ({num2} {random.choice(mbOps)} {num3}) {random.choice(mbOps)} ({num4} {random.choice(mbOps)} {num5}) {random.choice(mbOps)} {num6}'
            pattern6 = f'{num1} {random.choice(mbOps)} {num2} {random.choice(mbOps)} ({num3} {random.choice(mbOps)} {num4}) {random.choice(mbOps)} ({num5} {random.choice(mbOps)} {num6})'
            pattern25 = f'{num1} {random.choice(mbOps)} {num2} {random.choice(mbOps)} {num3} {random.choice(mbOps)} ({num4} {random.choice(mbOps)} {num5}) {random.choice(mbOps)} {num6}'
            pattern7 = f'({num1} {random.choice(mbOps)} {num2} {random.choice(mbOps)} {num3}) {random.choice(mbOps)} (({num4} {random.choice(mbOps)} {num5}) {random.choice(mbOps)} {num6})'
            pattern24 = f'{num1} {random.choice(mbOps)} {num2} {random.choice(mbOps)} {num3} {random.choice(mbOps)} ({num4} {random.choice(mbOps)} {num5} {random.choice(mbOps)} {num6})'
            pattern8 = f'({num1} {random.choice(mbOps)} {num2}) {random.choice(mbOps)} ({num3} {random.choice(mbOps)} {num4} {random.choice(mbOps)} {num5}) {random.choice(mbOps)} {num6}'
            pattern23 = f'{num1} {random.choice(mbOps)} ({num2} {random.choice(mbOps)} {num3} {random.choice(mbOps)} {num4}) {random.choice(mbOps)} {num5} {random.choice(mbOps)} {num6}'
            pattern9 = f'({num1} {random.choice(mbOps)} {num2} {random.choice(mbOps)} {num3} {random.choice(mbOps)} {num4}) {random.choice(mbOps)} {num5}'
            pattern22 = f'({num1} {random.choice(mbOps)} {num2} {random.choice(mbOps)} ({num3} {random.choice(mbOps)} {num4})) {random.choice(mbOps)} {num5} {random.choice(mbOps)} {num6}'
            pattern10 = f'{num1} {random.choice(mbOps)} {num2} {random.choice(mbOps)} {num3} {random.choice(mbOps)} ({num4} {random.choice(mbOps)} {num5} {random.choice(mbOps)} {num6})'
            pattern21 = f'({num1} {random.choice(mbOps)} {num2}) {random.choice(mbOps)} {num3} {random.choice(mbOps)} {num4} {random.choice(mbOps)} {num5} {random.choice(mbOps)} {num6}'
            pattern11 = f'({num1} {random.choice(mbOps)} ({num2} {random.choice(mbOps)} {num3}) {random.choice(mbOps)} ({num4} - {num5})) {random.choice(mbOps)} {num6}'
            pattern20 = f'({num1} {random.choice(mbOps)} {num2} {random.choice(mbOps)} {num3} {random.choice(mbOps)} ({num4} {random.choice(mbOps)} {num5})) {random.choice(mbOps)} {num6}'
            pattern12 = f'{num1} {random.choice(mbOps)} {num2} {random.choice(mbOps)} ({num3} {random.choice(mbOps)} {num4} {random.choice(mbOps)} ({num5} {random.choice(mbOps)} {num6}))'
            pattern19 = f'({num1} {random.choice(mbOps)} ({num2} {random.choice(mbOps)} {num3}) {random.choice(mbOps)} {num4} {random.choice(mbOps)} {num5}) {random.choice(mbOps)} {num6}'
            pattern13 = f'({num1} {random.choice(mbOps)} {num2}) {random.choice(mbOps)} (({num3} {random.choice(mbOps)} {num4} {random.choice(mbOps)} {num5}) {random.choice(mbOps)} {num6})'
            pattern18 = f'{num1} {random.choice(mbOps)} ({num2} {random.choice(mbOps)} {num3}) {random.choice(mbOps)} ({num4} {random.choice(mbOps)} {num5})'
            pattern14 = f'{num1} {random.choice(mbOps)} (({num2} {random.choice(mbOps)} {num3} {random.choice(mbOps)} {num4}) {random.choice(mbOps)} {num5}) {random.choice(mbOps)} {num6}'
            pattern17 = f'{num1} {random.choice(mbOps)} {num2} {random.choice(mbOps)} ({num3} {random.choice(mbOps)} ({num4} {random.choice(mbOps)} {num5}) {random.choice(mbOps)} {num6})'
            pattern15 = f'({num1} {random.choice(mbOps)} {num2}) {random.choice(mbOps)} (({num3} {random.choice(mbOps)} {num4}) {random.choice(mbOps)} {num5} {random.choice(mbOps)} {num6})'
            pattern16 = f'{num1} {random.choice(mbOps)} {num2} {random.choice(mbOps)} (({num3} {random.choice(mbOps)} {num4}) {random.choice(mbOps)} {num5} {random.choice(mbOps)} {num6})'

            # PATTERN LIST

            pattern_list = [easy_pattern1, easy_pattern2, easy_pattern3, pattern1, pattern2, pattern3, pattern4,
                            pattern5, pattern6, pattern7, pattern8, pattern9, pattern10, pattern11, pattern12,
                            pattern13, pattern14, pattern15, pattern16, pattern17, pattern18, pattern19, pattern20,
                            pattern21, pattern22, pattern23, pattern24, pattern25, pattern26, pattern27,
                            pattern28, pattern29, pattern30]

            # MATCHING PATTERN WITH MB SOL


            try:

                timer = time.process_time()

                for pattern in pattern_list:

                    if eval(pattern) == mbSol:
                        print('\n' + '* Rezultat:', pattern, '=', mbSol)
                        print('\n' + f'* Vreme programa: {timer} sec')
                        time.sleep(20)
                        sys.exit()

                    # OUTCOME 2 EXAMPLE 2,1,2,1,10,25,590
                    # OUTCOME 2 EXAMPLE 1,6,5,4,20,75,907

                    elif timer >= 5 and pattern != mbSol:

                        if eval(pattern) == mbSol:
                            print('\n' + '* Rezultat:', pattern, '=', mbSol)
                            print('\n' + f'* Vreme programa: {timer} sec')
                            time.sleep(20)
                            sys.exit()

                        if eval(pattern) == mbSol - 1:
                            print('\n' + '* Rezultat:', pattern, '=', mbSol - 1)
                            print('\n' + f'* Vreme programa: {timer} sec')
                            time.sleep(20)
                            sys.exit()

                        elif eval(pattern) == mbSol + 1:
                            print('\n' + '* Rezultat:', pattern, '=', mbSol + 1)
                            print('\n' + f'* Vreme programa: {timer} sec')
                            time.sleep(20)
                            sys.exit()

                        elif eval(pattern) == mbSol + 2:
                            print('\n' + '* Rezultat:', pattern, '=', mbSol + 2)
                            print('\n' + f'* Vreme programa: {timer} sec')
                            time.sleep(20)
                            sys.exit()

                        elif eval(pattern) == mbSol - 2:
                            print('\n' + '* Rezultat:', pattern, '=', mbSol - 2)
                            print('\n' + f'* Vreme programa: {timer} sec')
                            time.sleep(20)
                            sys.exit()

                # OUTCOME 3

                if timer >= 10:
                    print('\n' + '* Program nije uspeo da nadje priblizno resenje :( ')
                    time.sleep(20)
                    sys.exit()

            # FIXING VALUE,ZERO-DIVISION,NAME ERROR

            except ZeroDivisionError:
                continue

            except ValueError:
                print('Please enter only numbers')
                break

            except NameError:
                print('Please enter only numbers')
                break

            except KeyboardInterrupt:
                print('\n* Izasli ste iz programa')
                break

    bruteForce(mbNumbers)

def game():

    global my_timer

    # LISTS FOR SELECTION
    firstFour = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    firstTwo = [10, 25]
    lastTwo = [50, 100]
    sol = 0

    # FIRST FOUR SELECTION
    for num in firstFour:
        num1 = random.choice(firstFour)
        num2 = random.choice(firstFour)
        num3 = random.choice(firstFour)
        num4 = random.choice(firstFour)

    # LAST TWO SELECTION
    for lastNum in lastTwo:
        num5 = random.choice(firstTwo)
        num6 = random.choice(lastTwo)

    # MB LISTS
    mbList = [[num1,num2,num3,num4,num5,num6], []]
    mbSol = int(random.randint(50, 999))
    mbOps = ['+', '-', '*', '/']

    print('\n* Pritisnite "Space" taster da bi ste zapoceli igru: \n')

    while sol == 0:

        sol = 0

        for q in range(1, 100):
            print(f'* Vasi brojevi su: {q} {q} {q} {q} {q} {q}',end='\r')

        if keyboard.is_pressed('space'):
            print(f'* Vasi brojevi su: {mbList[0]}', end='\r')
            break

    print(f'\n\n* Vase resenje je: [{mbSol}]')

    user_solve = ''

    def countdown():
        global my_timer

        my_timer = 60

        for x in range(60):
            my_timer = my_timer - 1
            sleep(1)

        if my_timer == 0 and user_solve == '':
            print('\n\n* Vreme je isteklo')
            os._exit(1)

    countdown_thread = threading.Thread(target=countdown)

    timer_input = input('\n* Zelite li da ukljucite timer? (da/ne): ')

    if timer_input == 'da':
        print('\n* Imate 1 minut da unesete izraz!')

        countdown_thread.start()
    else:
        print('\n* Vreme za ovaj izraz je neograniceno')

    user_solve = input('\n* Unesite izraz:')

    try:

        user_list = user_solve.split(' ')

        # CHECK IF USER INPUT IS VALID

        # OPERATOR FILTER
        for each in user_list:
            if each.isdigit():
                continue
            else:
                user_list.remove(each)

        # FROM STR TO INT FILTER
        ul_str_to_int = map(int, user_list)
        mbList[1] = list(ul_str_to_int)

        # COMPARE LIST FUNCTION
        def compareList(l1, l2):
            l1.sort()
            l2.sort()

            for each in l1:
                if l1.count(each) > l2.count(each):
                    print('Mozete uneti samo postojace brojeve')
                    time.sleep(12)
                    sys.exit()
                else:
                    continue

        compareList(mbList[1], mbList[0])

        # PRINT SCORE
        print('\n''* Vas rezultat:', user_solve, '=', eval(user_solve))

        # SCORE COUNTING

        if eval(user_solve) == mbSol:
            print('\n* Udaljenost 0 = +10 Poena')

        elif eval(user_solve) == mbSol - 1:
            print('\n* Udaljenost 1 = +8 Poena')

        elif eval(user_solve) == mbSol + 1:
            print('\n* Udaljenost 1 = +8 Poena')

        elif eval(user_solve) == mbSol + 2:
            print('\n* Udaljenost 2 = +4 Poena')

        elif eval(user_solve) == mbSol - 2:
            print('\n* Udaljenost 2 = +4 Poena')

        else:
            print('\n* Udaljenost veca od 2 = 0 Poena')

    # ERROR FIXING

    except NameError:
        print('Molimo vas, unosite samo brojeve i matematicke operatore!')
        time.sleep(12)
        sys.exit()

    except ZeroDivisionError:
        print('Ne mozete deliti sa nulom!')
        time.sleep(12)
        sys.exit()

    except ValueError:
        print('Izraz nije ispravan!')
        time.sleep(12)
        sys.exit()


    # BRUTFORCE METHOD

    def bruteForce(array):

        while True:

            # FUNNEL METHOD

            num1 = random.choice(array)
            array.remove(num1)
            num2 = random.choice(array)
            array.remove(num2)
            num3 = random.choice(array)
            array.remove(num3)
            num4 = random.choice(array)
            array.remove(num4)
            num5 = random.choice(array)
            array.remove(num5)
            num6 = array[0]
            array.remove(num6)

            # RE-FILLING ARRAY
            array.append(num1)
            array.append(num2)
            array.append(num3)
            array.append(num4)
            array.append(num5)
            array.append(num6)

            # PATTERNS AND SPEED OPTIMIZATIONS

            # SMART PATTERN PLACEMENT

            easy_pattern1 = f'{num1} {random.choice(mbOps)} {num2}'
            easy_pattern2 = f'{num1} {random.choice(mbOps)} {num2} {random.choice(mbOps)} {num3}'
            easy_pattern3 = f'{num1} {random.choice(mbOps)} {num2} {random.choice(mbOps)} {num3} {random.choice(mbOps)} {num4}'

            pattern1 = f'{num1} {random.choice(mbOps)} ({num2} {random.choice(mbOps)} {num3} {random.choice(mbOps)} {num4})'
            pattern30 = f'({num1} {random.choice(mbOps)} {num2} {random.choice(mbOps)} ({num3} {random.choice(mbOps)} {num4}) {random.choice(mbOps)} {num5}) {random.choice(mbOps)} {num6}'

            pattern2 = f'{num1} {random.choice(mbOps)} ({num2} {random.choice(mbOps)} {num3}) {random.choice(mbOps)} {num4}'
            pattern29 = f'(({num1} {random.choice(mbOps)} {num2}) {random.choice(mbOps)} {num3}) {random.choice(mbOps)} ({num4} {random.choice(mbOps)} {num5} {random.choice(mbOps)} {num6})'
            pattern3 = f'{num1} {random.choice(mbOps)} {num2} {random.choice(mbOps)} {num3} {random.choice(mbOps)} {num4}'
            pattern28 = f'(({num1} {random.choice(mbOps)} {num2}) {random.choice(mbOps)} {num3}) {random.choice(mbOps)} ({num4} {random.choice(mbOps)} {num5})'
            pattern4 = f'{num1} {random.choice(mbOps)} ({num2} {random.choice(mbOps)} {num3} {random.choice(mbOps)} {num4})'
            pattern27 = f'({num1} {random.choice(mbOps)} ({num2} {random.choice(mbOps)} {num3}) {random.choice(mbOps)} {num4}) {random.choice(mbOps)} {num5} {random.choice(mbOps)} {num6}'
            pattern5 = f'({num1} {random.choice(mbOps)} {num2}) {random.choice(mbOps)} ({num3} {random.choice(mbOps)} {num4} {random.choice(mbOps)} {num5})'
            pattern26 = f'{num1} {random.choice(mbOps)} ({num2} {random.choice(mbOps)} {num3}) {random.choice(mbOps)} ({num4} {random.choice(mbOps)} {num5}) {random.choice(mbOps)} {num6}'
            pattern6 = f'{num1} {random.choice(mbOps)} {num2} {random.choice(mbOps)} ({num3} {random.choice(mbOps)} {num4}) {random.choice(mbOps)} ({num5} {random.choice(mbOps)} {num6})'
            pattern25 = f'{num1} {random.choice(mbOps)} {num2} {random.choice(mbOps)} {num3} {random.choice(mbOps)} ({num4} {random.choice(mbOps)} {num5}) {random.choice(mbOps)} {num6}'
            pattern7 = f'({num1} {random.choice(mbOps)} {num2} {random.choice(mbOps)} {num3}) {random.choice(mbOps)} (({num4} {random.choice(mbOps)} {num5}) {random.choice(mbOps)} {num6})'
            pattern24 = f'{num1} {random.choice(mbOps)} {num2} {random.choice(mbOps)} {num3} {random.choice(mbOps)} ({num4} {random.choice(mbOps)} {num5} {random.choice(mbOps)} {num6})'
            pattern8 = f'({num1} {random.choice(mbOps)} {num2}) {random.choice(mbOps)} ({num3} {random.choice(mbOps)} {num4} {random.choice(mbOps)} {num5}) {random.choice(mbOps)} {num6}'
            pattern23 = f'{num1} {random.choice(mbOps)} ({num2} {random.choice(mbOps)} {num3} {random.choice(mbOps)} {num4}) {random.choice(mbOps)} {num5} {random.choice(mbOps)} {num6}'
            pattern9 = f'({num1} {random.choice(mbOps)} {num2} {random.choice(mbOps)} {num3} {random.choice(mbOps)} {num4}) {random.choice(mbOps)} {num5}'
            pattern22 = f'({num1} {random.choice(mbOps)} {num2} {random.choice(mbOps)} ({num3} {random.choice(mbOps)} {num4})) {random.choice(mbOps)} {num5} {random.choice(mbOps)} {num6}'
            pattern10 = f'{num1} {random.choice(mbOps)} {num2} {random.choice(mbOps)} {num3} {random.choice(mbOps)} ({num4} {random.choice(mbOps)} {num5} {random.choice(mbOps)} {num6})'
            pattern21 = f'({num1} {random.choice(mbOps)} {num2}) {random.choice(mbOps)} {num3} {random.choice(mbOps)} {num4} {random.choice(mbOps)} {num5} {random.choice(mbOps)} {num6}'
            pattern11 = f'({num1} {random.choice(mbOps)} ({num2} {random.choice(mbOps)} {num3}) {random.choice(mbOps)} ({num4} - {num5})) {random.choice(mbOps)} {num6}'
            pattern20 = f'({num1} {random.choice(mbOps)} {num2} {random.choice(mbOps)} {num3} {random.choice(mbOps)} ({num4} {random.choice(mbOps)} {num5})) {random.choice(mbOps)} {num6}'
            pattern12 = f'{num1} {random.choice(mbOps)} {num2} {random.choice(mbOps)} ({num3} {random.choice(mbOps)} {num4} {random.choice(mbOps)} ({num5} {random.choice(mbOps)} {num6}))'
            pattern19 = f'({num1} {random.choice(mbOps)} ({num2} {random.choice(mbOps)} {num3}) {random.choice(mbOps)} {num4} {random.choice(mbOps)} {num5}) {random.choice(mbOps)} {num6}'
            pattern13 = f'({num1} {random.choice(mbOps)} {num2}) {random.choice(mbOps)} (({num3} {random.choice(mbOps)} {num4} {random.choice(mbOps)} {num5}) {random.choice(mbOps)} {num6})'
            pattern18 = f'{num1} {random.choice(mbOps)} ({num2} {random.choice(mbOps)} {num3}) {random.choice(mbOps)} ({num4} {random.choice(mbOps)} {num5})'
            pattern14 = f'{num1} {random.choice(mbOps)} (({num2} {random.choice(mbOps)} {num3} {random.choice(mbOps)} {num4}) {random.choice(mbOps)} {num5}) {random.choice(mbOps)} {num6}'
            pattern17 = f'{num1} {random.choice(mbOps)} {num2} {random.choice(mbOps)} ({num3} {random.choice(mbOps)} ({num4} {random.choice(mbOps)} {num5}) {random.choice(mbOps)} {num6})'
            pattern15 = f'({num1} {random.choice(mbOps)} {num2}) {random.choice(mbOps)} (({num3} {random.choice(mbOps)} {num4}) {random.choice(mbOps)} {num5} {random.choice(mbOps)} {num6})'
            pattern16 = f'{num1} {random.choice(mbOps)} {num2} {random.choice(mbOps)} (({num3} {random.choice(mbOps)} {num4}) {random.choice(mbOps)} {num5} {random.choice(mbOps)} {num6})'

            # PATTERN LIST

            pattern_list = [easy_pattern1,easy_pattern2,easy_pattern3,pattern1, pattern2, pattern3, pattern4,
                            pattern5, pattern6, pattern7, pattern8, pattern9,pattern10, pattern11, pattern12,
                            pattern13, pattern14, pattern15, pattern16, pattern17, pattern18, pattern19, pattern20,
                            pattern21, pattern22, pattern23, pattern24,pattern25, pattern26, pattern27,
                            pattern28, pattern29, pattern30]

            # MATCHING PATTERN WITH MB SOL

            try:
                timer = time.process_time()

                for pattern in pattern_list:

                    if eval(pattern) == mbSol:
                        print('\n' + '* Rezultat:', pattern, '=', mbSol)
                        print('\n' + f'* Vreme programa: {timer} sec')                        
                        time.sleep(20)
                        sys.exit()

                    # OUTCOME 2 EXAMPLE 2,1,2,1,10,25,590
                    # OUTCOME 2 EXAMPLE 1,6,5,4,20,75,907

                    elif timer >= 5 and pattern != mbSol:

                        if eval(pattern) == mbSol:
                            print('\n' + '* Rezultat:', pattern, '=', mbSol)
                            print('\n' + f'* Vreme programa: {timer} sec')
                            time.sleep(20)
                            sys.exit()

                        if eval(pattern) == mbSol - 1:
                            print('\n' + '* Rezultat:', pattern, '=', mbSol - 1)
                            print('\n' + f'* Vreme programa: {timer} sec')
                            time.sleep(20)
                            sys.exit()

                        elif eval(pattern) == mbSol + 1:
                            print('\n' + '* Rezultat:', pattern, '=', mbSol + 1)
                            print('\n' + f'* Vreme programa: {timer} sec')
                            time.sleep(20)
                            sys.exit()

                        elif eval(pattern) == mbSol + 2:
                            print('\n' + '* Rezultat:', pattern, '=', mbSol + 2)
                            print('\n' + f'* Vreme programa: {timer} sec')                            
                            time.sleep(20)
                            sys.exit()

                        elif eval(pattern) == mbSol - 2:
                            print('\n' + '* Rezultat:', pattern, '=', mbSol - 2)
                            print('\n' + f'* Vreme programa: {timer} sec')                            
                            time.sleep(20)
                            sys.exit()

                # OUTCOME 3

                if timer >= 10:
                    print('\n' + '* Program nije uspeo da nadje priblizno resenje :( ')
                    time.sleep(20)
                    sys.exit()

            # FIXING VALUE,ZERO-DIVISION,NAME ERROR

            except ZeroDivisionError:
                continue

            except ValueError:
                print('Please enter only numbers')
                break

            except NameError:
                print('Please enter only numbers')
                break

            except KeyboardInterrupt:
                print('\n* Izasli ste iz programa')
                break

    bruteForce(mbList[0])

def menu():
    user_input = int(input('\n1) Resenje Za Moj Broj \n2) Igra Moj Broj \n\n* Unesite broj:'))

    if user_input == 1:
        cheat()
    elif user_input == 2:
        game()
    else:
        print('\n* Mozete uneti samo ponudjene brojeve')
        menu()

menu()