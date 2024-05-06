import random 

def random_serch(boxs: list[int]) -> bool:
    """_summary_ 
        реализация условия без какой либо стратегии, заключенные выбирают коробки рандомно.
    Args:
        boxs (list[int]): Принимает список перемешаных целых чисел, индексы списка номер коробки, элемент списка это номер заключеного в этой коробке.

    Returns:
        bool: Возвращяет статус успеха поиска своих номеров если все нашли свои номера возвращается True в противном случае False.
    """
    
    result = 0 #счетчик удачных нахождей своего номера
    
    for id_man in range(100): # перебераем номера заключеных
        for _ in range(50): 
            rand_id_box = random.randint(0,99) # заключеный рандомно выберает номер коробки
            if id_man == boxs[rand_id_box]:    # если номер в коробке совпадает с его то-
                result += 1                    # увеличиваем счетчик на 1
                break
            
    if result == 100:    # проверяем что все нашли свой номер
        return True
    else:
        return False
        
def strategy_serch(boxs: list[int]) -> bool:
    """_summary_
        реализована стратегия выбора коробки со своим номером, если там не его номер то пойти к коробке с доставшимся номером из прошлой коробки, так до конца попыток.
    Args:
        boxs (list[int]): Принимает список перемешаных целых чисел, индексы списка номер коробки, элемент списка это номер заключеного в этой коробке.

    Returns:
        bool: Возвращяет статус успеха поиска своих номеров если все нашли свои номера возвращается True в противном случае False.
    """
    result = 0 #счетчик удачных нахождей своего номера
    
    for id_man in range(100): # перебераем номера заключеных
        
        id_box = boxs[id_man] # выберает коробку со своим номером
        for _ in range(49):
            if id_box == id_man:    # если номер в коробке совпадает с его то-
                result += 1         # увеличиваем счетчик на 1
                break
            id_box = boxs[id_box]  #обновляем номер будущей короби

    if result == 100:  # проверяем что все нашли свой номер
        return True
    else:
        return False
        
        
def test_serch(func,iter=50):
    value = 0
    
    for _ in range(iter):
        
        box = list(range(100))
        random.shuffle(box)
        
        if func(box):
            value += 1
    return value / iter

coef_rand = test_serch(random_serch,iter=1000)
print(f"Без использования какой либо стратегии и выборе коробок на угад то шанс составляет: {round(coef_rand * 100,1)}%")

coef_strateg = test_serch(strategy_serch,iter=1000)
print(f"При использовании стратегии из видео шанс составляет: {round(coef_strateg * 100,1)}%")