from django.db import models











class Category(models.Model):
    name=models.CharField(max_length=200)

    def to_json(self):
        return {
            'id': self.id,
            'name': self.name,


        }




class Product(models.Model):
    name = models.CharField(max_length=200)
    price = models.FloatField(max_length=200)
    description = models.TextField(max_length=200)
    count = models.IntegerField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return '{}: {}'.format(self.id, self.name)


    def to_json(self):
        return {
                'id': self.id,
                'name': self.name,
                'price': self.price,
                'description': self.description,
                'count': self.count
            }














