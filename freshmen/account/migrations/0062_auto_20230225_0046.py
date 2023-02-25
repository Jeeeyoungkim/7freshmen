# Generated by Django 3.2.18 on 2023-02-25 00:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0061_merge_0059_auto_20230224_0614_0060_auto_20230224_2220'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='live',
            field=models.CharField(choices=[('Y', '유'), ('N', '무')], max_length=128, null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='mbti',
            field=models.CharField(choices=[('ISFP', 'ISFP'), ('INFP', 'INFP'), ('ENTP', 'ENTP'), ('ISTJ', 'ISTJ'), ('ENFJ', 'ENFJ'), ('ISTP', 'ISTP'), ('ESTJ', 'ESTJ'), ('ISFJ', 'ISFJ'), ('ENTJ', 'ENTJ'), ('INTJ', 'INTJ'), ('INFJ', 'INFJ'), ('ESFP', 'ESFP'), ('ENFP', 'ENFP'), ('INTP', 'INTP'), ('ESFJ', 'ESFJ'), ('ESTP', 'ESTP')], max_length=16, null=True),
        ),
    ]
