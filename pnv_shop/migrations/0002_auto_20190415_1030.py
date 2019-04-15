# Generated by Django 2.2 on 2019-04-15 05:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pnv_shop', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='Image',
            field=models.ImageField(default='', upload_to='pnv_shop/images'),
        ),
        migrations.AddField(
            model_name='product',
            name='category',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='product',
            name='price',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='product',
            name='subcategory',
            field=models.CharField(default='', max_length=50),
        ),
    ]