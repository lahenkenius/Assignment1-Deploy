# Generated by Django 2.2 on 2020-09-13 23:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('clients', '0003_vehicle'),
    ]

    operations = [
        migrations.AddField(
            model_name='vehicle',
            name='client',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='vehicles', to='clients.Client'),
        ),
        migrations.AlterField(
            model_name='vehicle',
            name='Last_Service',
            field=models.DateField(max_length=10),
        ),
        migrations.AlterField(
            model_name='vehicle',
            name='Purchase_Date',
            field=models.DateField(max_length=50),
        ),
        migrations.AlterField(
            model_name='vehicle',
            name='VIN',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='vehicle',
            name='Year',
            field=models.CharField(max_length=10),
        ),
        migrations.AlterField(
            model_name='vehicle',
            name='make',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='vehicle',
            name='model',
            field=models.CharField(default='', max_length=50),
            preserve_default=False,
        ),
    ]
