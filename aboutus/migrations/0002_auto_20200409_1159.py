# Generated by Django 3.0.5 on 2020-04-09 06:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('aboutus', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='aboutus',
            options={'verbose_name': 'About Us', 'verbose_name_plural': 'Abous Us'},
        ),
        migrations.AlterModelOptions(
            name='chef',
            options={'verbose_name': 'Chef', 'verbose_name_plural': 'Chefs'},
        ),
        migrations.AlterModelOptions(
            name='why_choose_us',
            options={'verbose_name': 'Why Choose Us', 'verbose_name_plural': 'Why Choose Us'},
        ),
        migrations.RemoveField(
            model_name='aboutus',
            name='image',
        ),
    ]