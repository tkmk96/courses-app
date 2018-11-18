# Generated by Django 2.1.3 on 2018-11-12 22:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
            ],
        ),
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256)),
                ('description', models.CharField(max_length=1024)),
                ('price', models.DecimalField(decimal_places=2, max_digits=5)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.Category')),
            ],
        ),
        migrations.CreateModel(
            name='CourseUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(auto_now_add=True)),
                ('rating', models.FloatField(blank=True, null=True)),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.Course')),
            ],
        ),
        migrations.CreateModel(
            name='RecommendationForUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.IntegerField()),
                ('recommended_course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.Course')),
            ],
        ),
        migrations.CreateModel(
            name='RecommendationPeopleBuy',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.IntegerField()),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='course_for2', to='api.Course')),
                ('recommended_course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='course_offered2', to='api.Course')),
            ],
        ),
        migrations.CreateModel(
            name='RecommendationSimilarCourse',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.IntegerField()),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='course_for', to='api.Course')),
                ('recommended_course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='course_offered', to='api.Course')),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128, unique=True)),
            ],
        ),
        migrations.AddField(
            model_name='recommendationforuser',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.User'),
        ),
        migrations.AddField(
            model_name='courseuser',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.User'),
        ),
    ]
