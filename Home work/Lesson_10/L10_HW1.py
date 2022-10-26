import math
class Triangle:

    def __init__(self, side_a, side_b, side_c):
        '''
        Отримує данні трикутника
        :param side_a: Приймає данні трикутника сторони a
        :param side_b: Приймає данні трикутника сторони b
        :param side_c: Приймає данні трикутника сторони c
        '''
        self.side_a = float(side_a)
        self.side_b = float(side_b)
        self.side_c = float(side_c)


    def exists(self):
        '''
        Вираховує чи такий трикутник існує
        :return: повертає результат
        '''
        if self.side_a > (self.side_b + self.side_c) or self.side_b > (self.side_a + self.side_c) or self.side_c > (self.side_a + self.side_b):
            x = 'Існування такого трикутника в Евклідовому просторі не можливе'
        else:
            x = 'Існування такого трикутника в Евклідовому просторі можливе'
        return x


    def perimetr(self):
        '''
        Вираховує периметр трикутника, якщо він існує
        :return: Повертає периметр трикутника якщо він існує
        :return: Відповідь, що його не існує
        '''
        if self.exists() == 'Існування такого трикутника в Евклідовому просторі можливе':
            perimetr_x = self.side_a + self.side_b + self.side_c
            return perimetr_x
        else:
            return 'У трикутника який не існує не може бути периметру!'


    def squere(self):
        '''
        Вираховує площу трикутника, якщо він існує
        :return: Повертає площу трикутника якщо він існує
        :return: відповідь, що його не існує
        '''
        if self.exists() == 'Існування такого трикутника в Евклідовому просторі можливе':
            p = self.perimetr()/2
            s = math.sqrt(p*(p-self.side_a)*(p-self.side_b)*(p-self.side_c))
            return round(s,2)
        else:
            return 'У трикутника який не існує не може бути площі!'


    def __str__(self):
        '''
        Виводить інформацію про трикутник
        :return: повертає інформацію про трикутник якщо він існує
        :return: відповідь, що його не існує
        '''
        if self.exists() == 'Існування такого трикутника в Евклідовому просторі можливе':
            return f'{self.exists()}\nПериметр трикутника становить {self.perimetr()} та площа {self.squere()}'
        else:
            return self.exists()



if __name__ == '__main__':


    while True:
        a = input('Число a -> ')
        b = input('Число b -> ')
        c = input('Число c -> ')
        if a.isnumeric() and b.isnumeric() and c.isnumeric():
            triangle_x = Triangle(side_a=a, side_b=b, side_c=c)
            break
        else:
            print('Вкажіть число')


    print(triangle_x)
    print(triangle_x.exists())
    print(triangle_x.perimetr())
    print(triangle_x.squere())