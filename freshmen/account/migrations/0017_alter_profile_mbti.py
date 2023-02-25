# Generated by Django 3.2.18 on 2023-02-24 02:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0016_auto_20230224_0231'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='mbti',
            field=models.CharField(choices=[('ENFP', 'ENFP'), ('ENTJ', 'ENTJ'), ('ESTJ', 'ESTJ'), ('ESFP', 'ESFP'), ('ISTP', 'ISTP'), ('ISFP', 'ISFP'), ('INTJ', 'INTJ'), ('ENFJ', 'ENFJ'), ('INTP', 'INTP'), ('INFJ', 'INFJ'), ('INFP', 'INFP'), ('ESFJ', 'ESFJ'), ('ISTJ', 'ISTJ'), ('ENTP', 'ENTP'), ('ISFJ', 'ISFJ'), ('ESTP', 'ESTP')], max_length=16, null=True),
        ),
    ]
