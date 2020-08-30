#work 3
#a = int(input ('введите месяц '))
#if a == 1 or a == 2 or a == 12:
 #   print ('зима')
#elif a == 3 or a == 4 or a == 5:
#    print ('весна')
#elif a == 6 or a == 7 or a == 8:
 #   print ('лето')
#elif a == 9 or a == 10 or a == 11:
#    print ('осень')
#else:
#    print ('ошибосик')




#work 4
my_str = input("Введите предложения с пробелами: ")
a = my_str.split(' ')
for i, el in enumerate(a, 1):
    if len(el) > 10:
        el = el[0:10]
    print(f"{i}. - {el}")

#work 2
my_list = ['1', '2', '3', '4', '5']
if len(my_list) % 2 == 0:
    i = 0
    while i < len(my_list):
        el = my_list[i]
        my_list[i] = my_list[i+1]
        my_list[i+1] = el
        i += 2
else:
    i = 0
    while i < len(my_list) - 1:
        el = my_list[i]
        my_list[i] = my_list[i + 1]
        my_list[i + 1] = el
        i += 2
print(my_list)