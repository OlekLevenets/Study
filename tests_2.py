import math

# Завдання 1: Як ввести ім'я та вік користувача і вивести відповідь?
name = str(input("Як тебе звати? " ))
age = int(input("Скільки тобі років? " ))
print(f"Hello {name}, you are {age} yo.")

# Завдання 2: Як обчислити площу кола для радіуса 5?
radius = 5
s_circle =math.pi * radius ** 2
print(f"Площа кола з радіусом 5 довівнює: {s_circle}")

#Завдання 3: Як перевірити, чи є число 27 кратним 3?
is_multiple = 27 % 3 == 0
print(f"Чи є число 27 кратним 3? {is_multiple}")


# Завдання 4: Як додати нову страву до списку улюблених страв?
favorite_dishes = ["spaggeti","pizza","borshch"]
favorite_dishes.pop(0)
favorite_dishes.append("shashlyk")
print(f"Улюблені страви після змін: {favorite_dishes}")

# Завдання 5: Як змінити регістр рядка та вивести його у зворотному порядку?
word = str(input("Впиши слово:  " ))
print(f"Великими літерами: {word.upper()}, Малими літерами: {word.lower()}, Зворотній порядок: {word[::-1]}")


# Завдання 6: Як додати нового друга до словника?
friends_sports = {"Artur":"Football","Masya":"bowling","Daryna":"hockey"}
print(f"Словник друзів: {friends_sports}")
friends_sports["Andrew"] = "volleyball" # додавання до словника
print(f"Словник друзів з доданим другом: {friends_sports}")

# Завдання 7: Як перевірити, чи є число парним?
number = float(input("Впиши число для перевірки на парність:  " ))
if number % 2 == 0:
    print(f"Число {number} парне")
else:
    print(f"Число {number} не парне")

# Завдання 8: Як обчислити факторіал числа 5?
number_factorial = int(input("Впиши число для факторіалу: " ))
print(f"Факторіал числа {number_factorial} = {math.factorial(number_factorial)}")

# Завдання 9: Як вивести всі числа від 1 до 20, пропускаючи числа, кратні 3?
numbers_skipping_3 = [i for i in range(1, 21) if i % 3 != 0]
print(f"Числа від 1 до 20, пропускаючи кратні 3: {numbers_skipping_3}")

# Завдання 10: Як підрахувати кількість голосних у введеному реченні?
sentence = """Ой у лузі червона калина похилилася
Чогось наша славна Україна зажурилася."""
vowels = "аеєиіїоуюяАЕЄИІЇОУЮЯ"
vowel_count = sum(1 for char in sentence if char in vowels)
print(f"Кількість голосних у реченні: {vowel_count}")

# Завдання 11: Як замінити пробіли в рядку на символ '_'
nospace_sentence = sentence.replace(" ", "_")
print(f"Речення з зміненим пробілом на нижній прочерк: {nospace_sentence}")
