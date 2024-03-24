# Greedy and dynamic

def greedy_algorithm(items, budget):
    # Сортуємо страви за спаданням калорійності на одиницю вартості
    sorted_items = sorted(items.items(), key=lambda x: x[1]['calories'] / x[1]['cost'], reverse=True)
    
    selected_items = []  # Обраний набір страв
    total_cost = 0  # Загальна вартість
    total_calories = 0  # Загальна калорійність
    
    # Проходимося по стравам у відсортованому порядку
    for item_name, item_info in sorted_items:
        # Перевіряємо, чи можемо додати поточну страву до набору
        if total_cost + item_info['cost'] <= budget:
            selected_items.append(item_name)
            total_cost += item_info['cost']
            total_calories += item_info['calories']
    
    return selected_items, total_cost, total_calories


def dynamic_programming(items, budget):
    n = len(items)
    dp = [[0] * (budget + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        for j in range(budget + 1):
            if items[list(items.keys())[i - 1]]["cost"] <= j:
                dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - items[list(items.keys())[i - 1]]["cost"]] + items[list(items.keys())[i - 1]]["calories"])
            else:
                dp[i][j] = dp[i - 1][j]

    # Відновлення оптимального набору страв
    selected_items = []
    j = budget
    for i in range(n, 0, -1):
        if dp[i][j] != dp[i - 1][j]:
            selected_items.append(list(items.keys())[i - 1])
            j -= items[list(items.keys())[i - 1]]["cost"]

    return selected_items, dp[n][budget]

# Оголошення словника items
items = {
    "pizza": {"cost": 50, "calories": 300},
    "hamburger": {"cost": 40, "calories": 250},
    "hot-dog": {"cost": 30, "calories": 200},
    "pepsi": {"cost": 10, "calories": 100},
    "cola": {"cost": 15, "calories": 220},
    "potato": {"cost": 25, "calories": 350}
}

while True:
    try:
        budget_input = input("Введіть бюджет або 'exit', щоб завершити: ")
        if budget_input.lower() == 'exit':
            break
        budget = int(budget_input)

        # Використання жадібного алгоритму
        selected_items, total_cost, total_calories = greedy_algorithm(items, budget)
        print("\nЖадібний алгоритм:")
        print("Обрані страви:", selected_items)
        print("Загальна вартість:", total_cost)
        print("Загальна калорійність:", total_calories)

        selected_items, total_calories = dynamic_programming(items, budget)
        print("\nДинамічне програмування:")
        print("Обрані страви:", selected_items)
        print("Загальна калорійність:", total_calories, "\n")
    except ValueError:
        print("Бюджет має бути цілим числом. Спробуйте ще раз.")
