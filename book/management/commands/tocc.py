import json

from django.core.management.base import BaseCommand
from django.core.serializers.json import Serializer

from book.models import Book, City


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

        for item in data:
            row = [item[i] for i in header]
            writer.writerow(dict(zip(header, row)))

    def handle(self, *args, **options):
        from book.models import Book
        from book.models import Publisher

        book = Book.objects.all()
        # for item in book:
        #     print(item)
        data = JSONSerializer().serialize(book, fields=['title', 'description', 'publisher'])
        self.render_to_excel(data)


def get_field_name_types(self):
    attributes = dir(self)
    type_names = [eval("type(self." + dir(self)[i] + ").__name__") for i in range(len(dir(self)))]
    item = list(set([attributes[i] if type_names[i] == 'ForeignKeyDeferredAttribute'
                     else '' for i in range(len(attributes))]))
    item.remove('')
    return item[0] if len(item) > 0 else None


def graph(node):
    print([item.to_excel() for item in node])


class JSONSerializer(Serializer):
    def get_dump_object(self, obj, node=[]):
        node.append(obj)
        fk = get_field_name_types(obj.__class__)
        if fk is not None:
            attr = fk.split('_')[0]
            self.get_dump_object(eval(f'obj.{attr}'))
        else:
            graph(node)
            node.clear()
        self._current[obj._meta.pk.name] = obj._get_pk_val()
        return self._current
