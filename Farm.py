import random
class Farmer:
    def __init__(self,name='John Doe',gold=1000):
        self.name=name
        self.gold=gold
        self.farms=[]
    def buy_farm(self,farm_name,shop):
        price=shop.selling['farm']
        if (self.gold-price)>=0:
            self.farms.append(Farm(farm_name))
            self.gold=self.gold-price
        else: 
            raise Exception('Not enough money') 
    def buy_goods(self,shop,goods,farm):# example good={'forage':5, 'egg':2}
        price=0
        for good in goods.keys:
            price+=shop.selling([good])*goods([good])
        if (self.gold-price)>=0:
            for good in goods.keys:
                farm.goods[good]+=goods([good])
            self.gold-=price
        else: 
            raise Exception('Not enough money') 
    def wait(self):
        for farm in self.farms:
            for cow in farm.cows:
                cow.hunger=cow.hunger-1
                cow.age+=1
                cow.flag=0
                if (cow.hunger<0) or(cow.age>20):
                    farm.cows.remove(cow)
            for hen in farm.hens:
                hen.hunger=hen.hunger-1 
                hen.age+=1 
                hen.flag=0 
                if (hen.hunger<0) or(hen.age>10):
                    farm.cows.remove(hen)
class Farm:
    def __init__(self,name='New farm'):
        self.name=name
        self.goods={'egg':0,'chicken':0,'beaf':0, 'milk':0, 'forage':0}
        self.hens=[]
        self.cows=[]      
class Pet:
    def __init__(self,farm):
        self.flag=0
        self.age=0
        self.hunger=0
        self.place=farm        
    def feed_pet(self,):
        self.hunger+=1
        self.place.goods['forage']-=1
class Hen(Pet):
    def produce(self,farm):
        if self.flag==0:
            farm.goods['egg']+=random.choice(1,2,3,4,5)
            self.flag=1
            self.hunger-=1
        else:
            raise Exception("Hen is tired! Leave it alone!")
    def child(self,farm):
        if self.flag==0:
            for i in range(random.choice(1,2,3,4,5)):
                farm.hens.append(Hen(farm))
            self.flag=1
        else:
            raise Exception("Hen is tired! Leave it alone!")
    def kill_pet_for_meat(self):
        self.place.goods['chiken']+=(self.hunger+1)
class Cow(Pet):
    def produce(self,farm):
        if self.flag==0:
            farm.goods['milk']+=random.choice(1,2,3)
            self.flag=1
        else:
            raise Exception("Cow is tired! Leave it alone!")
    def child(self):
        if self.flag==0:
            for i in range(random.choice(1,2)):
                self.place.hens.append(Cow(self.place))
            self.flag=1
        else:
            raise Exception("Cow is tired! Leave it alone!")                  
class Shop:
    def __init__(self,pricelist_buying,pricelist_selling,name='"All YOU NEED"'):
        self.selling=pricelist_selling
        self.buying=pricelist_buying
        self.name="name"
Farmer1=Farmer("John Doe")
merchant=Shop({'farm':700, 'hen':8, 'cow':70, 'egg':1,'chicken':5,'beaf':40, 'milk':3},{'farm':1100, 'hen':10, 'cow':100, 'forage':5})
