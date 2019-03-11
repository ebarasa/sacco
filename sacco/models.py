from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Comment(models.Model):
    position = models.CharField(max_length=100)
    comment = models.TextField()
    date_commented = models.DateTimeField(default=timezone.now)
    name = models.ForeignKey(User, on_delete=models.CASCADE)

    def __srt__(self):
        return self.position


class Owner(models.Model):
    full_name = models.CharField(max_length=100)
    email = models.EmailField()
    id_number = models.IntegerField()
    phone_number = models.IntegerField()
    password =models.CharField(max_length=100)

    def __str__(self):
        return self.full_name


class Matatu(models.Model):
    owner_id = models.ForeignKey(Owner, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    reg_number = models.IntegerField()
    reg_year = models.DateTimeField()
    make_and_mode =models.CharField(max_length=100)
    seats = models.IntegerField()
    route = models.CharField(max_length=100, choices=(
        ('eldoret', 'Eldoret'),
        ('karatina', 'Karatina'),
        ('nairobi', 'Nairobi'),
        ('nanyuki', 'Nanyuki'),
        ('nakuru', 'Nakuru'),
        ('nyeri', 'Nyeri'),
        ('thika', 'Thika')
    ))
    image = models.ImageField(default='default.jpg', upload_to='matatu_pics')

    def __str__(self):
        return self.owner_id

class Crew(models.Model):
    matatu_id = models.ForeignKey(Matatu, on_delete=models.CASCADE) 
    full_name = models.CharField(max_length=100)
    id_number = models.IntegerField()
    phone_number = models.IntegerField()
    age = models.IntegerField()
    driver_license_type = models.CharField(max_length=100, choices = (
        ('category_a', 'Category_A'),
        ('category_b', 'Category_B'),
        ('category_c', 'Category_C')
    ))  
    driver_license_number = models.CharField(max_length=100)
    image = models.ImageField(default='default.jpg', upload_to='crew_pics')


    def __str__(self):
        return self.crew_type


class Finance(models.Model):
    matatu_id = models.ForeignKey(Matatu, on_delete=models.CASCADE)
    date_time = models.DateTimeField()
    finance_type = models.CharField(max_length=100, choices = (
        ('income', 'Income'),
        ('expense', 'Expense')
    ))
    details = models.CharField(max_length=200)
    amount = models.DecimalField(decimal_places=100, max_digits=100)

    def __str__(self):
        return self.matatu_id

class Activity_log(models.Model):
    matatu_id = models.ForeignKey(Matatu, on_delete=models.CASCADE)
    Activity_log_type = models.CharField(max_length=100, choices = (
        ('traffic_offence', 'Traffic_offence'),
        ('breakdown', 'Breakdown'),
        ('repair', 'Repair'),
        ('fuel', 'Fuel'),
        ('milage', 'Milage'),
        ('others', 'Others')
    ))
    Activity_log_details = models.CharField(max_length=100)
    amount = models.DecimalField(decimal_places=100, max_digits=100)

    def __str__(self):
        return self.matatu_id
