# Generated by Django 2.0.1 on 2018-01-27 09:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Bucketlist',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, unique=True)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('date_modified', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='INEModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ine_curp', models.CharField(max_length=35)),
                ('ine_local_id', models.CharField(max_length=6)),
                ('ine_municipality', models.CharField(max_length=4)),
                ('ine_section', models.CharField(max_length=6)),
                ('ine_emision', models.CharField(max_length=5)),
                ('ine_validity', models.CharField(max_length=5)),
                ('ine_state', models.IntegerField()),
                ('ine_elector_code', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='PassportModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('passport_emision_date', models.DateField()),
                ('passport_validity_date', models.DateField()),
                ('passport_number', models.CharField(max_length=40)),
            ],
        ),
        migrations.CreateModel(
            name='UserModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_name', models.CharField(max_length=30)),
                ('user_last_name', models.CharField(max_length=30)),
                ('user_email', models.CharField(max_length=50, unique=True)),
                ('user_tel', models.CharField(max_length=15)),
                ('user_birthday', models.DateField()),
                ('user_rfc', models.CharField(max_length=60)),
                ('user_address', models.CharField(max_length=300)),
                ('user_gender', models.CharField(choices=[('M', 'Male'), ('F', 'Female')], default='F', max_length=7)),
                ('user_ine_id', models.IntegerField()),
                ('user_passport_id', models.IntegerField()),
                ('user_creation_date', models.DateField()),
                ('user_profile_picture', models.ImageField(upload_to='')),
            ],
        ),
    ]
