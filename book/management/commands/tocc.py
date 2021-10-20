import json

from django.core.management.base import BaseCommand
from django.core.serializers.json import Serializer


class Command(BaseCommand):

    def get_header(self, data: list):
        return list(data[0].keys())

    def render_to_excel(self, data):
        data = json.loads(data)
        header = self.get_header(data)
        import csv
        output = open("category.csv", 'w')
        writer = csv.DictWriter(output, fieldnames=header, dialect='excel', delimiter=',')
        writer.writeheader()

        for index, item in enumerate(data):
            row = [item[i] for i in header]
            writer.writerow(dict(zip(header, row)))

    def handle(self, *args, **options):
        from book.models import Book

        obj = Book.objects.all()
        data = JSONSerializer().serialize(obj, fields=["title", "description"])
        self.render_to_excel(data)


class JSONSerializer(Serializer):
    def get_dump_object(self, obj):
        self._current[obj._meta.pk.name] = obj._get_pk_val()
        return self._current
