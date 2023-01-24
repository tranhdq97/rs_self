# Generated by Django 4.1.5 on 2023-01-24 12:48

import base.common.constant.db_table
import base.common.constant.master
import base.common.models.managers
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('profile', '0001_initial'),
        ('master', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Staff',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('is_deleted', models.BooleanField(default=False)),
                ('email', models.EmailField(max_length=255, unique=True, verbose_name='email address')),
                ('is_active', models.BooleanField(default=True)),
                ('is_leave', models.BooleanField(default=False)),
                ('is_admin', models.BooleanField(default=False)),
                ('profile', models.OneToOneField(null=True, on_delete=django.db.models.deletion.RESTRICT, related_name=base.common.constant.db_table.DBTable['STAFF'], to='profile.profile')),
                ('type', models.ForeignKey(default=base.common.constant.master.MasterStaffTypeID['UNAPPROVED'], on_delete=django.db.models.deletion.RESTRICT, related_name=base.common.constant.db_table.DBTable['STAFF'], to='master.masterstafftype')),
            ],
            options={
                'db_table': base.common.constant.db_table.DBTable['STAFF'],
            },
            managers=[
                ('objects', base.common.models.managers.CustomUserManager()),
            ],
        ),
    ]
