# Generated by Django 4.2.4 on 2024-02-11 12:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('college_admin', '0005_register_cap_img'),
    ]

    operations = [
        migrations.AlterField(
            model_name='register',
            name='cap_img',
            field=models.ImageField(default=None, upload_to='cap_images/'),
        ),
    ]