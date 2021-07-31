from rest_framework import serializers
from .additional.additional import isEnglish

class UserSerializer(serializers.Serializer):
    class Meta:
        fields = '__all__'



class Level1Serializer(serializers.Serializer):
    first_name = serializers.CharField(error_messages = {'blank': 'لطفا نام خود را وارد کنید'})
    last_name = serializers.CharField(error_messages = {'blank': 'لطفا نام خانوادگی خود را وارد کنید'})
    birthday = serializers.CharField(error_messages = {'blank': 'لطفا تاریخ تولد را وارد کنید'})
    national_number = serializers.CharField(error_messages = {'blank': 'لطفا کد ملی را وارد کنید'})
    phone_number = serializers.CharField(error_messages = {'blank': 'لطفا شماره تلفن خود را وارد کنید'})

    class Meta:
        fields = ['first_name', 'last_name', 'birthday', 'national_number', 'phone_number']

    
    def validate_phone_number(self, value):
        value = str(value)
        if value.isnumeric() is False:
            raise serializers.ValidationError('شماره تلفن خود را به درستی وارد کنید')
        return value

    
    def validate_national_number(self, value):
        value = str(value)
        if str(value).isnumeric() is False:
            raise serializers.ValidationError('کد ملی تنها می‌تواند شامل اعداد باشد')
        return value

    def validate(self, data):
        if isEnglish(data['first_name']):
            raise serializers.ValidationError('لطفا نام خود را به فارسی وارد نمایید')

        elif isEnglish(data['last_name']):
            raise serializers.ValidationError('لطفا نام خانوادگی خود را به فارسی وارد نمایید')
        
        return data

    