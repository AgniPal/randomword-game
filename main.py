import requests
from bs4 import BeautifulSoup

#Создаём функцию, которая будет получать информацию
def get_english_words():
   url = "https://randomword.com/"
   try:
       response = requests.get(url)

#Создаём объект Soup
       soup = BeautifulSoup(response.content, "html.parser")
       #Получаем слово. text.strip удаляет все пробелы из результата
       english_words = soup.find("div", id="random_word").text.strip()
       #Получаем описание слова
       word_definition = soup.find("div", id="random_word_definition").text.strip()

       #Чтобы программа возвращала словарь
       return {
           "english_words": english_words,
           "word_definition": word_definition
       }
   except:
       print("Что-то пошло не так")
       return None


def word_game():
    print("Добро пожаловать в игру 'Слова'")
    while True:
        word_dict = get_english_words()
        word = word_dict.get("english_words")
        word_definition = word_dict.get("word_definition")

        print(f"Значение слова: {word_definition}")
        user_input = input("Слово: ").lower()

        if user_input == word:
            print(f"Правильно! Вот ваше слово: {word}")
#            break
        else:
            print(f"Неправильно. Было загадано: {word}")

        play_again = input("Хотите сыграть еще раз? (y/n): ")
        if play_again.lower() != "y":

            print("Спасибо за игру!")
            break

word_game()


