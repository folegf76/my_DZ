#1. Напишіть регулярний вираз, який знаходитиме в тексті фрагменти, що складаються з однієї літери R, за якою слідує
# одна або більше літер b, за якою одна r. Враховувати верхній та нижній регістр.
import re


def my_pattern1(text):
    pattern = r'(Rb+r)'
    return re.findall(pattern, text)


print(my_pattern1("dsgg rgRbrlhihRbbbr jgrbbrugku"))

#2. Напишіть функцію, яка виконує валідацію номера банківської картки (9999-9999-9999-9999).
import re


def my_pattern2(text):
    pattern = r'^(\d{4}-\d{4}-\d{4}-\d{4})$'
    return True if re.search(pattern, text) else False


print(my_pattern2("3279-3769-6547-6655"))

#3. Напишіть функцію, яка приймає рядкові дані та виконує перевірку на їхню відповідність мейлу. Вимоги: -Цифри (0-9).
# -лише латинські літери у великому (A-Z) та малому (a-z) регістрах. -у тілі мейла допустимі лише символи "_" і "-".
# Але вони не можуть бути першим символом мейлу. -Символ "-" не може повторюватися.
import re


def my_pattern3(text):
    pattern = r'^[0-9A-Za-z](-?[0-9A-Za-z_])+@[0-9A-Za-z](-?[0-9A-Za-z._])+$'
    return True if re.search(pattern, text) else False


print(my_pattern3('Oleh-_7@gmail.com'))



#4. Напишіть функцію, яка перевіряє правильність логіну. Правильний логін – рядок від 2 до 10 символів, що містить
# лише літери та цифри.
import re


def my_pattern4(text):
    pattern = r'^[a-zA-Z0-9]{2,10}$'
    return True if re.search(pattern, text) else False


print(my_pattern4("54546cHfh"))
