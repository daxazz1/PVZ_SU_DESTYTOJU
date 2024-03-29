# Generated by Django 4.0.4 on 2022-05-09 16:20

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('projects', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, null=True, verbose_name='Name')),
                ('lastname', models.CharField(max_length=200, null=True, verbose_name='Lastname')),
                ('company', models.CharField(max_length=200, verbose_name='Company')),
                ('contacts', models.CharField(max_length=200, null=True, verbose_name='Contacts')),
            ],
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='Name')),
                ('lastname', models.CharField(max_length=200, verbose_name='Lastname')),
                ('position', models.CharField(max_length=200, null=True, verbose_name='Pareigos')),
            ],
        ),
        migrations.AddField(
            model_name='project',
            name='end_date',
            field=models.DateField(null=True, verbose_name='End date'),
        ),
        migrations.AddField(
            model_name='project',
            name='manager',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL, verbose_name='Manager'),
        ),
        migrations.AlterField(
            model_name='project',
            name='start_date',
            field=models.DateField(null=True, verbose_name='Start date'),
        ),
        migrations.CreateModel(
            name='Job',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='Title')),
                ('info', models.TextField(null=True, verbose_name='Information')),
                ('project', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='jobs', to='projects.project', verbose_name='Project')),
            ],
        ),
        migrations.CreateModel(
            name='Invoice',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(null=True, verbose_name='Date')),
                ('info', models.TextField(null=True, verbose_name='Information')),
                ('total', models.FloatField(verbose_name='Total')),
                ('project', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='invoices', to='projects.project', verbose_name='Project')),
            ],
        ),
        migrations.AddField(
            model_name='project',
            name='client',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='projects.client'),
        ),
        migrations.AddField(
            model_name='project',
            name='employees',
            field=models.ManyToManyField(to='projects.employee', verbose_name='Employees'),
        ),
    ]
