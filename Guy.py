import random

class Guy:
    def __init__(self, name='Human', job = None, home = None, first_car = None, second_car = None):
        self.name = name
        self.job = job
        self.home = home
        self.first_car = first_car
        self.second_car = second_car
        self.gladness = 50
        self.satiety = 50
        self.money = 100
    def get_home(self):
        self.home = House()
    def get_first_car(self):
        self.first_car = Auto(brands_of_car)
    def get_second_car(self):
        self.second_car = Auto(brands_of_car)
    def get_job(self):
        if self.first_car.drive():
            pass
        else:
            pass #потому что есть 2 машина
            self.to_repair_first_car()
            return
        self.job = Job(job_list)

    def eat(self):
        if self.home.food <= 0:
            self.shopping("food")
        else:
            if self.satiety >= 100:
                self.satiety = 100
                return
            self.satiety += 5
            self.home.food -= 5

    def work(self):
        if self.first_car.drive():
            pass
        else:
            if self.first_car.fuel < 20:
                self.shopping('fuel')
                return
            else:
                pass #потому что есть 2 машина
                self.to_repair_first_car()
                return
        self.money += self.job.salary
        self.gladness -= self.job.gladness_less
        self.satiety -= 4
    def shopping(self, manage):
        if self.first_car.drive():
            pass
        else:
            if self.first_car.fuel < 20 or self.second_car.fuel < 20:
                manage = 'fuel'
            else:
                pass#потому что есть 2 машина
                self.to_repair_first_car()
                return
        if manage == 'fuel':
            print('I bought fuel')
            self.money -= 100
            self.first_car.fuel += 100
            self.second_car.fuel += 100
        elif manage == 'food':
            print('Bought food')
            self.money -= 50
            self.home.food += 50
        elif manage == 'delicacies':
            print('Happy')
            self.gladness += 10
            self.satiety += 2
            self.money -= 15



    def chill(self):
        self.gladness += 10
        self.home.mess += 5
    def clean_home(self):
        self.gladness -= 5
        self.home.mess = 0
    def to_repair_first_car(self):
        self.first_car.strength += 100
        self.money -= 50
    def to_repair_second_car(self):
        self.second_car.strength += 100
        self.money -= 50
    def days_indexes(self, day):
        day = f"Today the {day} of {self.name}'s life"
        print(f"{day:^50}", '\n')
        human_indexes = self.name + "'s indexess"
        print(f"{human_indexes:=^50}", '\n')
        print(f'Money - {self.money}')
        print(f'Satiety - {self.satiety}')
        print(f'Gladness - {self.gladness}')
        home_indexes = "Home indexes"
        print(f"{home_indexes:^50}", '\n')
        print(f'Food - {self.home.food}')
        print(f'Mess - {self.home.mess}')
        first_car_indexes = "First car indexes"
        print(f"{first_car_indexes:^50}", '\n')
        print(f'Fuel - {self.first_car.fuel}')
        print(f'Strength - {self.first_car.strength}')
        second_car_indexes = "Second car indexes"
        print(f"{second_car_indexes:^50}", '\n')
        print(f'Fuel - {self.second_car.fuel}')
        print(f'Strength - {self.second_car.strength}')

    def is_alive(self):
        if self.gladness < 0:
            print("Depression…")
            return False
        if self.satiety < 0:
            print("Dead…")
            return False
        if self.money < -500:
            print("Bankrupt…")
            return False
    def live(self, day):
        if self.is_alive() == False:
            return False
        if self.home is None:
            print('Settled in the house')
            self.get_home()
        if self.first_car is None:
            self.get_first_car()
        if self.second_car is None:
            self.get_second_car()
            print(f"I bought a car {self.first_car.brand}")
        if self.job is None:
            self.get_job()
            print(f"I don't have a job, I'm going to get a job {self.job.job} with salary {self.job.salary}")
        self.days_indexes(day)

        dice = random.randint(1, 4)
        if self.satiety < 20:
            print("I'll go eat")
            self.eat()
        elif self.gladness < 20:
            if self.home.mess > 15:
                print("I want to chill, but there is so much mess…\nSo I will clean the house")
                self.clean_home()
            else:
                print("Let`s chill!")
                self.chill()
        elif self.money < 0:
            print("Start working")
            self.work()
        elif self.first_car.strength < 15:
            print("I need to repair my first car")
            self.to_repair_first_car()
        elif self.second_car.strength < 15:
            print("I need to repair my second car")
            self.to_repair_second_car()
        elif dice == 1:
            print("Let`s chill!")
            self.chill()
        elif dice == 2:
            print("Start working")
            self.work()
        elif dice == 3:
            print("Cleaning time!")
            self.clean_home()
        elif dice == 4:
            print("Time for treats!")
            self.shopping(manage="delicacies")



class Auto:
    def __init__(self, brand_list):
        self.brand = random.choice(list(brand_list)) # BMW
        self.fuel = brand_list[self.brand]['fuel']
        self.strength = brand_list[self.brand]['strength']
        self.consumption = brand_list[self.brand]['consumption']

    def drive(self):
        if self.strength > 0 and self.fuel >= self.consumption:
            self.fuel -= self.consumption
            self.strength -= 1
            return True
        else:
            print('The car cannot move')
            return False
class House:
    def __init__(self):
        self.mess = 0
        self.food = 0

job_list = {
    "Java developer": {"salary": 50, "gladness_less": 10},
    "Python developer": {"salary": 40, "gladness_less": 3},
    "C++ developer": {"salary": 45, "gladness_less": 25},
    "Rust developer": {"salary": 70, "gladness_less": 1},
    "Pizza deliveryman": {"salary": 30, "gladness_less": 10},
    "Policeman": {"salary": 40, "gladness_less": 30},
    "Builder": {"salary": 55, "gladness_less": 10},
}

brands_of_car = {
    "BMW X5":{"fuel": 100, "strength": 100, "consumption": 6},
    "Lamborgini Huracan":{"fuel": 70, "strength": 130, "consumption": 16},
    "Lada Priora":{"fuel": 50, "strength": 40, "consumption": 10},
    "Volvo XC90":{"fuel": 70, "strength": 150, "consumption": 8},
    "Ferrari Roma":{"fuel": 80, "strength": 120, "consumption": 14},
    "Mersedes Benz":{"fuel": 90, "strength": 110, "consumption": 7},
    "Ford Focus":{"fuel": 70, "strength": 90, "consumption": 8},
    "Lamborgini Miura":{"fuel": 80, "strength": 100, "consumption": 12},

}
class Job:
    def __init__(self, job_list):
        self.job = random.choice(list(job_list))
        self.salary = job_list[self.job]['salary']
        self.gladness_less = job_list[self.job]['gladness_less']
manuel = Guy(name="Manuel")

for day in range(1,8):
    if manuel.live(day) == False:
        break