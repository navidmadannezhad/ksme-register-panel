from django.contrib import admin
from .models import EducationalField, EducationalLevel, ExtraWords, NationalNumber, StudentNumber, PhoneNumber, Birthday, Activities, Skills, CorporateField, Activity
from django.contrib.auth.models import User

class myUserAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'educational_level', 'get_educational_field', 'get_student_number', 'get_national_number']
    empty_value_display = " - "
    fields = ('first_name', 'last_name', 'email')

    def get_educational_level(self, obj):
        return obj.educational_level.educational_level

    def get_educational_field(self, obj):
        return obj.educational_field.educational_field

    def get_phone_number(self, obj):
        return obj.phone_number.phone_number

    def get_student_number(self, obj):
        return obj.student_number.student_number

    def get_national_number(self, obj):
        return obj.national_number.national_number

    def get_skills(self, obj):
        return obj.skills.skills

    def get_activities(self, obj):
        return obj.activities.activities

    def get_activity(self, obj):
        return obj.activity.activity

    def get_educational_field(self, obj):
        return obj.educational_field.educational_field

    def get_educational_field(self, obj):
        return obj.educational_field.educational_field

    def get_educational_field(self, obj):
        return obj.educational_field.educational_field

        

class EducationalFieldAdmin(admin.ModelAdmin):
    list_display = ['user_full_name', 'educational_field']
    
    def user_full_name(self, obj):
        return obj.user.first_name+' '+obj.user.last_name

class EducationalLevelAdmin(admin.ModelAdmin):
    list_display = ['user_full_name', 'educational_level']

    def user_full_name(self, obj):
        return obj.user.first_name+' '+obj.user.last_name

class ExtraWordsAdmin(admin.ModelAdmin):
    list_display = ['user_full_name', 'extra_words']

    def user_full_name(self, obj):
        return obj.user.first_name+' '+obj.user.last_name

class NationalNumberAdmin(admin.ModelAdmin):
    list_display = ['user_full_name', 'national_number']

    def user_full_name(self, obj):
        return obj.user.first_name+' '+obj.user.last_name

class StudentNumberAdmin(admin.ModelAdmin):
    list_display = ['user_full_name', 'student_number']

    def user_full_name(self, obj):
        return obj.user.first_name+' '+obj.user.last_name

class PhoneNumberAdmin(admin.ModelAdmin):
    list_display = ['user_full_name', 'phone_number']

    def user_full_name(self, obj):
        return obj.user.first_name+' '+obj.user.last_name

class BirthdayAdmin(admin.ModelAdmin):
    list_display = ['user_full_name', 'birthday']

    def user_full_name(self, obj):
        return obj.user.first_name+' '+obj.user.last_name

class ActivitiesAdmin(admin.ModelAdmin):
    list_display = ['user_full_name', 'activities']

    def user_full_name(self, obj):
        return obj.user.first_name+' '+obj.user.last_name

class SkillsAdmin(admin.ModelAdmin):
    list_display = ['user_full_name', 'skills']

    def user_full_name(self, obj):
        return obj.user.first_name+' '+obj.user.last_name

class CorporateFieldAdmin(admin.ModelAdmin):
    list_display = ['user_full_name', 'corporate_field']

    def user_full_name(self, obj):
        return obj.user.first_name+' '+obj.user.last_name

class ActivityAdmin(admin.ModelAdmin):
    list_display = ['user_full_name', 'activity']

    def user_full_name(self, obj):
        return obj.user.first_name+' '+obj.user.last_name



admin.site.unregister(User)
admin.site.register(User, myUserAdmin)

admin.site.register(EducationalField, EducationalFieldAdmin)
admin.site.register(EducationalLevel, EducationalLevelAdmin)
admin.site.register(ExtraWords, ExtraWordsAdmin)
admin.site.register(NationalNumber, NationalNumberAdmin)
admin.site.register(StudentNumber, StudentNumberAdmin)
admin.site.register(PhoneNumber, PhoneNumberAdmin)
admin.site.register(Birthday, BirthdayAdmin)
admin.site.register(Activities, ActivitiesAdmin)
admin.site.register(Skills, SkillsAdmin)
admin.site.register(CorporateField, CorporateFieldAdmin)
admin.site.register(Activity, ActivityAdmin)