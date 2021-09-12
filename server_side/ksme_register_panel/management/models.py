from django.db import models
from django.contrib.auth.models import User
from django.db.models.deletion import CASCADE

class PhoneNumber(models.Model):
    phone_number = models.CharField(blank=True, max_length=20, verbose_name="شماره تماس")
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="phone_number", verbose_name="کاربر")

    class Meta:
        verbose_name_plural = "شماره های تماس"


class EducationalLevel(models.Model): # مقطع تحصیلی
    educational_level = models.CharField(blank=True, max_length=20, verbose_name="مقطع تحصیلی")
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="educational_level", verbose_name="کاربر")


    class Meta:
        verbose_name_plural = "مقاطع تحصیلی"


class EducationalField(models.Model): # رشته تحصیلی
    educational_field = models.CharField(blank=True, max_length=20, verbose_name="رشته تحصیلی")
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="educational_field", verbose_name="کاربر")

    class Meta:
        verbose_name_plural = "رشته های تحصیلی"


class Skills(models.Model):
    skills = models.TextField(blank=True, verbose_name="توانایی ها")
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="skills", verbose_name="کاربر")

    class Meta:
        verbose_name_plural = "توانایی ها"



class ExtraWords(models.Model):
    extra_words = models.TextField(blank=True, verbose_name="حرف های بیشتر")
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="extra_words", verbose_name="کاربر")

    class Meta:
        verbose_name_plural = "حرف های بیشتر"


class StudentNumber(models.Model): 
    student_number = models.CharField(blank=True, max_length=20, verbose_name="شماره دانشجویی")
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="student_number", verbose_name="کاربر")

    class Meta:
        verbose_name_plural = "شماره های دانشجویی"


class NationalNumber(models.Model): 
    national_number = models.CharField(blank=True, max_length=20, verbose_name="کد ملی")
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="national_number", verbose_name="کاربر")

    class Meta:
        verbose_name_plural = "کد های ملی"


class Activities(models.Model):
    activities = models.TextField(blank=True, verbose_name="فعالیت های کاری و پژوهشی")
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="activities", verbose_name="کاربر")

    class Meta:
        verbose_name_plural = "فعالیت های کاری"


class Birthday(models.Model): 
    birthday = models.CharField(blank=True, max_length=20, verbose_name="تاریخ تولد")
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="birthday", verbose_name="کاربر")

    class Meta:
        verbose_name_plural = "تاریخ های تولد"


class CorporateField(models.Model):
    corporate_field = models.CharField(blank=True, max_length=20, verbose_name="حوزه همکاری")
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="corporate_field", verbose_name="کاربر")   

    class Meta:
        verbose_name_plural = "حوزه های همکاری" 


class Activity(models.Model):
    activity = models.BooleanField(default=False, verbose_name="فعال")
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="activity", verbose_name="کاربر") 

    class Meta:
        verbose_name_plural = "فعال بودن"