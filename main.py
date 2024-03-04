import os
import datetime


current_day = datetime.date.today().weekday()

links = ['https://colab.research.google.com/', 'https://www.youtube.com/@SeanStudy/videos',
         'https://www.youtube.com/', 'https://www.blackbox.ai/',
         'https://www.pythonanywhere.com/user/Aboba8432/',
         'https://github.com/Vova2808', 'https://leetcode.com/Vova_3000/',
         'https://seanprashad.com/leetcode-patterns/', "https://py.checkio.org/"]

if current_day == 0:
    os.system('explorer "E:\Kurs\[Udemy] Gleb Mikhaylov - SQL для Анализа Данных с Глебом Михайловым (2021)"')
    os.system('explorer  "E:\Kurs\[Глеб Михайлов] А Б-тесты с Глебом Михайловым (2023)"')
    os.system("start https://www.odin.study/ru/Chat/2058270")
    for _ in links:
        os.system("start " + str(_))
    print("Понедельник")
    os.system(r'cd "C:\Program Files\JetBrains\PyCharm Community Edition 2023.2\bin" & pycharm64.exe & exit')



elif current_day == 1:
    os.system('explorer "E:\Kurs\[Udemy] Gleb Mikhaylov - SQL для Анализа Данных с Глебом Михайловым (2021)"')
    os.system('explorer  "E:\Kurs\[Глеб Михайлов] А Б-тесты с Глебом Михайловым (2023)"')
    for _ in links:
        os.system("start "+ str(_))
    print("Вторник")
    os.system(r'cd "C:\Program Files\JetBrains\PyCharm Community Edition 2023.2\bin" & pycharm64.exe & exit')
    os.system("start https://www.odin.study/ru/Chat/2058270")


elif current_day == 2:
    os.system('explorer "E:\Kurs\[Udemy] Gleb Mikhaylov - SQL для Анализа Данных с Глебом Михайловым (2021)"')
    os.system('explorer  "E:\Kurs\[Глеб Михайлов] А Б-тесты с Глебом Михайловым (2023)"')
    os.system("start https://www.odin.study/ru/Chat/2058270")
    for _ in links:
        os.system("start "+ str(_))
    print("Среда")
    os.system(r'cd "C:\Program Files\JetBrains\PyCharm Community Edition 2023.2\bin" & pycharm64.exe & exit')





elif current_day == 3:
    os.system('explorer "E:\Kurs\[Udemy] Gleb Mikhaylov - SQL для Анализа Данных с Глебом Михайловым (2021)"')
    os.system('explorer  "E:\Kurs\[Глеб Михайлов] А Б-тесты с Глебом Михайловым (2023)"')
    for _ in links:
        os.system("start "+ str(_))
    print("Четверг")
    os.system(r'cd "C:\Program Files\JetBrains\PyCharm Community Edition 2023.2\bin" & pycharm64.exe & exit')




elif current_day == 4:
    os.system('explorer "E:\Kurs\[Udemy] Gleb Mikhaylov - SQL для Анализа Данных с Глебом Михайловым (2021)"')
    os.system('explorer  "E:\Kurs\[Глеб Михайлов] А Б-тесты с Глебом Михайловым (2023)"')
    os.system("start https://www.odin.study/ru/Chat/2058270")
    for _ in links:
        os.system("start "+ str(_))
    print("Пятница")
    os.system(r'cd "C:\Program Files\JetBrains\PyCharm Community Edition 2023.2\bin" & pycharm64.exe & exit')



elif current_day == 5:
    for _ in links:
        os.system("start " + str(_))
    print("Суббота")
    os.system('explorer "E:\Kurs\[Udemy] Gleb Mikhaylov - SQL для Анализа Данных с Глебом Михайловым (2021)"')
    os.system('explorer  "E:\Kurs\[Глеб Михайлов] А Б-тесты с Глебом Михайловым (2023)"')
    os.system(r'cd "C:\Program Files\JetBrains\PyCharm Community Edition 2023.2\bin" & pycharm64.exe & exit')

else:
    os.system('explorer "E:\Kurs\[Udemy] Gleb Mikhaylov - SQL для Анализа Данных с Глебом Михайловым (2021)"')
    os.system('explorer  "E:\Kurs\[Глеб Михайлов] А Б-тесты с Глебом Михайловым (2023)"')
    for _ in links:
        os.system("start " + str(_))
    print("Воскресенье")
    os.system(r'cd "C:\Program Files\JetBrains\PyCharm Community Edition 2023.2\bin" & pycharm64.exe & exit')
