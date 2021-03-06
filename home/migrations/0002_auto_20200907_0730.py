# Generated by Django 3.1.1 on 2020-09-07 02:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='patient',
            name='date',
            field=models.TextField(default='', editable=False),
        ),
        migrations.AddField(
            model_name='patient',
            name='desc',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='patient',
            name='doctor',
            field=models.CharField(max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='patient',
            name='time',
            field=models.TextField(default='', editable=False),
        ),
        migrations.AlterField(
            model_name='patient',
            name='address',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='patient',
            name='age',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='patient',
            name='contact',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='patient',
            name='gender',
            field=models.CharField(max_length=30),
        ),
    ]
