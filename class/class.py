class Person:
     def __init__(self, name, age, height):
        self.name = name
        self.age =  age
        self.height =  height
  
     def introduce(self):
         print(f"나는 {self.name}이고 나이는 {self.age}이고 내 키는 {self.height}cm야")
     def yell(self):
         print(f"아?")

class Developer(Person):
    keyboard= '기계식'
    def __init__(self, name, age, height):
        super().__init__(name, age, height)

    def yell(self):
        print(f"어?")

class Designer(Person):
    def __init__(self, name, age, height, disease):
        super().__init__(name, age, height)
        self.disease = disease

class ProductManager(Person):
    def __init__(self, name, age, height):
        super().__init__(name, age, height)

    def yell(self):
        print("개발자님 여기 오류있어요")

    def aging(self):
        self.age += 2
        self.height -= 5
        print("개발자를 새로 뽑아야하나...")
        Developer.keyboard='멤브레인'



d1 = Developer('김모시',20, 172)
d2 = Designer('김상우', 21, 174,'안구건조증')
p1 = ProductManager('정모시', 30, 180)

d1.introduce()
d1.yell()
d2.introduce()
d2.yell()
p1.introduce()
p1.yell()
p1.aging()
p1.introduce()



        
    
    


        
    