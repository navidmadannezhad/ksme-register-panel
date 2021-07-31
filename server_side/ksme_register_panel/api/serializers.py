from rest_framework import serializers
from .additional.additional import isEnglish
from django.contrib.auth.models import User
from management.models import PhoneNumber, EducationalLevel, EducationalField, Skills, ExtraWords, StudentNumber, NationalNumber, Activities, Birthday, CorporateField, Activity

class UserSerializer(serializers.Serializer):
    class Meta:
        fields = '__all__'

class Level(serializers.Serializer):
    first_name = serializers.CharField(error_messages = {'blank': 'ﺩیﻥک ﺩﺭاﻭ اﺭ ﺩﻮﺧ ﻡﺎﻧ ﺎﻔﻄﻟ'})
    last_name = serializers.CharField(error_messages = {'blank': 'ﺩیﻥک ﺩﺭاﻭ اﺭ ﺩﻮﺧ یگﺩاﻮﻧﺎﺧ ﻡﺎﻧ ﺎﻔﻄﻟ'})
    email = serializers.EmailField(error_messages = {'blank': 'Please enter your email'})
    birthday = serializers.CharField(error_messages = {'blank': 'ﺩیﻥک ﺩﺭاﻭ اﺭ ﺪﻟﻮﺗ ﺥیﺭﺎﺗ ﺎﻔﻄﻟ'})
    national_number = serializers.CharField(error_messages = {'blank': 'ﺩیﻥک ﺩﺭاﻭ اﺭ یﻞﻣ ﺩک ﺎﻔﻄﻟ'})
    phone_number = serializers.CharField(error_messages = {'blank': 'ﺩیﻥک ﺩﺭاﻭ اﺭ ﺩﻮﺧ ﻦﻔﻠﺗ ﻩﺭﺎﻤﺷ ﺎﻔﻄﻟ'})
    educational_field = serializers.CharField(error_messages = {'blank': 'Please enter educational field'})
    educational_level = serializers.CharField(error_messages = {'blank': 'Please enter educational level'})
    student_number = serializers.CharField(error_messages ={'blank': 'Please enter student number'} )
    skills = serializers.CharField(allow_blank=True)
    activities = serializers.CharField(allow_blank=True)
    corporate_field = serializers.CharField(error_messages={'blank': 'Please at least enter one corporation Field'})
    extra_words = serializers.CharField(allow_blank=True)



class Level1Serializer(Level):
    
    def validate_phone_number(self, value):
        value = str(value)
        if value.isnumeric() is False:
            raise serializers.ValidationError('ﺩیﻥک ﺩﺭاﻭ یﺖﺳﺭﺩ ﻪﺑ اﺭ ﺩﻮﺧ ﻦﻔﻠﺗ ﻩﺭﺎﻤﺷ')
        return value

    
    def validate_national_number(self, value):
        value = str(value)
        if str(value).isnumeric() is False:
            raise serializers.ValidationError('ﺪﺷﺎﺑ ﺩاﺪﻋا ﻞﻣﺎﺷ ﺪﻧاﻮﺗیﻡ ﺎﻬﻨﺗ یﻞﻣ ﺩک')
        return value

    def validate(self, data):
        if isEnglish(data['first_name']):
            raise serializers.ValidationError('ﺩییﺎﻤﻧ ﺩﺭاﻭ یﺱﺭﺎﻓ ﻪﺑ اﺭ ﺩﻮﺧ ﻡﺎﻧ ﺎﻔﻄﻟ')

        elif isEnglish(data['last_name']):
            raise serializers.ValidationError('ﺩییﺎﻤﻧ ﺩﺭاﻭ یﺱﺭﺎﻓ ﻪﺑ اﺭ ﺩﻮﺧ یگﺩاﻮﻧﺎﺧ ﻡﺎﻧ ﺎﻔﻄﻟ')
        
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
        phone_number.save()

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

        activity = PhoneNumber.objects.create(
            user= user
        )
        activity.save()

        return user



    