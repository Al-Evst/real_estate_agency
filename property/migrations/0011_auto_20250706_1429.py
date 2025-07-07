from django.db import migrations


def link_owners_to_flats(apps, schema_editor):
    Flat = apps.get_model('property', 'Flat')
    Owner = apps.get_model('property', 'Owner')

    for flat in Flat.objects.all():
        if not flat.owner:
            continue

        owner, _ = Owner.objects.get_or_create(
            full_name=flat.owner,
            phone_number=flat.owners_phonenumber,
            defaults={'pure_phone': flat.owner_pure_phone}
        )

        owner.flats.add(flat)


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0010_owner'), 
    ]

    operations = [
        migrations.RunPython(link_owners_to_flats),
    ]