# MC new

import random

# Вхідні дані з таблиці вимірювань
input_data = {
    2: 0.0278,
    3: 0.0556,
    4: 0.0833,
    5: 0.1111,
    6: 0.1389,
    7: 0.1667,
    8: 0.1389,
    9: 0.1111,
    10: 0.0833,
    11: 0.0556,
    12: 0.0278
}

# Створення порожнього словника для збереження кількості кожної можливої суми
sum_count = {}
probabilities = {}

def roll_dice():
    return random.randint(1, 6)

def monte_carlo_simulation(num_trials):
    results = {}
    for _ in range(num_trials):
        roll1 = roll_dice()
        roll2 = roll_dice()
        total = roll1 + roll2
        if total in results:
            results[total] += 1
        else:
            results[total] = 1
    return results

def calculate_probabilities(results, num_trials):
    probabilities = {}
    for total, count in results.items():
        probabilities[total] = count / num_trials * 100
    return probabilities

def print_results(probabilities):
    print("Сума\tЙмовірність")
    for total, probability in sorted(probabilities.items()):
        print(f"{total}\t{probability:.2f}% ({probability/100:.4f})")
        sum_count[total] = round((probability/100),4)

def compare_results(monte_carlo_results, input_data):
    print("Сума\tЙмовірність (Monte Carlo)\tЙмовірність (Вхідні дані)")
    for total in range(2, 13):
        probability_mc = monte_carlo_results.get(total, 0)
        probability_input = input_data.get(total, 0)
        print(f"{total}\t{probability_mc:.4f}\t\t\t\t{probability_input:.4f}")


def main():
    num_trials = 1000000
    results = monte_carlo_simulation(num_trials)
    probabilities = calculate_probabilities(results, num_trials)
    print("Використавши метод Монте Карло отримали такі виміри:")
    print_results(probabilities)
    print()
    print("Порівняння отриманих результатів з вхідними даними:")
    compare_results(sum_count, input_data)

if (__name__ == "__main__") or (__name__ == "__fp_07__"):
    main()

"""
Загальною тенденцією є те, що результати методу Монте-Карло досить близькі до аналітичних розрахунків,
але в деяких випадках може спостерігатися невелике відхилення. Ми отримали майже ідентичні дані.
"""