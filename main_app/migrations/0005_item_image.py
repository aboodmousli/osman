# Generated by Django 2.2.5 on 2019-09-30 21:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0004_remove_item_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='image',
            field=models.ImageField(default='https://mdbootstrap.com/img/Photos/Horizontal/E-commerce/Products/14.jpg', upload_to='images/'),
            preserve_default=False,
        ),
    ]