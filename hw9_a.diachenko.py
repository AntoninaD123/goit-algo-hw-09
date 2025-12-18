# Набір монет
coins = [50, 25, 10, 5, 2, 1]

# -----------------------------
# Жадібний алгоритм
# -----------------------------
def find_coins_greedy(amount):
    result = {}
    remaining = amount
    
    for coin in coins:
        count = remaining // coin
        if count > 0:
            result[coin] = count
            remaining -= coin * count
    
    return result

# -----------------------------
# Динамічне програмування
# -----------------------------
def find_min_coins(amount):
    # dp[i] = мінімальна кількість монет для суми i
    dp = [float('inf')] * (amount + 1)
    dp[0] = 0  # 0 монет для суми 0

    # Відслідковуємо, яку монету використали
    coin_used = [0] * (amount + 1)
    
    for i in range(1, amount + 1):
        for coin in coins:
            if i >= coin and dp[i - coin] + 1 < dp[i]:
                dp[i] = dp[i - coin] + 1
                coin_used[i] = coin
    
    # Відновлюємо набір монет
    result = {}
    current = amount
    while current > 0:
        coin = coin_used[current]
        if coin in result:
            result[coin] += 1
        else:
            result[coin] = 1
        current -= coin
    
    return result

# -----------------------------
# Приклади використання
# -----------------------------
amount = 113

greedy_result = find_coins_greedy(amount)
dp_result = find_min_coins(amount)

print("Жадібний алгоритм:", greedy_result)
print("Динамічне програмування:", dp_result)
