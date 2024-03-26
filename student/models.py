import json
from django.db import models
from sponsor.models import SponsorModel
from django.core.validators import MinValueValidator
min = 1000000

class OtmModel(models.Model):
    name = models.CharField(max_length=250) 

    def __str__(self) -> str:
        return self.name
    
    class Meta:
        verbose_name = 'OTM'
        verbose_name_plural = 'OTMs'

class TypeModel(models.Model):
    name = models.CharField(max_length=250)

    def __str__(self) -> str:
        return self.name
    
    class Meta:
        verbose_name = 'Type'
        verbose_name_plural = 'Types'

class StudentModel(models.Model):
    full_name = models.CharField(max_length=250)
    phone = models.CharField(max_length=13)
    type = models.ForeignKey(TypeModel, on_delete=models.CASCADE, related_name='student')
    otm = models.ForeignKey(OtmModel, on_delete=models.CASCADE, related_name='student')
    allocated_amount = models.PositiveIntegerField(default=0)
    contract = models.PositiveIntegerField(validators=[MinValueValidator(min)])
    sponsor = models.JSONField(null=True, blank=True)

    def sponsors_get(self):
        if self.sponsor is not None:
            sponsors = eval(self.sponsor)
            return sponsors
        return self.sponsor

    def otm_name(self):
        return self.otm.name if self.otm else None
    
    def type_name(self):
        return self.type.name if self.type else None

    def __str__(self) -> str:
        return self.full_name
   
    class Meta:
        verbose_name = 'Student'
        verbose_name_plural = 'Students'

class AddSponsorModel(models.Model):
    summa = models.PositiveIntegerField(validators=[MinValueValidator(min)])
    sponsor = models.ForeignKey(SponsorModel, on_delete=models.CASCADE)
    student = models.ForeignKey(StudentModel, on_delete=models.CASCADE)

    def get_sponsor_full_name(self):
        return self.sponsor.full_name if self.sponsor else None
