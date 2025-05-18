import pandas as pd

class Obrabotka:
    def __init__(self, csv):
        try:
            self.csv = pd.read_csv(csv)
        except FileNotFoundError:
            print(f'Возникла ошибка: Файла нет')
            raise SystemExit()
        except pd.errors.EmptyDataError:
            print('Возникла ошибка: Файл пустой')
            raise SystemExit()
        except:
            print('Возникла ошибка: Где файл?')
            raise SystemExit()
        try:
            a = self.csv.columns.to_list()
            self.df_o = pd.read_csv('var1.csv')
            b = self.df_o.columns.to_list()
            if a != b:
                raise TypeError 
        except TypeError:
            print('Возникла ошибка: колонки не то пальто')
        try:
            self.f_t = str(self.csv.dtypes)
            self.o_t = str(self.df_o.dtypes)
            if self.f_t != self.o_t:
                raise TypeError('Неверные типы данных')
            else:
                print('Все хорошо')
        except TypeError:
            print(f'Файлы не совпадают, ожидалось: {self.o_t}, есть:{self.f_t} ')


def main():
    csv = 'var1_lox.csv'            
    df = Obrabotka(csv)

if __name__ == "__main__":
    main()

        
        
        
        