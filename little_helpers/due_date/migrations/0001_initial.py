# Generated by Django 3.0.3 on 2020-03-17 10:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DueAction',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Name the action that has to be done', max_length=100)),
                ('first_exec_date', models.DateField(auto_now=True, help_text='First time this action has to be executed')),
                ('last_exec_date', models.DateField(auto_now=True, help_text='Last time this action was executed')),
                ('exec_frequency', models.IntegerField(default=1)),
                ('exec_interval', models.CharField(choices=[('d', 'daily'), ('w', 'weekly'), ('m', 'monthly'), ('y', 'yearly')], default='w', help_text='Interval this has to be done.', max_length=1)),
            ],
            options={
                'ordering': ['-first_exec_date'],
            },
        ),
    ]
