#!/usr/bin/env python
# coding: utf-8

# ### Инкапсуляция
# 
# Инкапсуляция заключается в том, что данные скрыты за пределами определения объекта. Это позволяет разработчикам создавать удобный интерфейс взаимодействия и защитить данные от внешних источников.

# In[ ]:


class Person:
    
    def __init__(self, name, gender, height=0, weight=0, hands=2):
        self.name = name
        self.gender = gender
        self.height = height
        self.weight = weight
        self.weapons = []
        self.hands = hands
    
    def eat(self, food):
        self.weight += food
    
    def do_exercise(self, hours):
        self.weight -= hours * 0.2
    
    def change_alias(self, new_alias):
        print(self) 
        self.alias = new_alias

    def beat_up(self, foe):
        if not isinstance(foe, Person):
            return
        foe.status = 'defeated'
        self.status = 'winner'
    


# Реализуем защищенную переменную и метод

# In[1]:


class Person:
    
    def __init__(self, name, gender, height=0, weight=0, hands=2):
        self.name = name
        self.gender = gender
        self.height = height
        self.weight = weight
        self.weapons = []
        self.hands = hands
        self._alias = 'No alias' # определяем, что псевдоним должен protected
    
    def eat(self, food):
        self.weight += food
    
    def do_exercise(self, hours):
        self.weight -= hours * 0.2
    # определяем, что изменение псевдонима тоже будет protected методом
    def change_alias(self, new_alias):
        self._alias = new_alias

    def beat_up(self, foe):
        if not isinstance(foe, Person):
            return
        foe.status = 'defeated'
        self.status = 'winner'

peter = Person('Peter Parker', 'Male', 175, 70)
print(peter._alias)
peter._change_alias('Spider-Man')
print(peter._alias)


# На самом деле, технические для интерпретатора это не имеет никакого значения. Это просто соглашение, согласно которому, такие атрибуты и методы не стоит использовать за рамками класса и дочерних классов.

# Двойное подчеркивание в начале имени атрибута/метода дает большую защиту: атрибут становится недоступным по этому имени вне самого класса.

# In[2]:


class Person:
    
    def __init__(self, name, gender, height=0, weight=0, hands=2):
        self.name = name
        self.gender = gender
        self.height = height
        self.weight = weight
        self.weapons = []
        self.hands = hands
        self.__alias = 'No alias' # делаем псевдоним приватным
    
    def eat(self, food):
        self.weight += food
    
    def do_exercise(self, hours):
        self.weight -= hours * 0.2
    # делаем изменение псевдонима приватным методом
    def __change_alias(self, new_alias): 
        self.__alias = new_alias

    def beat_up(self, foe):
        if not isinstance(foe, Person):
            return
        foe.status = 'defeated'
        self.status = 'winner'

peter = Person('Peter Parker', 'Male', 175, 70)
print(peter.__alias)
peter.__change_alias('Spider-Man')
print(peter.__alias)


# Но и это можно обойти при помощи прямого указания класса.

# In[3]:


class Human:
    
    def __init__(self, name, gender, height=0, weight=0, hands=2):
        self.name = name
        self.gender = gender
        self.height = height
        self.weight = weight
        self.weapons = []
        self.hands = hands
        self.__alias = 'No alias'
    
    def eat(self, food):
        self.weight += food
    
    def do_exercise(self, hours):
        self.weight -= hours * 0.2
    
    def __change_alias(self, new_alias):
        self.__alias = new_alias

    def beat_up(self, foe):
        if not isinstance(foe, Person):
            return
        foe.status = 'defeated'
        self.status = 'winner'

peter = Human('Peter Parker', 'Male', 175, 70)
print(peter._Human__alias)
peter._Human__change_alias('Spider-Man')
print(peter._Human__alias)


# Таким образом, реализация инкапсуляции в Python носит формальный характер и работает только на уровне соглашения.
# 
# 
# 

# ### Наследование

# In[6]:


# и сращу реализуем множественное наследование!
class Human():
    name = ''
    gender = ''
    height = 0
    weight = 0
    hands = 2

class Spider():
    gender = ''
    height = 0
    weight = 0
    hands = 8   
    
    def webshoot(self):
        print('Pew-Pew!')

        
class SpiderMan(Human, Spider):
    def __init__(self, name, gender):
        self.name = name
        self.gender = gender


