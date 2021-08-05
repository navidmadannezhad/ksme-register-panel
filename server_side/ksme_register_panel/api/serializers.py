from rest_framework import serializers
from .additional.additional import isEnglish
from django.contrib.auth.models import User
from management.models import PhoneNumber, EducationalLevel, EducationalField, Skills, ExtraWords, StudentNumber, NationalNumber, Activities, Birthday, CorporateField, Activity

class UserSerializer(serializers.Serializer):
    class Meta:
        fields = '__all__'

class Level(serializers.Serializer):
    first_name = serializers.CharField(error_messages = {'blank': 'لطفا نام خود را وارد کنید'}, required=False)
    last_name = serializers.CharField(error_messages = {'blank': 'لطفا نام خانوادگی خود را وارد کنید'}, required=False)
    email = serializers.EmailField(error_messages = {'blank': 'لطفا ایمیل خود را وارد کنید'}, required=False)
    birthday = serializers.CharField(error_messages = {'blank': 'لطفا تاریخ تولد خود را وارد کنید'}, required=False)
    national_number = serializers.CharField(error_messages = {'blank': 'لطفا کد ملی یا شماره شناسنامه را وارد کنید'}, required=False)
    phone_number = serializers.CharField(error_messages = {'blank': 'لطفا شماره تلفن همراه خود را وارد کنید'}, required=False)
    educational_field = serializers.CharField(error_messages = {'blank': 'لطفا نام رشته را وارد کنید'}, required=False)
    educational_level = serializers.CharField(error_messages = {'blank': 'لطفا مقطع تحصیلی خود را وارد کنید'}, required=False)
    student_number = serializers.CharField(error_messages = {'blank': 'لطفا شماره دانشجویی را وارد کنید'}, required=False)
    skills = serializers.CharField(allow_blank=True, required=False)
    activities = serializers.CharField(allow_blank=True, required=False)
    corporate_field = serializers.CharField(error_messages = {'blank': 'لطفا نام حوزه مورد نظر جهت همکاری را وارد کنید'}, required=False)
    extra_words = serializers.CharField(allow_blank=True, required=False)



class Level1Serializer(Level):
    
    def validate_phone_number(self, value):
        value = str(value)
        if value.isnumeric() is False:
            raise serializers.ValidationError('لطفا شماره تلفن خود را صحیح وارد کنید')
        return value

    
    def validate_national_number(self, value):
        value = str(value)
        if str(value).isnumeric() is False:
            raise serializers.ValidationError('لطفا کد ملی یا شماره شناسنامه خود را صحیح وارد کنید')
        return value

    def validate(self, data):
        if isEnglish(data['first_name']):
            raise serializers.ValidationError('لطفا نام خود را به فارسی بنویسید')

        elif isEnglish(data['last_name']):
            raise serializers.ValidationError('لطفا نام خانوادگی خود را به فارسی بنویسید')
        
        return data




class Level2Serializer(Level):

    def validate_student_number(self, value):
        value = str(value)
        if value.isnumeric() is False:
            raise serializers.ValidationError('Please enter your student number numerically')
        return value




class Level3Serializer(Level):

    def create(self, validated_data):
        user = User.objects.create(
            first_name= validated_data['first_name'],
            last_name= validated_data['last_name'],
            email= validated_data['email'],
        )

        phone_number = PhoneNumber.objects.create(
            phone_number= validated_data['phone_number'],
            user= user
        )
        phone_number.save()

        student_number = StudentNumber.objects.create(
            student_number= validated_data['student_number'],
            user= user
        )
        student_number.save()

        national_number = NationalNumber.objects.create(
            national_number= validated_data['national_number'],
            user= user
        )
        national_number.save()

        educational_field = EducationalField.objects.create(
            educational_field= validated_data['educational_field'],
            user= user
        )
        educational_field.save()

        educational_level = EducationalLevel.objects.create(
            educational_level= validated_data['educational_level'],
            user= user
        )
        educational_level.save()

        extra_words = ExtraWords.objects.create(
            extra_words= validated_data['extra_words'],
            user= user
        )
        extra_words.save()

        skills = Skills.objects.create(
            skills= validated_data['skills'],
            user= user
        )
        skills.save()

        activities = Activities.objects.create(
            activities= validated_data['activities'],
            user= user
        )
        activities.save()

        birthday = Birthday.objects.create(
            birthday= validated_data['birthday'],
            user= user
        )
        birthday.save()

        corporate_field = CorporateField.objects.create(
            corporate_field= validated_data['corporate_field'],
            user= user
        )
        corporate_field.save()

        activity = Activity.objects.create(
            user= user
        )
        activity.save()

        return user



    