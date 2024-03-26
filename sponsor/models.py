from django.db import models
from django.core.validators import MinValueValidator

min = 1000000

class IsHumanModel(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self) -> str:
        return self.name

class ConditionModel(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self) -> str:
        return self.name
    
    class Meta:
        verbose_name = 'Condition'
        verbose_name_plural = 'Conditions'

class SponsorModel(models.Model):
    full_name = models.CharField(max_length=255)
    phone = models.CharField(max_length=13)
    spons_value = models.PositiveIntegerField(validators=[MinValueValidator(min)])
    use_value = models.PositiveIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    condition = models.ForeignKey(ConditionModel, on_delete=models.CASCADE, related_name='sponsor', default=1)
    is_human = models.ForeignKey(IsHumanModel, on_delete=models.CASCADE, related_name='sponsor')
    organization = models.CharField(max_length=250, blank=True, null=True, default='')

    def condition_name(self):
        return self.condition.name if self.condition else None
    
    def isHuman_name(self):
        return self.is_human.name if self.is_human else None
    
    def __str__(self) -> str:
        return self.full_name

    
    class Meta:
        verbose_name = 'Sponsor'
        verbose_name_plural = 'Sponsors'