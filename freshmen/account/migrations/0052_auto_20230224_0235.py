# Generated by Django 3.2.17 on 2023-02-24 02:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0051_alter_profile_mbti'),
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
            field=models.CharField(choices=[('INTP', 'INTP'), ('ESFP', 'ESFP'), ('ENFJ', 'ENFJ'), ('ISTP', 'ISTP'), ('INTJ', 'INTJ'), ('ESTP', 'ESTP'), ('ENTP', 'ENTP'), ('ESTJ', 'ESTJ'), ('ENFP', 'ENFP'), ('ISFJ', 'ISFJ'), ('INFP', 'INFP'), ('ESFJ', 'ESFJ'), ('ISFP', 'ISFP'), ('ENTJ', 'ENTJ'), ('INFJ', 'INFJ'), ('ISTJ', 'ISTJ')], max_length=16, null=True),
        ),
    ]
