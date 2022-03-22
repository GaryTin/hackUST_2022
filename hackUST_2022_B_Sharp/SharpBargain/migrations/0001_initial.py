# Generated by Django 4.0.3 on 2022-03-19 09:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DB_Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('prod_type', models.CharField(max_length=256)),
                ('prod_img', models.ImageField(upload_to='images')),
            ],
        ),
        migrations.CreateModel(
            name='DB_user',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.IntegerField(unique=True)),
                ('email', models.EmailField(max_length=254)),
                ('password', models.CharField(max_length=32)),
                ('role', models.CharField(choices=[('C', 'Customer'), ('R', 'Retailer'), ('M', 'Manufacturer')], default='C', max_length=1)),
                ('name', models.CharField(max_length=256)),
            ],
        ),
        migrations.CreateModel(
            name='Manufacturer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('manu_id', models.IntegerField(unique=True)),
                ('manu_name', models.CharField(max_length=256)),
                ('manu_address', models.CharField(max_length=256)),
            ],
        ),
    ]