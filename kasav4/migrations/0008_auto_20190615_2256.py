# Generated by Django 2.2.2 on 2019-06-15 22:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kasav4', '0007_auto_20190615_2142'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transaction',
            name='transaction_method',
            field=models.CharField(max_length=30, null=True),
        ),
    ]