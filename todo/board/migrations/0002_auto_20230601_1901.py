# Generated by Django 3.1.5 on 2023-06-01 10:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('board', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProjectCode',
            fields=[
                ('pcode', models.CharField(db_column='PCODE', max_length=4, primary_key=True, serialize=False)),
                ('pname', models.CharField(db_column='PNAME', max_length=100)),
            ],
            options={
                'db_table': 'project_code',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='TodoList',
            fields=[
                ('no', models.AutoField(db_column='NO', primary_key=True, serialize=False)),
                ('pcode', models.CharField(db_column='PCODE', max_length=4)),
                ('user_id', models.CharField(blank=True, db_column='USER_ID', max_length=50, null=True)),
                ('title', models.CharField(blank=True, db_column='TITLE', max_length=200, null=True)),
                ('content', models.CharField(blank=True, db_column='CONTENT', max_length=1000, null=True)),
                ('is_complete', models.IntegerField(blank=True, db_column='IS_COMPLETE', null=True)),
                ('priority', models.IntegerField(blank=True, db_column='PRIORITY', null=True)),
                ('end_date', models.DateField(blank=True, db_column='END_DATE', null=True)),
            ],
            options={
                'db_table': 'todo_list',
                'managed': False,
            },
        ),
        migrations.DeleteModel(
            name='Todo_list',
        ),
    ]
