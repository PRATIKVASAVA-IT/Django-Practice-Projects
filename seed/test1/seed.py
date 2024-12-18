from faker import Faker
import random
from .models import student
faker=Faker()


try:
    def insert_stu_data(n=130):
        for i in range(0,n):
            name=faker.name()
            address=faker.city()
            email=faker.email()
            age=random.randint(18,38)

            stu=student.objects.create(name=name,address=address,email=email,age=age)
        
        print('Data Seeded Successfully!')
except Exception as e:
    print(e)        

insert_stu_data()    