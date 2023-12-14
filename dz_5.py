import random

print("Сегодня мы потренируемся расшифровывать азбуку Морзе")
input("Нажмите Enter и начнем")

words = ['home', 'help', 'finish', 'hello']
answers = []
MORSE_CODES = {
    "0": "-----",
    "1": ".----",
    "2": "..---",
    "3": "...--",
    "4": "....-",
    "5": ".....",
    "6": "-....",
    "7": "--...",
    "8": "---..",
    "9": "----.",
    "a": ".-",
    "b": "-...",
    "c": "-.-.",
    "d": "-..",
    "e": ".",
    "f": "..-.",
    "g": "--.",
    "h": "....",
    "i": "..",
    "j": ".---",
    "k": "-.-",
    "l": ".-..",
    "m": "--",
    "n": "-.",
    "o": "---",
    "p": ".--.",
    "q": "--.-",
    "r": ".-.",
    "s": "...",
    "t": "-",
    "u": "..-",
    "v": "...-",
    "w": ".--",
    "x": "-..-",
    "y": "-.--",
    "z": "--..",
    ".": ".-.-.-",
    ",": "--..--",
    "?": "..--..",
    "!": "-.-.--",
    "-": "-....-",
    "/": "-..-.",
    "@": ".--.-.",
    "(": "-.--.",
    ")": "-.--.-"
}


def morse_encode(word):
    word_encode = []

    for letter in word:
        word_encode.append(MORSE_CODES.get(letter, ""))

    return ' '.join(word_encode)


def get_word():
    return random.choice(words)


for i in range(1, len(words) + 1):
    current_word = get_word()
    current_encoded = morse_encode(current_word)

    print(f"Слово {i} {current_encoded}")
    user_input = input()

    if user_input.lower() == current_word:
        print(f"Верно, {current_word}!")
        answers.append(True)
    else:
        print(f"Неверно, {current_word}!")
        answers.append(False)


def print_statistic(answer):
    answers_total = len(answer)
    answers_correct = sum(answer)
    answers_incorrect = answers_total - answers_correct

    print(f"Всего ответов: {answers_total}\n"
          f"Верных ответов: {answers_correct}\n"
          f"Неверных ответов: {answers_incorrect}")


print_statistic(answers)
