# Generated by Django 2.2.5 on 2019-10-02 15:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0005_item_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='label',
            field=models.CharField(choices=[('Y', 'Yeni'), ('I', 'İndirimli')], max_length=1),
        ),
    ]