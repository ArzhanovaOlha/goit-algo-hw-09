import timeit
RED = "\33[91m"
GREEN = "\033[32m"
RESET = "\033[0m"
YELLOW = "\033[33m"

def find_coins_greedy(change, coins_weight):
    coins_count = {}
    current_change = change
    for coin in coins_weight:
        count = current_change // coin
        if count > 0:
            coins_count[coin] = count
        current_change -= coin * count
    return coins_count


def find_min_coins(change, coins_weight):
    coins_count = {}
    coins_count_list = [0] + [float('inf')]*change
    coins_weight_list = [0]*(change + 1)

    for i in range(1, change +1):
        for coin in coins_weight:
            if i >= coin and coins_count_list[i - coin] + 1 < coins_count_list[i]:
                coins_count_list[i] = coins_count_list[i - coin] + 1
                coins_weight_list[i] = coin
    
    current_change = change
    while current_change > 0:
        coin = coins_weight_list[current_change]
        coins_count[coin] = coins_count.get(coin, 0) + 1
        current_change -= coin

    return coins_count



change_list = [113, 15, 3578]
coins_weight= [50, 25, 10, 5, 1]

if __name__ == '__main__':
    print(f'''
          {YELLOW}Gready algorithm:{RESET}
          ''')
    for change in change_list:
        timer = timeit.timeit(lambda: find_coins_greedy(change, coins_weight), number=1000)
        print(f'For change {GREEN}{change}{RESET} you should take coins with weight: {GREEN}{find_coins_greedy(change, coins_weight)}{RESET}')
        print(f'''The time is: {RED}{timer}{RESET}
    ''')
    print(f'''
          {YELLOW}Dinamic programming:{RESET}
          ''')
    for change in change_list:
        timer = timeit.timeit(lambda: find_min_coins(change, coins_weight), number=1000)
        print(f'For change {GREEN}{change}{RESET} you should take coins with weight: {GREEN}{find_min_coins(change, coins_weight)}{RESET}')
        print(f'''The time is: {RED}{timer}{RESET}
          ''')


