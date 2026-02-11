from django.db import models

class Department(models.Model):
    department_name = models.CharField(max_length=100)
    department_description = models.TextField()

    def __str__(self):
        return self.department_name

class Placementcell(models.Model):
    student_name = models.CharField(max_length=100)
    student_image = models.ImageField(upload_to='placementcell')
    dep_name = models.ForeignKey(Department, on_delete=models.CASCADE)


    def __str__(self):
        return self.student_name+ " - " +str(self.dep_name)

class Search(models.Model):
    student_name = models.CharField(max_length=100)
    student_phonenumber = models.CharField(max_length=100)
    student_email = models.EmailField()
    student_image = models.ForeignKey(Placementcell, on_delete=models.CASCADE)