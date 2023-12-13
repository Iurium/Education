easy = {
    'home': 'дом',
    'name': 'имя',
    'sun': 'солнце',
    'apple':'яблоко',
    'fun': 'веселье',
}

medium = {
    'tree': 'дерево',
    'beach': 'пляж',
    'like': 'нравится',
    'love': 'любовь',
    'success': 'успех'
}

hard = {
    'amazing': 'удивительный',
    'popular': 'популярный',
    'people': 'люди',
    'national': 'национальный',
    'special': 'особенный',
}

levels = {
    0: 'Нулевой',
    1: 'Так себе',
    2: 'Можно лучше',
    3: 'Норм',
    4: 'Хорошо',
    5: 'Отлично',
}


answer = {}


user_level = input('Выберите уровень сложности\nлегкий, средний, сложный: \n')
if user_level == 'легкий':
    words = easy
elif user_level == 'средний':
    words = medium
elif user_level == 'сложный':
    words = hard
else:
    print('Нет такого уровня сложности')

print(f'Выбран уровень сложности {user_level}')

words_count = len(words)
print(f'Мы предложим {words_count} слов, подберите перевод')

for word_en, word_ru in words.items():
    print(input('Нажмите Enter'))

    letters_count = len(word_ru)
    letters_first = word_ru[0]

    print(f'{word_en}, {letters_count} букв, начинается на {letters_first}...')

    user_answer = input('Введите ваш ответ: ').lower()
    if user_answer == word_ru:
        print(f'Верно, {word_en.title()} это {word_ru}')
        answer[word_en] = True
    else:
        print(f'Неверно. {word_en.title()} это {word_ru}')
        answer[word_en] = False

correct_words = []
incorrect_words = []

for word_en, is_correct in answer.items():
    if is_correct:
        correct_words.append(word_en)
    else:
        incorrect_words.append(word_en)

print('Правильное отвечены слова:')
print('\n'.join(correct_words))
print()
print('Неправильно отвечены слова:')
print('\n'.join(incorrect_words))

correct_count = len(correct_words)
user_level = levels[correct_count]

print()
print('Ваш ранг:')
print(f'{user_level}')