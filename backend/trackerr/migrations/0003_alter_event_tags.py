# Generated by Django 4.0.4 on 2022-06-10 20:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trackerr', '0002_alter_company_address'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='tags',
            field=models.CharField(blank=True, max_length=400, null=True),
        ),
    ]