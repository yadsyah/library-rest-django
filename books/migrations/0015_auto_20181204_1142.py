# Generated by Django 2.1.3 on 2018-12-04 04:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0014_auto_20181204_0025'),
    ]

    operations = [
        migrations.AddField(
            model_name='member',
            name='gender',
            field=models.CharField(choices=[('M', 'Male'), ('F', 'FEMALE')], default='M', max_length=2),
        ),
        migrations.AlterField(
            model_name='book',
            name='title',
            field=models.CharField(max_length=200, unique=True),
        ),
        migrations.AlterField(
            model_name='bookcategory',
            name='name',
            field=models.CharField(blank=True, default='', max_length=100, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='order',
            name='code_borrow',
            field=models.CharField(blank=True, default='36029F', max_length=8, null=True, unique=True),
        ),
    ]
