# Generated by Django 3.0.6 on 2020-10-31 12:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Staff',
            fields=[
                ('emp_id', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('emp_name', models.CharField(max_length=100)),
                ('emp_gender', models.CharField(choices=[('M', 'Male'), ('F', 'Female'), ('O', 'Other')], max_length=100)),
                ('emp_age', models.CharField(max_length=3)),
                ('emp_salary', models.IntegerField()),
            ],
        ),
    ]