peter_parker = SpiderMan('Peter Parker', 'Male')
print(peter_parker.name)
print(peter_parker.gender)
print(peter_parker.height)
print(peter_parker.weight)
print(peter_parker.hands)
peter_parker.webshoot()


# Линераизация способ представления дерева (графа, дерева) в линейную модель (плоскую структуру, список) для определения порядка наследования.

# In[7]:


print(SpiderMan.mro())


# Функция super() позволяет напрямую использовать атрибуты и методы родительского класса

# In[12]:


class Human():
    # перенесем все в init, т.к. теперь мы сможем его наследовать при помощи super()
     def __init__(self, name, gender, height=0, weight=0, hands=2):
        self.name = name
        self.gender = gender
        self.height = height
        self.weight = weight
        self.hands = hands
    

class Spider():
    def __init__(self, gender, height=0, weight=0, hands=6):
        self.gender = gender
        self.height = height
        self.weight = weight
        self.hands = hands
    
    def webshoot(self):
        print('Pew-Pew!')

        
    
class SpiderMan(Human, Spider):
    def __init__(self, name, gender):
        self.weapons = []
        # вызываем конструктор родительского класса, чтобы взять и инициализировать нужные атрибуты оттуда
        super().__init__(name, gender)

    def attack(self):
        if 'web' in self.weapons:
            super().webshoot()
        else:
            print('No web!')
        

       
        
peter_parker = SpiderMan('Peter Parker', 'Male')
peter_parker.attack()

peter_parker.weapons.append('web')
peter_parker.attack()


# ### Полиморфизм
# 
# Полиморфизм предполагает способность к изменению функционала, унаследованного от родительского класса.

# In[13]:


class Human():
    def __init__(self, name, gender, height=0, weight=0, hands=2):
        self.name = name
        self.gender = gender
        self.height = height
        self.weight = weight
        self.hands = hands
    
    def move(self):
        self.weight -= 0.01

class Spider():
    def __init__(self, gender, height=0, weight=0, hands=6):
        self.gender = gender
        self.height = height
        self.weight = weight
        self.hands = hands
    
    def webshoot(self):
        print('Pew-Pew!')

        
    
class SpiderMan(Human, Spider):
    def __init__(self, name, gender):
        self.weapons = []
        super().__init__(name, gender)

    def attack(self):
        if 'web' in self.weapons:
            super().webshoot()
        else:
            print('No web!')
    # мы можем переопределить метод родительского класса на какой-то другой функционал
    def move(self):
        super().webshoot()
        super().move()
        
peter_parker = SpiderMan('Peter Parker', 'Male')
print(peter_parker.weight)
peter_parker.move()
print(peter_parker.weight)


# Магические методы – это общий термин, относящийся к "специальным" методам классов, для которых нет единого определения, поскольку их применение разнообразно. 

# И мы также можем перегрузить эти магические методы

# In[22]:


class Human():
    def __init__(self, name, gender, height=0, weight=0, hands=2):
        self.name = name
        self.gender = gender
        self.height = height
        self.weight = weight
        self.hands = hands
    
    def move(self):
        self.weight -= 0.01

class Spider():
    def __init__(self, gender, height=0, weight=0, hands=6):
        self.gender = gender
        self.height = height
        self.weight = weight
        self.hands = hands
    
    def webshoot(self):
        print('Pew-Pew!')

        
    
class SpiderMan(Human, Spider):
    def __init__(self, name, gender):
        self.weapons = []
        super().__init__(name, gender)

    def attack(self):
        if 'web' in self.weapons:
            super().webshoot()
        else:
            print('No web!')
    def move(self):
        super().webshoot()
        super().move()
        
    # добавим возможность сравнения персонажей   
    def __lt__(self, other):
        if not isinstance(other, SpiderMan):
            print('Not a SpiderMan!')
            return
        return len(self.weapons) < len(other.weapons)
    
peter_parker = SpiderMan('Peter Parker', 'Male')
miles_morales = SpiderMan('Miles Morales', 'Male')
peter_parker.weapons += ['web_shooter', 'electricity']
print(peter_parker.weapons)
miles_morales.weapons += ['web_shooter', 'electricity']
print(miles_morales.weapons)
print(peter_parker < miles_morales)
# и даже "больше" будет работать!
print(peter_parker > miles_morales)



