# Generated by Django 2.2.6 on 2019-12-12 09:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Professor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, verbose_name='이름')),
                ('email', models.EmailField(max_length=30, verbose_name='아이디')),
                ('professor_number', models.CharField(max_length=10, verbose_name='직원번호')),
                ('password', models.CharField(max_length=20, verbose_name='비밀번호')),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, verbose_name='이름')),
                ('email', models.EmailField(max_length=30, verbose_name='아이디')),
                ('student_number', models.CharField(max_length=10, verbose_name='학번')),
                ('password', models.CharField(max_length=20, verbose_name='비밀번호')),
                ('grade', models.CharField(max_length=10, verbose_name='학년')),
                ('tutor', models.CharField(max_length=10, verbose_name='지도교수')),
            ],
        ),
    ]
