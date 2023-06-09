# Generated by Django 4.2 on 2023-05-06 11:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created at')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Updated at')),
                ('name', models.CharField(max_length=255, verbose_name='Name')),
                ('price', models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=12, null=True)),
                ('marja', models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=12, null=True)),
                ('package_code', models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=12, null=True)),
            ],
            options={
                'verbose_name': 'Product',
                'verbose_name_plural': 'Products',
            },
        ),
    ]
