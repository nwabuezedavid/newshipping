# Generated by Django 5.0.4 on 2024-12-31 08:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_shippmenthistory_shippment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shippment',
            name='uuid',
            field=models.CharField(blank=True, default='eeb263dbc735', max_length=50, null=True),
        ),
    ]
