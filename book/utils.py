from book.models import Book


def render_to_excel(a):
    import csv
    header = ['Category1', 'Category1.1', 'url']
    output = open("category.csv", 'w')
    writer = csv.DictWriter(output, fieldnames=header, dialect='excel', delimiter=',')
    writer.writeheader()

    for b in a:
        data = []
        data.append(b['title'])
        data.append("")
        data.append(b['url'])
        writer.writerow(dict(zip(header, data)))
        data = []
        for i in range(len(b['subCategory'])):
            data.append(b['title'])
            data.append(b['subCategory'][i]['title'])
            data.append(b['subCategory'][i]['url'])
            writer.writerow(dict(zip(header, data)))

from django.core import serializers

obj = Book.objects.all()
serialized_obj = serializers.serialize('json', [ obj, ])
a = [{"description": "https://www.amazon.com/Best-Sellers-Appliances-Cooktops/zgbs/appliances/3741261",
      "title": "Cooktops"
      },
     {"description": "https://www.amazon.com/Best-Sellers-Appliances-Dishwashers/zgbs/appliances/3741271",
      "title": "Built-In Dishwashers"
      }]
render_to_excel(a)
