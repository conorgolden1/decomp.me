# Generated by Django 3.2.4 on 2021-07-03 15:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('coreapp', '0004_auto_20210702_1441'),
    ]

    operations = [
        migrations.CreateModel(
            name='Assembly',
            fields=[
                ('hash', models.CharField(max_length=64, primary_key=True, serialize=False)),
                ('data', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Compiler',
            fields=[
                ('shortname', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Scratch',
            fields=[
                ('slug', models.SlugField(primary_key=True, serialize=False)),
                ('submission_time', models.DateTimeField()),
                ('c_code', models.TextField()),
                ('owner', models.UUIDField()),
                ('assembly', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='coreapp.assembly')),
                ('compiler', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='coreapp.compiler')),
                ('parent', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='coreapp.scratch')),
            ],
        ),
        migrations.RemoveField(
            model_name='submission',
            name='function',
        ),
        migrations.RemoveField(
            model_name='submission',
            name='user',
        ),
        migrations.DeleteModel(
            name='Function',
        ),
        migrations.DeleteModel(
            name='Project',
        ),
        migrations.DeleteModel(
            name='Submission',
        ),
        migrations.DeleteModel(
            name='User',
        ),
    ]
