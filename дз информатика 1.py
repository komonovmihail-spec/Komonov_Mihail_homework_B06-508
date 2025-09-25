import turtle
import random
import time

screen = turtle.Screen()
screen.bgcolor("white")  # Белый фон
screen.tracer(0)  # Отключаем автоматическую анимацию для ручного управления

# Функция для проверки расстояния между бабочками
def is_too_close(pos1, pos2, min_distance):
    x1, y1 = pos1
    x2, y2 = pos2
    distance = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5
    return distance < min_distance

# Функция для рисования бабочки с заданными параметрами
def draw_butterfly(t, x, y, size, color1, color2, body_color, circle_color):
    t.penup()
    t.goto(x, y)
    t.setheading(0)
    t.pendown()
    
    # Основные крылья
    t.color(color1)
    t.begin_fill()
    t.circle(100 * size, 90)
    t.circle(50 * size, 90)
    t.circle(100 * size, 90)
    t.circle(50 * size, 90)
    t.end_fill()

    t.penup()
    t.goto(x - 70 * size, y)
    t.setheading(0)
    t.pendown()
    t.begin_fill()
    t.circle(100 * size, -90)
    t.circle(50 * size, -90)
    t.circle(100 * size, -90)
    t.circle(50 * size, -90)
    t.end_fill()

    # Внутренние крылья
    t.penup()
    t.goto(x - 35 * size, y - 15 * size)
    t.setheading(270)
    t.pendown()
    t.color(color2)
    t.begin_fill()
    t.circle(70 * size, 90)
    t.circle(35 * size, 90)
    t.circle(70 * size, 90)
    t.circle(35 * size, 90)
    t.end_fill()

    t.penup()
    t.goto(x - 35 * size, y - 15 * size)
    t.setheading(270)
    t.pendown()
    t.begin_fill()
    t.circle(-70 * size, 90)
    t.circle(-35 * size, 90)
    t.circle(-70 * size, 90)
    t.circle(-35 * size, 90)
    t.end_fill()

    # Тело бабочки (коричневое)
    t.penup()
    t.goto(x - 40 * size, y + 110 * size)
    t.color(body_color)
    t.pendown()
    t.begin_fill()
    t.setheading(270)
    t.forward(150 * size)
    t.left(90)
    t.forward(12 * size)
    t.left(90)
    t.forward(150 * size)
    t.end_fill()

    # Круги на крыльях
    t.penup()
    t.goto(x - 70 * size, y + 60 * size)
    t.color(circle_color)
    t.pendown()
    t.begin_fill()
    t.circle(28 * size)
    t.end_fill()

    t.penup()
    t.goto(x + 55 * size, y + 60 * size)
    t.pendown()
    t.begin_fill()
    t.circle(28 * size)
    t.end_fill()

    # Усики (коричневые)
    t.pensize(5 * size)
    t.penup()
    t.goto(x - 35 * size, y + 110 * size) 
    t.color("brown")  # Коричневые усики
    t.pendown()
    t.setheading(45)
    t.forward(73 * size)

    t.penup()
    t.goto(x - 35 * size, y + 110 * size)
    t.pendown()
    t.setheading(135)
    t.forward(73 * size)

# Создаем черепашку
t = turtle.Turtle()
t.speed(0)  # Максимальная скорость
t.pensize(2)
t.hideturtle()

# Параметры для трех бабочек с экзотическими цветами
butterflies = [
    {"size": 0.7, "color1": "darkorchid", "color2": "mediumspringgreen", "body_color": "brown", "circle_color": "gold"},
    {"size": 1.0, "color1": "deeppink", "color2": "cyan", "body_color": "brown", "circle_color": "lime"},
    {"size": 1.3, "color1": "coral", "color2": "darkviolet", "body_color": "brown", "circle_color": "turquoise"}
]

# Генерируем случайные позиции для бабочек
positions = []
min_distance = 350  # Минимальное расстояние между бабочками

# Увеличим диапазон случайных координат
x_range = (-350, 350)
y_range = (-400, 0)  # Начинаем снизу экрана

for i in range(3):
    attempts = 0
    max_attempts = 100  # Максимальное количество попыток найти подходящую позицию
    
    while attempts < max_attempts:
        # Генерируем случайные координаты в пределах экрана
        x = random.randint(x_range[0], x_range[1])
        y = random.randint(y_range[0], y_range[1])
        
        # Проверяем, не слишком ли близко к другим бабочкам
        too_close = False
        for pos in positions:
            if is_too_close((x, y), pos, min_distance):
                too_close = True
                break
        
        # Если позиция подходящая, добавляем ее и выходим из цикла
        if not too_close:
            positions.append((x, y))
            break
        
        attempts += 1
    
    # Если не удалось найти подходящую позицию после max_attempts попыток,
    # используем заранее определенные безопасные позиции
    if attempts >= max_attempts:
        safe_positions = [(-300, -200), (0, -300), (300, -100)]
        positions.append(safe_positions[len(positions)])

# Функция для обновления позиций бабочек
def update_butterflies():
    global positions
    # Очищаем экран
    t.clear()
    
    # Обновляем позиции и рисуем бабочек
    for i, pos in enumerate(positions):
        x, y = pos
        # Двигаем бабочку вверх на 2 пикселя
        y += 2
        
        # Если бабочка вышла за верхнюю границу экрана, возвращаем ее вниз
        if y > 400:
            y = -400
            
        # Обновляем позицию
        positions[i] = (x, y)
        
        # Рисуем бабочку в новой позиции
        butterfly = butterflies[i]
        draw_butterfly(t, x, y, butterfly["size"], butterfly["color1"], 
                       butterfly["color2"], butterfly["body_color"], butterfly["circle_color"])

# Основной цикл анимации
def animate():
    while True:
        update_butterflies()
        screen.update()  # Обновляем экран
        time.sleep(0.02)  # Задержка для контроля скорости анимации

# Запускаем анимацию
animate()

screen.exitonclick()
