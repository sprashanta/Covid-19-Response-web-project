# Generated by Django 2.2.5 on 2021-05-01 09:53

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('SuperAdmin', '0002_auto_20210501_1553'),
        ('patient', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='vaccine',
            name='patient_name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='vaccine_patient_name', to=settings.AUTH_USER_MODEL, verbose_name='Patient Name'),
        ),
        migrations.AddField(
            model_name='oxygencylinderbooking',
            name='hospital_name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='oxygen_cylinder_booking_hospital_name', to='SuperAdmin.Hospital', verbose_name='Hospital Name'),
        ),
        migrations.AddField(
            model_name='oxygencylinderbooking',
            name='patient_name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='oxygen_cylinder_booking_patient_name', to=settings.AUTH_USER_MODEL, verbose_name='Patient Name'),
        ),
        migrations.AddField(
            model_name='makeappointment',
            name='doctor_name',
            field=models.ForeignKey(blank=True, limit_choices_to={'is_doctor': True}, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='doctor_name', to=settings.AUTH_USER_MODEL, verbose_name='Doctor Name'),
        ),
        migrations.AddField(
            model_name='makeappointment',
            name='patient_name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='patient_name', to=settings.AUTH_USER_MODEL, verbose_name='Patient Name'),
        ),
        migrations.AddField(
            model_name='icubedbooking',
            name='hospital_name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='icu_bed_booking_hospital_name', to='SuperAdmin.Hospital', verbose_name='Hospital Name'),
        ),
        migrations.AddField(
            model_name='icubedbooking',
            name='patient_name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='icu_bed_booking_patient_name', to=settings.AUTH_USER_MODEL, verbose_name='Patient Name'),
        ),
    ]
