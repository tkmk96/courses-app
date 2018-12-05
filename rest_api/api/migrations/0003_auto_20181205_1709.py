# Generated by Django 2.1.3 on 2018-12-05 16:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_keyword'),
    ]

    operations = [
        migrations.CreateModel(
            name='CourseKeyword',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='keywords', to='api.Course')),
                ('keyword', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='kw_courses', to='api.KeyWord')),
            ],
        ),
        migrations.AlterUniqueTogether(
            name='coursekeyword',
            unique_together={('course', 'keyword')},
        ),
    ]
