#задание 1
import time


def time_it(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        func(args[0])
        print(time.time() - start_time)
    return wrapper


@time_it
def test_list(n):
    list_obj = []
    for i in range(n):
        list_obj.append(i)
        list_obj.index(i)
    return list_obj
#быстрее обрабатываются списки, но это может быть из-за оперативки компа? Потому что запускал много раз и только 3 значения
#были чуть разные

@time_it
def test_dict(n):
    dict_obj = dict()
    for i in range(n):
        dict_obj[i] = i
        dict_obj.get(i)
    return dict_obj


test_list(1000)
test_dict(1000)

#задание 2

from uuid import uuid4
import hashlib

salt = uuid4().hex  # -> <class 'str'> - 8d43a764ef0f4c059fa40af85d8e2923

# я не понимаю, для чего мы должны переводить в строчку, не монятен смысл этого задания. Каюсь, скопипастил
def get_hash(passwd_obj):
    return hashlib.sha256(salt.encode() + passwd_obj.encode()).hexdigest()


def hash_check(hashed_password, user_password):
    return hashed_password == hashlib.sha256(salt.encode() + user_password.encode()).hexdigest()


new_passwd = input('Введите пароль: ')
hash_obj = get_hash(new_passwd)
print(f'В базе данных хранится строка: {hash_obj}')

old_pass = input('Введите пароль еще раз для проверки: ')

if hash_check(hash_obj, old_pass):
    print('Вы ввели правильный пароль')
else:
    print('Внимание! Пароли не совпадают')

# 3 задание

s = input("Введите строку из английских букв: ")
r = set()

N = len(s)
for i in range(N):
    if i == 10:
        N = len(s) - 1
    else:
        N = len(s)
    for j in range(N, i, -1):
        print(s[i:j])

        r.add(hashlib.sha1(s[i:j].encode('utf-8')).hexdigest())
print(r)


print("Количество различных подстрок в строке '%s' равно %d" % (s, len(r)))
