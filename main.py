# Викторина
# Игра на выбор правильного варианта ответа,
# вопросы, которой читаются из текстового файла
import sys
def open_file(file_name, mode):
    """Открывает файл."""
    try:
        the_file = open(file_name, mode, encoding='utf-8')
    except IOError as e:
        print("Невозможно открыть файл", file_name, ". Работа программы будет завершена.\n", e)
        input("\n\nНажмите Enter, чтобы выйти.")
        sys.exit()
    else:
        return the_file
# Функция принимает файловый объект и возвращает очередную строку текста из него
def next_line(the_file):
    """Возвращает в отформатированном виде очередную строку игрового файла"""
    line = the_file.readline()
    line = line.replace("/", "\n")
    return line
# Функция принимает файловый объект и возвращает 4 строки:
# (тема вопроса, текст вопроса, правильный ответ, комментарий),
# а так же список (4 строки - возможные ответы на вопрос)
def next_block(the_file):
    """Возвращает очередной блок данных из игрового файла"""
    category = next_line(the_file)
    question = next_line(the_file)
    answers = []
    for i in range(4):
        answers.append(next_line(the_file))
    correct = next_line(the_file)
    if correct:
        correct = correct[0]
        explanation = next_line(the_file)
        return category, question, answers, correct, explanation
# Функция приветсвует и объявляет название эпизода (это наша первая строка)
def welcome(title):
    """Приветствует игрока и сообщает тему игры"""
    print("\t\tДобро пожаловать в игру 'Викторина'!\n")
    print("\t\t", title, "\n")
# Ф-ия main() отвечает за основную часть игрового процесса.
# Это настройка игры
def main():
    trivia_file = open_file("trivia.txt", "r")
    title = next_line(trivia_file)
    welcome(title)
    score = 0 # счёт = 0
# Извлечение первого блока
    category, question, answers, correct, explanation = next_block(trivia_file)
    while category:
    #вывод вопроса на экран
        print(category)
        print(question)
        for i in range(4):
            print("\t", i + 1, "-", answers[i])
# Получение ответа
        answer = input("Ваш ответ: ")
# Проверка ответа игрока
# Сравниваем ответ игрока с правильным ответом
        if answer == correct:
            print("\nДа!", end=" ")
            score += 1
        else:
            print("\nНет!", end=" ")
            print(explanation)
            print("Счёт:", score, "\n\n")
# Переход к следующему вопросу
        category, question, answers, correct, explanation = next_block(trivia_file)
# После окончания цикла, я закрываю файл 'Викторина.txt' и вывожу результат игрока на экран
# завершении игры
    trivia_file.close()
    print("Это был последний вопрос!")
    print("На вашем счету", score)
# запуск функции main()
main()
input("\n\nНажмите Enter, чтобы выйти.")

