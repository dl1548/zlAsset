# Generated by Django 2.1.4 on 2019-01-05 17:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hdServer', '0002_auto_20190101_1957'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cert',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ip', models.CharField(blank=True, max_length=128, null=True)),
                ('way', models.CharField(blank=True, max_length=128, null=True)),
                ('username', models.CharField(blank=True, max_length=128, null=True)),
                ('password', models.CharField(blank=True, max_length=128, null=True)),
            ],
        ),
    ]
