"""
Домашнее задание №2

Работа с файлами


1. Скачайте файл по ссылке https://www.dropbox.com/s/sipsmqpw1gwzd37/referat.txt?dl=0
2. Прочитайте содержимое файла в перменную, подсчитайте длинну получившейся строки
3. Подсчитайте количество слов в тексте
4. Замените точки в тексте на восклицательные знаки
5. Сохраните результат в файл referat2.txt
"""



def main():
    word_count = 0
    with open('referat.txt', 'r', encoding='utf-8') as file:
        content = (file.read())
        len_file = len(content)
        for line in file:
            word_count += len(line)
        new_content = content.replace('.', '!')    
        print(len_file)
        print(word_count)
        
    with open('referat2.txt', 'w', encoding='utf-8') as file1:
        file1.write(new_content)

        


if __name__ == "__main__":
    main()
