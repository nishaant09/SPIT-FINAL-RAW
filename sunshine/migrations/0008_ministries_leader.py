
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sunshine', '0007_event_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='ministries',
            name='leader',
            field=models.CharField(max_length=70, null=True),
        ),
    ]
