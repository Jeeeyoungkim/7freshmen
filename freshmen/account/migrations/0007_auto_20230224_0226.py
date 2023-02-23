# Generated by Django 3.2.18 on 2023-02-24 02:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0006_alter_profile_mbti'),
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
            field=models.CharField(choices=[('ESTP', 'ESTP'), ('ESTJ', 'ESTJ'), ('ESFJ', 'ESFJ'), ('ESFP', 'ESFP'), ('ENTP', 'ENTP'), ('ENFJ', 'ENFJ'), ('ENFP', 'ENFP'), ('ISTP', 'ISTP'), ('ISFJ', 'ISFJ'), ('INTP', 'INTP'), ('INTJ', 'INTJ'), ('INFJ', 'INFJ'), ('ENTJ', 'ENTJ'), ('ISTJ', 'ISTJ'), ('ISFP', 'ISFP'), ('INFP', 'INFP')], max_length=16, null=True),
        ),
    ]
