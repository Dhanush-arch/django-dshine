# Generated by Django 2.2.4 on 2020-08-11 10:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0027_comment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='status',
            field=models.CharField(choices=[('New', 'New'), ('True', 'True'), ('False', 'False')], default='True', max_length=10),
        ),
    ]
