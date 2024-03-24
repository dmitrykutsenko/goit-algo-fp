# fractal tree

import turtle
import sys

def draw_tree(t, branch_len, level):
    if level > 0:
        t.forward(branch_len)
        t.right(45)
        draw_tree(t, branch_len/2, level-1)
        t.left(90)
        draw_tree(t, branch_len/2, level-1)
        t.right(45)
        t.backward(branch_len)


def get_user_input():
    while True:
        level = input("Введіть рівень рекурсії (або 'exit' для виходу): ")
        if level.lower() == 'exit':
            sys.exit("До зустрічі!")
        try:
            level = int(level)
            if level > 0:
                return level
            else:
                print("Рівень рекурсії має бути більше 0.")
        except ValueError:
            print("Введено невірне значення. Будь ласка, введіть ціле число.")


def main():
    window = turtle.Screen()
    window.bgcolor("white")
    t = turtle.Turtle()
    t.speed(0)
    t.color("green")
    t.left(90)

    while True:
        level = get_user_input()

        # Позиція та довжина стартового стовбура
        t.penup()
        t.setpos(0, -250)
        t.pendown()
        
        # Очищення екрану перед наступним малюванням
        t.clear()

        draw_tree(t, 100, level)
        #t.reset()


if (__name__ == "__main__") or (__name__ == "__fp_02__"):
    main()
