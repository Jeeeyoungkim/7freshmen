# Generated by Django 3.2.18 on 2023-02-24 02:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0015_auto_20230224_0230'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='gender',
            field=models.CharField(choices=[('male', '남성'), ('female', '여성')], max_length=16, null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='mbti',
            field=models.CharField(choices=[('INTJ', 'INTJ'), ('INTP', 'INTP'), ('ENTJ', 'ENTJ'), ('ENTP', 'ENTP'), ('ESFJ', 'ESFJ'), ('ESTP', 'ESTP'), ('ENFP', 'ENFP'), ('ISTP', 'ISTP'), ('ESFP', 'ESFP'), ('ENFJ', 'ENFJ'), ('ESTJ', 'ESTJ'), ('ISTJ', 'ISTJ'), ('ISFJ', 'ISFJ'), ('ISFP', 'ISFP'), ('INFP', 'INFP'), ('INFJ', 'INFJ')], max_length=16, null=True),
        ),
    ]
