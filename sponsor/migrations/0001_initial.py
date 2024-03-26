# Generated by Django 5.0.1 on 2024-02-17 12:08

import django.core.validators
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ConditionModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
            options={
                'verbose_name': 'Condition',
                'verbose_name_plural': 'Conditions',
            },
        ),
        migrations.CreateModel(
            name='IsHumanModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='SponsorModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=255)),
                ('phone', models.CharField(max_length=13)),
                ('spons_value', models.PositiveIntegerField(validators=[django.core.validators.MinValueValidator(1000000)])),
                ('use_value', models.PositiveIntegerField(default=0)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('organization', models.CharField(blank=True, max_length=250, null=True)),
                ('condition', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='sponsor', to='sponsor.conditionmodel')),
                ('is_human', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sponsor', to='sponsor.ishumanmodel')),
            ],
            options={
                'verbose_name': 'Sponsor',
                'verbose_name_plural': 'Sponsors',
            },
        ),
    ]
