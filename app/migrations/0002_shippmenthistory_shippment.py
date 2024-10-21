# Generated by Django 5.0.4 on 2024-10-21 10:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='shippmenthistory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Location', models.CharField(blank=True, max_length=50, null=True)),
                ('Status', models.CharField(blank=True, max_length=50, null=True)),
                ('datetimec', models.CharField(blank=True, max_length=50, null=True)),
                ('Remarks', models.CharField(blank=True, max_length=50, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='shippment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('SName', models.CharField(blank=True, max_length=50, null=True)),
                ('SAddress', models.TextField(blank=True, null=True)),
                ('SEmail', models.CharField(blank=True, max_length=50, null=True)),
                ('SPhone', models.CharField(blank=True, max_length=50, null=True)),
                ('RName', models.CharField(blank=True, max_length=50, null=True)),
                ('RAddress', models.TextField(blank=True, null=True)),
                ('REmail', models.CharField(blank=True, max_length=50, null=True)),
                ('RPhone', models.CharField(blank=True, max_length=50, null=True)),
                ('Origin', models.CharField(blank=True, max_length=50, null=True)),
                ('Destination', models.CharField(blank=True, max_length=50, null=True)),
                ('Mode', models.CharField(blank=True, max_length=50, null=True)),
                ('uuid', models.CharField(blank=True, default='e59951025812', max_length=50, null=True)),
                ('Quantity', models.CharField(blank=True, max_length=50, null=True)),
                ('Weight', models.CharField(blank=True, max_length=50, null=True)),
                ('Amount', models.CharField(blank=True, max_length=50, null=True)),
                ('PaymentMode', models.CharField(blank=True, max_length=50, null=True)),
                ('Delivery', models.CharField(blank=True, max_length=50, null=True)),
                ('DepartureDate', models.CharField(blank=True, max_length=50, null=True)),
                ('PackageItems', models.TextField(blank=True, null=True)),
                ('message', models.TextField(blank=True, null=True)),
                ('datetimec', models.DateTimeField(auto_now_add=True, null=True)),
                ('datetimecmain', models.DateTimeField(blank=True, null=True)),
                ('history', models.ManyToManyField(blank=True, to='app.shippmenthistory')),
            ],
        ),
    ]