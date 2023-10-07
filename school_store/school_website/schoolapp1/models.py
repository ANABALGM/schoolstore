from django.db import models

class Department(models.Model):
    name = models.CharField(max_length=100)


class Course(models.Model):
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)

class Material(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class User(models.Model):
    name = models.CharField(max_length=100)
    dob = models.DateField()
    age = models.IntegerField()
    gender = models.CharField(max_length=1, choices=[('M', 'Male'), ('F', 'Female')])
    phone_number = models.CharField(max_length=20)
    email = models.EmailField()
    address = models.TextField()
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    purpose = models.CharField(max_length=20, choices=[('Enquiry', 'Enquiry'), ('Order', 'Place Order'), ('Return', 'Return')])
    materials_provide = models.ManyToManyField(Material)




