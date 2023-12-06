import os
from Parsing_html import func
import Parsing_html

# Vars
reviews_folder = (os.environ['USERPROFILE']) + "\\Desktop\\Reviews\\"
html_files_folder = (reviews_folder + "html files\\")
# Checking
check = os.path.exists(html_files_folder)
if check == False:
    os.makedirs(html_files_folder)
    input("Сохраните html файлы и поместите их в папку \"\\Reviews\\"
    "html files\\\" на рабочем столе.\n(Папка была только что создана)")
    exit()
first_check = os.path.exists(html_files_folder + "ReviewsFile1.html")
if first_check == False:
    input("В папке \"html files\" не найдено ни одного файла html, "
    "сохраните файлы в формате: \n\"ReviewsFile1.html\", \"ReviewsFile2.html\" и так далее.")
    exit()
# Parsing
stop_name = input("Введите имя пользователя на котором нужно остановиться: ")
result = open(reviews_folder + 'result.txt', 'w', encoding="utf-8")
result.close()
i = 1
while str(i):
    check = os.path.exists(html_files_folder + "ReviewsFile" + str(i) + ".html")
    if check:
        print("Сбор отзывов из файла ReviewsFile" + str(i) + ".html")
        html_page = open(html_files_folder + "ReviewsFile" + str(i) + ".html", "r", encoding="utf-8")
        html_code = html_page.read()
        html_page.close()
        func()
        if Parsing_html.name_in_cycle == stop_name:
            break
        else:
            i = i + 1
    else:
        break
print("Отзывы собраны в файле \"result.txt\"")