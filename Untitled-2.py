def calculate_area(length, width):
    return length * width

rectangles = []

for i in range(3):
    length = float(input(f"Введіть довжину прямокутника {i+1}: "))
    width = float(input(f"Введіть ширину прямокутника {i+1}: "))
    area = calculate_area(length, width)
    rectangles.append(area)
    print(f"Площа прямокутника {i+1}: {area}")



#Завдання 2

    import math

def calculate_hypotenuse(a, b):
    return math.sqrt(a**2 + b**2)


a1 = float(input("Введіть перший катет першого трикутника: "))
b1 = float(input("Введіть другий катет першого трикутника: "))
hypotenuse1 = calculate_hypotenuse(a1, b1)
print(f"Гіпотенуза першого трикутника: {hypotenuse1}")


a2 = float(input("Введіть перший катет другого трикутника: "))
b2 = float(input("Введіть другий катет другого трикутника: "))
hypotenuse2 = calculate_hypotenuse(a2, b2)
print(f"Гіпотенуза другого трикутника: {hypotenuse2}")


if hypotenuse1 > hypotenuse2:
    print("Гіпотенуза першого трикутника більша за гіпотенузу другого трикутника.")
elif hypotenuse1 < hypotenuse2:
    print("Гіпотенуза другого трикутника більша за гіпотенузу першого трикутника.")
else:
    print("Гіпотенузи трикутників рівні.")









#Завдання 3



    def is_inside_circle(x, y, a, b, R):
    return (x - a)**2 + (y - b)**2 < R**2


a = float(input("Введіть координату a центру кола: "))
b = float(input("Введіть координату b центру кола: "))
R = float(input("Введіть радіус кола: "))


points = {
    "P": (float(input("Введіть координату x точки P: ")), float(input("Введіть координату y точки P: "))),
    "F": (float(input("Введіть координату x точки F: ")), float(input("Введіть координату y точки F: "))),
    "L": (float(input("Введіть координату x точки L: ")), float(input("Введіть координату y точки L: ")))
}


inside_count = 0
for point_name, (px, py) in points.items():
    if is_inside_circle(px, py, a, b, R):
        inside_count += 1

print(f"Кількість точок, що лежать всередині кола: {inside_count}")\




#Завдання 4




def quadrilateral_area(X, Y, Z, T):
    
    return 0.5 * X * Y


X = float(input("Введіть довжину сторони X: "))
Y = float(input("Введіть довжину сторони Y: "))
Z = float(input("Введіть довжину сторони Z: "))
T = float(input("Введіть довжину сторони T: "))


area = quadrilateral_area(X, Y, Z, T)
print(f"Площа чотирикутника: {area}")



#Завдання 5




def find_divisible_numbers(n, divisors):
    result = []
    for num in range(1, n+1):
        if all(num % d == 0 for d in divisors):
            result.append(num)
    return result


n = int(input("Введіть натуральне число n: "))


divisors = list(map(int, input("Введіть числа, на які повинні ділитися всі знайдені числа, через пробіл: ").split()))


divisible_numbers = find_divisible_numbers(n, divisors)
print(f"Натуральні числа, що не перевищують {n}, які діляться на кожне із заданих чисел: {divisible_numbers}")
