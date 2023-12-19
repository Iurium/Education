import random


def word_from_file():
    with open('words.txt', 'r', encoding='utf-8') as file:
        lines = file.read()
        words = lines.splitlines()

    return words


def shuffle_word(word):
    word_list = list(word)
    random.shuffle(word_list)
    return ''.join(word_list)


def player_score_file(player_name, player_score):
    with open('history.txt', 'a', encoding='utf-8') as file:
        file.write(f"{player_name} {player_score}\n")


def get_statistic_from_file():
    scores = []
    with open('history.txt', 'r', encoding='utf-8') as file:
        for line in file:
            score = line.strip().split(' ')[-1]
            scores.append(score)

    max_score = max(scores)
    len_score = len(scores)

    return {'max': max_score, 'len': len_score}


def main():
    user_score = 0

    print("Введите ваше имя")
    user_name = input()

    words = word_from_file()

    for word in words:
        word_shuffled = shuffle_word(word)
        print(f"Угадайте слово: {word_shuffled}")

        user_input = input()

        if user_input == word:
            print(f"Верно! Вы получаете 10 очков")
            user_score += 10
        else:
            print(f"Неверно! Верный ответ - {word}")

    player_score_file(user_name, user_score)
    stats = get_statistic_from_file()

    print(f"Всего игр сыграно: {stats.get('len')}")
    print(f"Максимальный рекорд: {stats.get('max')}")


main()
