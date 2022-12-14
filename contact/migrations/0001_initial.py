# Generated by Django 3.2.7 on 2022-09-20 08:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='نام')),
                ('email', models.EmailField(max_length=100, verbose_name='ایمیل')),
                ('message', models.TextField(blank=True, verbose_name='متن')),
            ],
            options={
                'verbose_name': 'مخاطبین',
                'verbose_name_plural': 'مخاطبین ها',
            },
        ),
    ]
