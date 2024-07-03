import requests
from bs4 import BeautifulSoup
from googletrans import Translator

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

# Функция для перевода текста
def translate_text(text, dest_lang):
    translator = Translator()
    translation = translator.translate(text, dest=dest_lang)
    return translation.text

def word_game():
    print("Добро пожаловать в игру 'Слова'")
    while True:
        word_dict = get_english_words()
        if word_dict is None:
            continue
        word = word_dict.get("english_words")
        word_definition = word_dict.get("word_definition")

# Переводим определение на русский
        word_definition_ru = translate_text(word_definition, "ru")
        word_ru = translate_text(word, "ru")

        print(f"Значение слова на английском языке: {word_definition}")
        print(f"Значение слова на русском языке: {word_definition_ru}")
        user_input = input("Угадай слово на английском: ").strip().lower()


        if user_input == word:
            print(f"Правильно! Вот ваше слово: {word}")
#            break
        else:
            print(f"Неправильно. Попробуй угадать слово на русском ")
            user_input_ru = input("Слово на русском: ").strip().lower()
            translated_guess_en = translate_text(user_input_ru, "en")

            if translated_guess_en == word:
                print(f"Правильно! Вот ваше слово: {word}")
            else:
                print(f"Неправильно. Было загадано слово: {word}, {word_ru}")

        play_again = input("Хотите сыграть еще раз? (y/n): ")
        if play_again.lower() != "y":

            print("Спасибо за игру!")
            break

word_game()


