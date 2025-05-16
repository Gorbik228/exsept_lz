import pandas as pd

class Obrabotka:
    def __init__(self,filename):
        self.filename = filename
        try:
            self.df = pd.read_csv(filename)
        except FileNotFoundError:
            print('Возникла следующая ошибка: Отсутствует файл: ', self.filename)
            raise SystemExit()
        except pd.errors.EmptyDataError:
            print('Возникла следующая ошибка : Пустой файл')
            raise SystemExit()
        except pd.errors.ParserError:
            print('Возникла следующая ошибка : Структура датафрейма не соответсвует')
            raise SystemExit()    
            