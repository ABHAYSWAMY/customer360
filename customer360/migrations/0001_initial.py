from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=100)),
                ('phone', models.CharField(max_length=20)),
                ('address', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Interaction',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('interaction_date', models.DateField(auto_now_add=True)),
                ('channel', models.CharField(choices=[('email', 'Email'), ('phone', 'Phone'), ('chat', 'Chat'), ('in_person', 'In Person')], max_length=32)),
                ('direction', models.CharField(choices=[('inbound', 'Inbound'), ('outbound', 'Outbound')], max_length=16)),
                ('summary', models.TextField(blank=True)),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='interactions', to='customer360.customer')),
            ],
        ),
    ]
