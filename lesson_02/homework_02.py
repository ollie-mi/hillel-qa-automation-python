# task 01 == Розділіть змінну alice_in_wonderland так, щоб вона займала декілька фізичних лінії
# task 02 == Знайдіть та екрануйте всі символи одинарної дужки у тексті
# task 03 == Виведіть змінну alice_in_wonderland на друк

alice_in_wonderland = '"Would you tell me, please, which way I ought to go from here?"\n' \
                       '"That depends a good deal on where you want to get to," said the Cat.\n' \
                       '"I don\'t much care where ——" said Alice.\n' \
                       '"Then it doesn\'t matter which way you go," said the Cat.\n' \
                       '"—— so long as I get somewhere," Alice added as an explanation.\n' \
                       '"Oh, you\'re sure to do that," said the Cat, "if you only walk long enough."'
print(alice_in_wonderland, end="\n\n")


"""
    # Задачі 04 -10:
    # Переведіть задачі з книги "Математика, 5 клас"
    # на мову пітон і виведіть відповідь, так, щоб було
    # зрозуміло дитині, що навчається в п'ятому класі
"""
# task 04
"""
Площа Чорного моря становить 436 402 км2, а площа Азовського
моря становить 37 800 км2. Яку площу займають Чорне та Азов-
ське моря разом?
"""
metric = 'км2'
black_sea = 436402
azov_sea = 37800
total_area = black_sea + azov_sea
print(f"Загальна плоша Чорного та Азовського морів становить {total_area} {metric}", end="\n\n")


# task 05
"""
Мережа супермаркетів має 3 склади, де всього розміщено
375 291 товар. На першому та другому складах перебуває
250 449 товарів. На другому та третьому – 222 950 товарів.
Знайдіть кількість товарів, що розміщені на кожному складі.
"""
total_items = 375291
first_and_second_storage_items = 250449
second_and_third_storage_items = 222950

first_storage_items = total_items - second_and_third_storage_items
second_storage_items = first_and_second_storage_items - first_storage_items
third_storage_items = total_items - first_and_second_storage_items

print(f"На першому складі знаходиться {first_storage_items} товарів. На другому складі {second_storage_items} "
      f"товарів. А на третьому складі знаходиться {third_storage_items} товарів.", end="\n\n")

# task 06
"""
Михайло разом з батьками вирішили купити комп’ютер, ско-
риставшись послугою «Оплата частинами». Відомо, що сплачу-
вати необхідно буде півтора року по 1179 грн/місяць. Обчисліть
вартість комп’ютера.
"""
month_year = 12
half_year = int(month_year / 2)
term = month_year + half_year
price_per_month = 1179
currency = 'грн'

computer_price = price_per_month * term
print(f"Якщо платити {price_per_month} {currency} в місяць, то виходить що вартість компʼютера {computer_price} "
      f"{currency}", end="\n\n")


# task 07
"""
Знайди остачу від діленя чисел:
a) 8019 : 8     d) 7248 : 6
b) 9907 : 9     e) 7128 : 5
c) 2789 : 5     f) 19224 : 9
"""
num_dict = {
    "a": [8019, 8], "b": [9907, 9],
    "c": [2789, 5], "d": [7248, 6],
    "e": [7128, 5], "f": [19224, 9]
}

for key, value in num_dict.items():
    modulus = value[0] % value[1]
    print(f"{key}) Остача від ділення {value[0]} на {value[1]} буде {modulus}")
print("\n\n")

# task 08
"""
Іринка, готуючись до свого дня народження, склала список того,
що їй потрібно замовити. Обчисліть, скільки грошей знадобиться
для даного її замовлення.
Назва товару    Кількість   Ціна
Піца велика     4           274 грн
Піца середня    2           218 грн
Сік             4           35 грн
Торт            1           350 грн
Вода            3           21 грн
"""
birthday_party = ((
    {"name": "великих піц", "amount": 4, "price": 274},
    {"name": "маленькі піци", "amount": 2, "price": 218},
    {"name": "пакета соку", "amount": 4, "price": 35},
    {"name": "торт", "amount": 1, "price": 350},
    {"name": "пляшки води", "amount": 3, "price": 21},
))
currency = 'грн'

print("Іринка має заплатити", end=' ')
total = 0
for item in birthday_party:
    total_item_price = item['amount'] * item['price']
    print(f"за {item['amount']} {item['name']} - {total_item_price} {currency}", end=', ')
    total += total_item_price
print(f"і всього вартість замовлення буде становити {total} {currency}", end="\n\n")


# task 09
"""
Ігор займається фотографією. Він вирішив зібрати всі свої 232
фотографії та вклеїти в альбом. На одній сторінці може бути
розміщено щонайбільше 8 фото. Скільки сторінок знадобиться
Ігорю, щоб вклеїти всі фото?
"""
photos_amount = 232
amount_per_page = 8
if photos_amount % amount_per_page == 0:
    pages = int(photos_amount / amount_per_page)
else:
    pages = int(photos_amount // amount_per_page) + 1

print(f"Ігорю знадобиться {pages} сторінок в альбомі для всіх його фотографій", end="\n\n")


# task 10
"""
Родина зібралася в автомобільну подорож із Харкова в Буда-
пешт. Відстань між цими містами становить 1600 км. Відомо,
що на кожні 100 км необхідно 9 літрів бензину. Місткість баку
становить 48 літрів.
1) Скільки літрів бензину знадобиться для такої подорожі?
2) Скільки щонайменше разів родині необхідно заїхати на зап-
равку під час цієї подорожі, кожного разу заправляючи пов-
ний бак?
"""
total_distance = 1600
fuel_distance = 100
fuel_consumption = 9
tank_capacity = 48

total_fuel_litres = int(total_distance / fuel_distance * fuel_consumption)

km_on_one_tank = tank_capacity / fuel_consumption * fuel_distance
pit_stops = int(total_distance / km_on_one_tank)
if total_distance % km_on_one_tank:
    pit_stops += 1

print(f"Для того щоб доїхати з Харькова до Будапешту необхідно {total_fuel_litres} літрів бензину. "
      f"Для цього родині потрібно зупинитися {pit_stops} разів, заправляючи поаний бак.")
