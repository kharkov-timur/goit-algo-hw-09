import time


def find_coins_greedy(amount):
    coins = [50, 25, 10, 5, 2, 1]
    result = {}
    for coin in coins:
        if amount >= coin:
            result[coin] = amount // coin
            amount -= coin * (amount // coin)
    return result


def find_min_coins(amount):
    coins = [1, 2, 5, 10, 25, 50]
    dp = [float("inf")] * (amount + 1)
    dp[0] = 0
    coin_used = [0] * (amount + 1)

    for coin in coins:
        for i in range(coin, amount + 1):
            if dp[i - coin] + 1 < dp[i]:
                dp[i] = dp[i - coin] + 1
                coin_used[i] = coin

    result = {}
    while amount > 0:
        result[coin_used[amount]] = result.get(coin_used[amount], 0) + 1
        amount -= coin_used[amount]

    return result


def measure_time_for_amount(algorithm, amount):
    start_time = time.time()
    result = algorithm(amount)
    end_time = time.time()
    return result, end_time - start_time


large_amounts = [1000, 5000, 10000, 50000, 100000]

for amount in large_amounts:
    print(f"Amount: {amount}")
    result_greedy, time_greedy = measure_time_for_amount(find_coins_greedy, amount)
    print("Greedy Algorithm:")
    print("Result:", result_greedy)
    print("Time:", time_greedy)

    result_dp, time_dp = measure_time_for_amount(find_min_coins, amount)
    print("Dynamic Programming:")
    print("Result:", result_dp)
    print("Time:", time_dp)
    print()
