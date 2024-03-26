import json
from django.dispatch import receiver
from rest_framework import serializers
from .models import StudentModel, AddSponsorModel
from sponsor.models import SponsorModel
from django.db.models.signals import pre_save
import phonenumbers

class StudentCreateSerializer(serializers.ModelSerializer):
    phone = serializers.CharField()

    def validate_phone(self, value):
        parsed_number = phonenumbers.parse(value, 'UZ')
        if phonenumbers.is_valid_number(parsed_number):
            return value    
        e = "Noto'g'ri O'zbekiston telefon raqami formati !"
        raise serializers.ValidationError({'phone': e})

    class Meta:
        model = StudentModel
        fields = ['full_name', 'phone', 'type', 'otm', 'allocated_amount', 'contract']
        read_only_fields = ['allocated_amount']

class StudentSerializer(serializers.ModelSerializer):
    type_name = serializers.CharField(read_only=True)
    otm_name = serializers.CharField(read_only=True)

    class Meta:
        model = StudentModel
        exclude = ['phone', 'sponsor', 'type', 'otm']
        read_only_fields = ['allocated_amount']



class StudentUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentModel
        fields = ['full_name', 'phone', 'otm', 'contract']

class AddSponsorListSerializer(serializers.ModelSerializer):
    class Meta:
        model = AddSponsorModel
        fields = ['get_sponsor_full_name', 'summa']

class AddSponsorSerializer(serializers.ModelSerializer):
    class Meta:
        model = AddSponsorModel
        fields = '__all__'

    @receiver(pre_save, sender=AddSponsorModel)
    def pre_save(sender, instance, **kwargs):
        student = StudentModel.objects.get(id=instance.student.id)
        sponsor = SponsorModel.objects.get(id=instance.sponsor.id)
        if student.contract >= instance.summa:
            student.allocated_amount += instance.summa
            student.contract -= instance.summa
            s = {      
                "full_name": instance.sponsor.full_name,
                "summa": instance.summa
            }
            if student.sponsor is not None:
                student.sponsor += f",{str(s)}"
            else:
                student.sponsor = json.dumps(s)
            student.save()
        else:
            e = f"Studentning kontrakti {student.contract} !"
            raise serializers.ValidationError({
                'contract': e
            })
        if sponsor.spons_value >= instance.summa:
            sponsor.spons_value -= instance.summa
            sponsor.use_value += instance.summa
            sponsor.save()
        else:    
            e = f"Sponsorda {sponsor.spons_value} pul bor !"
            raise serializers.ValidationError({
                'spons_value': e
            })

class StudentDetSerializer(serializers.ModelSerializer):
    type_name = serializers.CharField()
    otm_name = serializers.CharField()
    sponsors_get = serializers.CharField()
    class Meta:
        model = StudentModel
        exclude = ['type', 'otm', 'sponsor']

