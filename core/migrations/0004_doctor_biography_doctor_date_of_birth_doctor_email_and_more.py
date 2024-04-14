# Generated by Django 5.0.4 on 2024-04-13 23:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0003_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="doctor",
            name="biography",
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name="doctor",
            name="date_of_birth",
            field=models.DateField(default=None),
        ),
        migrations.AddField(
            model_name="doctor",
            name="email",
            field=models.EmailField(default=None, max_length=254, unique=True),
        ),
        migrations.AddField(
            model_name="doctor",
            name="experience_years",
            field=models.PositiveIntegerField(default=None),
        ),
        migrations.AddField(
            model_name="doctor",
            name="gender",
            field=models.CharField(
                choices=[("M", "Male"), ("F", "Female"), ("O", "Other")],
                default=None,
                max_length=1,
            ),
        ),
        migrations.AddField(
            model_name="doctor",
            name="location",
            field=models.CharField(default=None, max_length=100),
        ),
        migrations.AddField(
            model_name="doctor",
            name="phone_number",
            field=models.CharField(blank=True, default=None, max_length=15, null=True),
        ),
        migrations.AddField(
            model_name="doctor",
            name="profile_picture",
            field=models.ImageField(
                blank=True, null=True, upload_to="doctor_profiles/"
            ),
        ),
        migrations.AddField(
            model_name="doctor",
            name="specialization",
            field=models.CharField(default=None, max_length=100),
        ),
    ]
