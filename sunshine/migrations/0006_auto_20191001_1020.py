
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sunshine', '0005_auto_20191001_1009'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='eventinfo',
            field=models.TextField(max_length=850, null=True),
        ),
    ]
