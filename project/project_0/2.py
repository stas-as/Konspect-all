line = "("
from collections import *

def brackets(line):
    stec = deque()
    if len(line) == 0:
        return False
    for i in line:
        if i == "(":
            stec.append(i)
        elif i == ")":
            stec.pop()
    if len(stec) == 0:
        return True
    else:
        return False
    
    
#print(brackets(line))


ratings = [('Old York', 3.3), ('New Age', 4.6), ('Old Gold', 3.3), ('General Foods', 4.8),
          ('Belissimo', 4.5), ('CakeAndCoffee', 4.2), ('CakeOClock', 4.2), ('CakeTime', 4.1),
          ('WokToWork', 4.9), ('WokAndRice', 4.9), ('Old Wine Cellar', 3.3), ('Nice Cakes', 3.9)]
# Отсортируйте список ratings по убыванию рейтинга. Для кафе
# с одинаковым рейтингом отсортируйте кортежи по названию.
ratings.sort(key=lambda x: (-x[1], x[0]))
# Сохраните данные с рейтингом в словарь cafes, где ключами являются
# названия кафе, а значениями - их рейтинг.
from collections import OrderedDict
cafes = OrderedDict(ratings)
print(type(ratings))
print(cafes)
from collections import *
tasks = [(36871, 'office', False),
(40690, 'office', False),
(35364, 'voltage', False),
(41667, 'voltage', True),
(33850, 'office', False)]

def task_manager(task):
    servers = defaultdict(deque)
    for task in tasks:
        if tasks[-1]:
            servers[tasks[1]].appendleft(tasks[0])
        else:
            servers[tasks[1]].append(tasks[0])
    return servers
print(task_manager(tasks))
# defaultdict(, {'voltage': deque([41667, 35364]),q
# 'office': deque([36871, 40690, 33850])})
