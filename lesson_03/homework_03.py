adwentures_of_tom_sawer = """\
Tom gave up the brush with reluctance in his .... face but alacrity
in his heart. And while
the late steamer
"Big Missouri" worked ....
and sweated
in the sun,
the retired artist sat on a barrel in the .... shade close by, dangled his legs,
munched his apple, and planned the slaughter of more innocents.
There was no lack of material;
boys happened along every little while;
they came to jeer, but .... remained to whitewash. ....
By the time Ben was fagged out, Tom had traded the next chance to Billy Fisher for
a kite, in good repair;
and when he played
out, Johnny Miller bought
in for a dead rat and a string to swing it with—and so on, and so on,
hour after hour. And when the middle of the afternoon came, from being a
poor poverty, stricken boy in the .... morning, Tom was literally
rolling in wealth."""

# task 01 ==
""" Дані у строці adwentures_of_tom_sawer розбиті випадковим чином, через помилку.
треба замінити кінець абзацу на пробіл .replace("\n", " ")"""

adwentures_of_tom_sawer = adwentures_of_tom_sawer.replace('\n', ' ')
print(adwentures_of_tom_sawer, end='\n\n')

# task 02 ==
""" Замініть .... на пробіл
"""

adwentures_of_tom_sawer = adwentures_of_tom_sawer.replace('....', ' ')
print(adwentures_of_tom_sawer, end='\n\n')

# task 03 ==
""" Зробіть так, щоб у тексті було не більше одного пробілу між словами.
"""

string_list = adwentures_of_tom_sawer.split()
adwentures_of_tom_sawer = ' '.join(string_list)
print(adwentures_of_tom_sawer, end='\n\n')

# task 04
""" Виведіть, скількі разів у тексті зустрічається літера "h"
"""

print(f"Кількість літер h в тексті: {adwentures_of_tom_sawer.lower().count('h')}", end='\n\n')

# task 05
""" Виведіть, скільки слів у тексті починається з Великої літери?
"""

symbol_list = ["'", "\""]
count = 0
for word in adwentures_of_tom_sawer.split():
    if word[0].isupper() or (word[0] in symbol_list and word[1].isupper()):
        count += 1

print(f"Кількість слів, що починаються з великої літери: {count}", end='\n\n')


# task 06
""" Виведіть позицію, на якій слово Tom зустрічається вдруге
"""

start = adwentures_of_tom_sawer.find('Tom')
print(f"Вдруге слово Tom зустрічається на позиції {adwentures_of_tom_sawer.find('Tom', start+1)}", end='\n\n')


# task 07
""" Розділіть змінну adwentures_of_tom_sawer по кінцю речення.
Збережіть результат у змінній adwentures_of_tom_sawer_sentences
"""

adwentures_of_tom_sawer_sentences = adwentures_of_tom_sawer.split('. ')

# task 08
""" Виведіть четверте речення з adwentures_of_tom_sawer_sentences.
Перетворіть рядок у нижній регістр.
"""

print(adwentures_of_tom_sawer_sentences[3].lower(), end="\n\n")

# task 09
""" Перевірте чи починається якесь речення з "By the time".
"""

for sentence in adwentures_of_tom_sawer_sentences:
    if sentence.startswith('By the time'):
        print(f"Речення, яке починається з 'By the time': {sentence}", end='\n\n')

# task 10
""" Виведіть кількість слів останнього речення з adwentures_of_tom_sawer_sentences.
"""

print(f"Кількість слів в останньому речені: {len(adwentures_of_tom_sawer_sentences[-1].split())}")
