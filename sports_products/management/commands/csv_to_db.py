import os
import csv

from django.core.management.base import BaseCommand, CommandError
from django.conf import settings

from sports_products.models import Order

CSV_DIR = os.path.join(settings.BASE_DIR, 'data')


class Command(BaseCommand):
    args = 'No arguments.'
    help = 'Dump data to db from csv.'

    def handle(self, *args, **options):
        try:
            with open(os.path.join(CSV_DIR, 'Test-Orders_DB.csv'), 'rU') as csv_file:
                reader = csv.DictReader(csv_file)

                for row in reader:
                    try:
                        if row['order_status'] == 'Active':
                            status = 'A'
                        else:
                            status = 'C'

                        if is_number(row['cost_price']):
                            cost_price = float(row['cost_price']) * 66
                        else:
                            cost_price = None

                        Order.objects.get_or_create(
                            status=status,
                            order_id=row['order_id'],
                            product_name=row['product_name'],
                            product_url=row['product_url'],
                            cost_price=cost_price
                        )
                    except Exception as exc:
                        print exc

            self.stdout.write("All CSV dumped successfully.")

        except Exception as exc:
            raise CommandError(str(exc))


def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        return False
