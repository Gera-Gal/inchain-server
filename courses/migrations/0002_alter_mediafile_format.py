# Generated by Django 3.2 on 2022-06-28 21:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mediafile',
            name='format',
            field=models.CharField(choices=[('l-in', 'Left Inline'), ('r-in', 'Right Inline'), ('c-full', 'Center Full Screen')], max_length=6),
        ),
    ]
