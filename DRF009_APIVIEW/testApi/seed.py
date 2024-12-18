from faker import Faker
import random
from .models import UserModel
faker=Faker()


try:
    def insert_stu_data(n=50):
        for i in range(0,n):
            name=faker.name()
            city=faker.city()
            email=faker.email()
            roll=random.randint(100,999)

            stu=UserModel.objects.create(name=name,city=city,email=email,roll=roll)
        
        print('Data Seeded Successfully!')
except Exception as e:
    print(e)        

insert_stu_data()    