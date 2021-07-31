from django.db import models
from django.contrib.auth.models import User
from django.db.models.deletion import CASCADE

class PhoneNumber(models.Model):
    phone_number = models.CharField(blank=True, max_length=20)
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="phone_number")


class EducationalLevel(models.Model): # مقطع تحصیلی
    educational_level = models.CharField(blank=True, max_length=20)
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="educational_level")


class EducationalField(models.Model): # رشته تحصیلی
    educational_field = models.CharField(blank=True, max_length=20)
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="educational_field")


class Skills(models.Model):
    skills = models.TextField(blank=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="skills")


class ExtraWords(models.Model):
    extra_words = models.TextField(blank=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="extra_words")


class StudentNumber(models.Model): 
    student_number = models.CharField(blank=True, max_length=20)
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="student_number")


class NationalNumber(models.Model): 
    national_number = models.CharField(blank=True, max_length=20)
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="national_number")


class Activities(models.Model):
    activities = models.TextField(blank=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="activities")


class Birthday(models.Model): 
    birthday = models.CharField(blank=True, max_length=20)
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="birthday")
