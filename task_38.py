#Дополнить телефонный справочник возможностью изменения и удаления данных.
#Пользователь также может ввести имя или фамилию, и Вы должны реализовать функционал для изменения и удаления данных

def readfile(filename):
    return open(filename).read().split('\n')
 
def scan(data):
    for i in  data:
        print(i)
        
def search(data):
    flag = 1
    name = input('имя:  ')
    for line in data:
        if name in line:
            flag = 0
            print(line)
    if flag: print('no name given')
    
data = readfile('data.txt')
dict_command = {'1' :  scan, '2' : search}
 
print('''Команды для работы со справочником:
    Просмотр всех записей: 1
    Поиск: 2
    Новая запись: 3
     Удаление записи: 4
     Изменение любого поля: 5 
     Вывод возраста человека: 6 ''')
 
while True:
    command = input('Команда:   ')
    if command in dict_command:
        dict_command[command](data)
    else:
        print('error!')

