# Generated by Django 3.0.5 on 2020-04-13 18:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('questions', '0002_auto_20200414_0017'),
    ]

    operations = [
        migrations.RenameField(
            model_name='questions',
            old_name='question_1_sample_2',
            new_name='question_1_sample_output_1',
        ),
        migrations.RemoveField(
            model_name='questions',
            name='question_1_sample_3',
        ),
        migrations.RemoveField(
            model_name='questions',
            name='question_1_sample_4',
        ),
    ]
