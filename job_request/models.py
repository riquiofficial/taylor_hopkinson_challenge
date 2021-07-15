from django.db import models

# Create your models here.


class Job(models.Model):
    name = models.CharField(max_length=60)
    role = models.CharField(max_length=200)

    def __str__(self):
        return f'{self.name} seeking candidate with {self.role} experience'


class JobApplication(models.Model):
    job_id = models.ForeignKey(Job, on_delete=models.CASCADE)
    candidate_email = models.EmailField(max_length=100, unique=True)

    def __str__(self):
        return f'{self.candidate_email} has applied to {self.job_id}'
