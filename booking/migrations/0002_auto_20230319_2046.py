# Generated by Django 3.2.18 on 2023-03-19 20:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='amount_adults',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='booking',
            name='end_date',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='booking',
            name='start_date',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='booking',
            name='total_price',
            field=models.FloatField(),
        ),
    ]
