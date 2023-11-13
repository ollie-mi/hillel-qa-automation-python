# task 01 == Виправте синтаксичні помилки
print("Hello", end=" ")
print("world!")

# task 02 == Виправте синтаксичні помилки
hello = "Hello"
world = "world"
if True:
    print(f"{hello} {world}!")

# task 03  == Вcтавте пропущену змінну у ф-цію print
for letter in "Hello world!":
    print(letter)

# task 04 == Зробіть так, щоб кількість бананів була
# завжди в чотири рази більша, ніж яблук
apples = 2
banana = apples * 4

# task 05 == виправте назви змінних
side_1 = 1
side_2 = 2
side_3 = 3
side_4 = 4

# task 06 == Порахуйте периметр фігури з task 05
# та виведіть його для користувача
perimetery = side_1 + side_2 + side_3 + side_4
print(perimetery)


"""
    # Задачі 07 -10:
    # Переведіть задачі з книги "Математика, 2 клас"
    # на мову пітон і виведіть відповідь, так, щоб було
    # зрозуміло дитині, що навчається в другому класі
"""
# task 07
"""
У саду посадили 4 яблуні. Груш на 5 більше яблунь, а слив - на 2 менше.
Скільки всього дерев посадили в саду?
"""
apples = 4
pears = apples + 5
plums = apples - 2
all_trees = apples + pears + plums
print(f"There are {apples} apples, {pears} pears, {plums} plums in the garden. "
      f"And if we count all the trees the result will be {all_trees} trees in the garden")

# task 08
"""
До обіда температура повітря була на 5 градусів вище нуля.
Після обіду температура опустилася на 10 градусів.
Надвечір потепліло на 4 градуси. Яка температура надвечір?
"""
morning_temperature = 5
day_temperature = morning_temperature - 10
evening_temperature = day_temperature + 4
print(f"It's {evening_temperature} degrees in the evening today")

# task 09
"""
Взагалі у театральному гуртку - 24 хлопчики, а дівчаток - вдвічі менше.
1 хлопчик захворів та 2 дівчинки не прийшли сьогодні.
Скількі сьогодні дітей у театральному гуртку?
"""
boys = 24
girls = int(boys / 2)
sick_boys = 1
absent_girls = 2
boys_today = boys - sick_boys
girls_today = girls - absent_girls
children_in_class = boys_today + girls_today
print(f"There are {children_in_class} children in the class today: {boys_today} boys and {girls_today} girls")

# task 10
"""
Перша книжка коштує 8 грн., друга - на 2 грн. дороже,
а третя - як половина вартості першої та другої разом.
Скільки будуть коштувати усі книги, якщо купити по одному примірнику?
"""
currency = "UAH"
book_price_1 = 8
book_price_2 = book_price_1 + 2
book_price_3 = int((book_price_1 + book_price_2) / 2)
book_total_price = book_price_1 + book_price_2 + book_price_3
print(f"Price for the first book is {book_price_1} {currency}, price for the second book is {book_price_2} {currency} "
      f"and price for the third book is {book_price_3} {currency}. "
      f"If to buy one of each book the total price will be {book_total_price} {currency}")
