import csv
from django.core.management.base import BaseCommand
from django.apps import apps


class Command(BaseCommand):
    help = 'Import data from CSV file into a specified model'

    def add_arguments(self, parser):
        parser.add_argument('model_name', type=str, help='Name of the model to import into')
        parser.add_argument('csv_file', type=str, help='Path to the CSV file')
        parser.add_argument('--batch-size', type=int, default=1000, help='Number of rows to process in each batch')

    def handle(self, *args, **options):
        model_name = options['model_name']
        csv_file_path = options['csv_file']
        batch_size = options['batch_size']

        try:
            model = apps.get_model(app_label='ecommerce_app2', model_name=model_name)
            fields = model._meta.fields

            with open(csv_file_path, 'r') as csv_file:
                reader = csv.reader(csv_file)
                next(reader)  # Skip header row

                related_instances_cache = {} # store related instances to reduce querying db

                instances = []
                for i, row in enumerate(reader, start=1):
                    instance = model()
                    for j, field in enumerate(fields):
                        field_name = field.name
                        field_type = field.get_internal_type()

                    
                        if field_type == 'ForeignKey':
                            related_model = model._meta.get_field(f'{field_name}').remote_field.model
                            field_name = field_name + '_id' # django adds '_id' to foriegn key names
                            # related_instance = related_model.objects.get(**{f'{field_name}':row[j]})

                            # check instances cache before querying db
                            if row[j] in related_instances_cache:
                                related_instance = related_instances_cache[row[j]]

                            else:
                                # related_model = model._meta.get_field(f'{field_name}').remote_field.model
                                # field_name = field_name + '_id' # django adds '_id' to foreign key names
                                related_instance = related_model.objects.get(**{f'{field_name}':row[j]})
                                related_instances_cache[row[j]] = related_instance

                            setattr(instance, field_name, row[j])

                        elif field_type == 'IntegerField':
                            setattr(instance, field_name, int(row[j]))
                        else:
                            setattr(instance, field_name, row[j])
                    instances.append(instance)

                    if i % batch_size == 0:
                        model.objects.bulk_create(instances)
                        instances = []

                if instances:
                    model.objects.bulk_create(instances)

            self.stdout.write(self.style.SUCCESS('Data import successful'))
        except LookupError:
            self.stderr.write(self.style.ERROR('Model not found'))
        except FileNotFoundError:
            self.stderr.write(self.style.ERROR('CSV file not found'))
        except csv.Error as e:
            self.stderr.write(self.style.ERROR(f'Error reading CSV file: {str(e)}'))
        except Exception as e:
            self.stderr.write(self.style.ERROR(f'An error occurred during data import: {str(e)}, {field_name}<>{row[j]}'))


# Usage: python manage.py import_data your_model_name your_csv_file.csv --batch-size 1000


# Usage: python manage.py import_data your_model_name your_csv_file.csv --batch-size 1000

# change Aisles with registered models and the csv file associated with this. Can put this in docker to automatically do this 
