import pandas as pd
import numpy as np


chat_id = 1612072510 # Ваш chat ID, не меняйте название переменной

def solution(x_success: int, 
             x_cnt: int, 
             y_success: int, 
             y_cnt: int) -> bool:
    # Измените код этой функции
    # Это будет вашим решением
    # Не меняйте название функции и её аргументы
    tmp = ((x_success+y_success) * y_cnt)/(x_cnt+y_cnt)
    sqr = (y_success - tmp)**2/tmp
    if sqr < 6.63:
        return False
    else:
        return True
#return ... # Ваш ответ, True или False
