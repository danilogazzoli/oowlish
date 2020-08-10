from customers.models import Customer
from django.core.management.base import BaseCommand, CommandError
import csv
from .maps import Maps


class Command(BaseCommand):
    """
    Base command used for importing customers in a CSV file.
    This file must contain the columns:
     "first_name", "last_name", "email", "gender", "company", "city", "title", "latitude", "longitude"
    """
    help = "Imports a .csv file with customers' names and inserts them into database."

    def add_arguments(self, parser):
        parser.add_argument('file', type=str, help='CSV File name (Ex.: customers.csv).')

    def handle(self, *args, **options):
        filename = options['file']
        if not filename:
            raise CommandError('No file was specified.')
        errors = False
        customers = []
        maps = Maps()
        with open(filename, 'r', newline='', encoding='utf-8') as file:
            reader = csv.DictReader(file, delimiter=',')
            try:
                for row in reader:
                    print(f'Id to be imported:{row["id"]}')
                    coord = maps.get_coords(row['city'])
                    customers.append(Customer(first_name=row['first_name'],
                                              last_name=row['last_name'],
                                              email=row['email'],
                                              gender=row['gender'],
                                              company=row['company'],
                                              city=row['city'],
                                              title=row['title'],
                                              latitude= coord['Latitude'],
                                              longitude=coord['Longitude']))
            except KeyError:
                # File structure is incorrect, its first column must be "name".
                errors = True
        if errors:
            self.stdout.write(self.style.ERROR('File has incorrect format. It''s missing a "name" column.'))
            return
        created = Customer.objects.bulk_create(customers, ignore_conflicts=True)
        count = len(created)
        if not count:
            self.stdout.write(self.style.WARNING('File was imported but no customer was registered.'))
            return
        self.stdout.write(
            self.style.SUCCESS(
                f'Successfully imported customer file and registered {count} '
                f'customer{"s" if count != 1 else ""}. '
            )
        )

