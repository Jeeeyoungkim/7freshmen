# Generated by Django 3.2.18 on 2023-02-24 02:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0011_alter_profile_mbti'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='mbti',
            field=models.CharField(choices=[('INTP', 'INTP'), ('ESFP', 'ESFP'), ('ENTJ', 'ENTJ'), ('ESTJ', 'ESTJ'), ('ESFJ', 'ESFJ'), ('ESTP', 'ESTP'), ('ISTJ', 'ISTJ'), ('ENFJ', 'ENFJ'), ('ENFP', 'ENFP'), ('ENTP', 'ENTP'), ('ISTP', 'ISTP'), ('INFP', 'INFP'), ('ISFJ', 'ISFJ'), ('INFJ', 'INFJ'), ('INTJ', 'INTJ'), ('ISFP', 'ISFP')], max_length=16, null=True),
        ),
    ]
