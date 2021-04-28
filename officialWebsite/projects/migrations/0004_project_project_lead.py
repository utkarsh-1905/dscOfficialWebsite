# Generated by Django 2.2.10 on 2020-04-16 23:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("members", "0012_auto_20200202_1332"),
        ("projects", "0003_auto_20200208_1551"),
    ]

    operations = [
        migrations.AddField(
            model_name="project",
            name="project_lead",
            field=models.ForeignKey(
                default="",
                on_delete=django.db.models.deletion.CASCADE,
                related_name="lead",
                to="members.Member",
            ),
            preserve_default=False,
        ),
    ]