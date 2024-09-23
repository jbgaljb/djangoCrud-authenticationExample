# Generated by Django 5.1.1 on 2024-09-22 08:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.CharField(blank=True, max_length=50, null=True)),
                ('age', models.DecimalField(decimal_places=2, max_digits=4)),
                ('createdTime', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
