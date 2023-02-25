# Generated by Django 3.2.18 on 2023-02-24 03:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0058_profile_drink_profile_favfood_profile_hometown_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='mbti',
            field=models.CharField(choices=[('ENTJ', 'ENTJ'), ('ENTP', 'ENTP'), ('ENFP', 'ENFP'), ('ESTP', 'ESTP'), ('ISTJ', 'ISTJ'), ('INTJ', 'INTJ'), ('INFP', 'INFP'), ('ENFJ', 'ENFJ'), ('INFJ', 'INFJ'), ('ESTJ', 'ESTJ'), ('ISFP', 'ISFP'), ('ISTP', 'ISTP'), ('ESFJ', 'ESFJ'), ('INTP', 'INTP'), ('ESFP', 'ESFP'), ('ISFJ', 'ISFJ')], max_length=16, null=True),
        ),
    ]