import datetime
c=[]
class Person:
    def __init__(self, name ):
        self.name=name

    def items(self ,a):
        for i in range(a):
          x={'item':input() , 'price':int(input()) ,'time': datetime.datetime.strptime(input(),"%Y-%m-%d"), 'name':input()}
          c.append(x)

    def person_expense_in_year(self ,y):
        k=0
        for i in c:
            if self.name==i['name'] and  i['time'].year==y:
               k+=i['price']

        print(f'{self.name} expensive in year {y} is {k}')
    def person_expense_in_month(self,y,m):
        n=0
        for i in c:
            if self.name==i['name'] and  i['time'].year==y and   i['time'].month==m:
                  n+=i['price']
        print(f'{self.name} expensive in {m} month is {n}')

    def person_expense_in_day(self ,y ,m, d):
        b=0
        for i in c:
            if self.name==i['name'] and  i['time'].year==y  and i['time'].month==m and  i['time'].day==d:
                  b+=i['price']
        print(f'{self.name}  expensive in {d} day  is {b}')




l=Person(input())
l.items(int(input()))
l. person_expense_in_year(int(input()))
l.person_expense_in_month(int(input()), int(input()))
l.person_expense_in_day(int(input()),int(input()),int(input()))



