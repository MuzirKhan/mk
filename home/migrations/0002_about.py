# Generated by Django 4.2.2 on 2023-06-23 15:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='about',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=122)),
                ('Email', models.CharField(max_length=122)),
                ('Phone', models.CharField(max_length=122)),
            ],
        ),
    ]
