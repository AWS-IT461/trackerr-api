# Generated by Django 4.0.4 on 2022-06-10 21:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trackerr', '0004_alter_company_address_alter_company_contact_info'),
    ]

    operations = [
        migrations.AlterField(
            model_name='company',
            name='address',
            field=models.CharField(blank=True, default='', max_length=150),
        ),
        migrations.AlterField(
            model_name='company',
            name='contact_info',
            field=models.CharField(blank=True, default='', max_length=11),
        ),
    ]
