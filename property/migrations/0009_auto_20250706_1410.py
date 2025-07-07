from django.db import migrations
import phonenumbers


def normalize_phone_numbers(apps, schema_editor):
    Flat = apps.get_model('property', 'Flat')

    for flat in Flat.objects.all():
        raw_number = flat.owners_phonenumber
        try:
            parsed_number = phonenumbers.parse(raw_number, 'RU')
            if phonenumbers.is_valid_number(parsed_number):
                flat.owner_pure_phone = phonenumbers.format_number(
                    parsed_number,
                    phonenumbers.PhoneNumberFormat.E164
                )
                flat.save()
        except phonenumbers.NumberParseException:
            
            continue


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0008_flat_owner_pure_phone'),  
    ]

    operations = [
        migrations.RunPython(normalize_phone_numbers),
    ]