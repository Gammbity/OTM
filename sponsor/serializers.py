import phonenumbers
from rest_framework import serializers
from .models import SponsorModel
import re
    
class SponsorSerializers(serializers.ModelSerializer):
    condition_name = serializers.CharField(read_only=True)
    isHuman_name = serializers.CharField(read_only=True)
    use_value = serializers.CharField(read_only=True)

    
    class Meta:
        model = SponsorModel
        fields = ['full_name', 'phone', 'spons_value', 'use_value', 'created_at', 'condition_name', 'isHuman_name']

class SponsorCreateSerializers(serializers.ModelSerializer):
    phone = serializers.CharField()

    def validate_phone(self, value):
        parsed_number = phonenumbers.parse(value, 'UZ')
        if phonenumbers.is_valid_number(parsed_number):
            return value    
        e = "Noto'g'ri O'zbekiston telefon raqami formati !"
        raise serializers.ValidationError({'phone': e})

    class Meta:
        model = SponsorModel
        fields = ['full_name', 'phone', 'spons_value', 'is_human', 'organization']
    
class SponsorDetSerializers(serializers.ModelSerializer):

    class Meta:
        model = SponsorModel
        fields = ['full_name', 'phone', 'spons_value', 'organization']

class SponsorUpdateSerializers(serializers.ModelSerializer):

    def to_representation(self, instance):
        if instance.is_human != 2:
            self.fields.pop('organization')
        return super().to_representation(instance)

    class Meta:
        model = SponsorModel
        fields = ['full_name', 'phone', 'spons_value', 'condition', 'is_human', 'organization']
