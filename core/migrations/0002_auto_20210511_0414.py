# Generated by Django 3.2.2 on 2021-05-11 04:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='UserRishu',
        ),
        migrations.AlterField(
            model_name='propertymaster',
            name='Descrpt',
            field=models.TextField(max_length=255, null=True),
        ),
    ]
