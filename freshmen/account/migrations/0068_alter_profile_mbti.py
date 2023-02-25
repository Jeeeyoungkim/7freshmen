# Generated by Django 3.2.18 on 2023-02-25 08:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0067_auto_20230225_0404'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='mbti',
            field=models.CharField(choices=[('ESFJ', 'ESFJ'), ('ENTJ', 'ENTJ'), ('ENFP', 'ENFP'), ('ENFJ', 'ENFJ'), ('ISTP', 'ISTP'), ('INTJ', 'INTJ'), ('INFJ', 'INFJ'), ('ESTP', 'ESTP'), ('ESFP', 'ESFP'), ('ESTJ', 'ESTJ'), ('ENTP', 'ENTP'), ('ISFP', 'ISFP'), ('ISTJ', 'ISTJ'), ('INTP', 'INTP'), ('INFP', 'INFP'), ('ISFJ', 'ISFJ')], max_length=16, null=True),
        ),
    ]
