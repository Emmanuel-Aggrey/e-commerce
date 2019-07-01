from django.db import models
from django.urls import reverse


class Category(models.Model):
    name = models.CharField(max_length=150, db_index=True)
    slug = models.SlugField(max_length=150, unique=True ,db_index=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    image = models.ImageField(upload_to='category_img/%Y/%m/%d', blank=False,null=True)
   
  
    class Meta:
        ordering = ('-created_at', )
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('shop:product_list_by_category', args=[self.slug])


class Product(models.Model):
    category = models.ForeignKey(Category, related_name='products_img', on_delete=models.CASCADE)
    name = models.CharField(max_length=100, db_index=True)
    slug = models.SlugField(max_length=100, db_index=True)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    available = models.BooleanField(default=True)
    stock = models.PositiveIntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    image = models.ImageField(upload_to='products_img/%Y/%m/%d', blank=False,null=True)
    image1 = models.ImageField(upload_to='products_img/%Y/%m/%d', blank=True,null=True)
    image2 = models.ImageField(upload_to='products_img/%Y/%m/%d', blank=True,null=True)
    image3 = models.ImageField(upload_to='products_img/%Y/%m/%d', blank=True,null=True)





    class Meta:
        ordering = ('-name', )
        index_together = (('id', 'slug'),)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('shop:product_detail', args=[self.id, self.slug])

# work on this later
class Gallary(models.Model):
    image1 = models.ImageField(upload_to='gallary_img/%Y/%m/%d', blank=True,null=True)
    image2 = models.ImageField(upload_to='gallary_img/%Y/%m/%d', blank=True,null=True)
    image3 = models.ImageField(upload_to='gallary_img/%Y/%m/%d', blank=True,null=True)
    image4 = models.ImageField(upload_to='gallary_img/%Y/%m/%d', blank=True,null=True)
    image5 = models.ImageField(upload_to='gallary_img/%Y/%m/%d', blank=True,null=True)
    image6 = models.ImageField(upload_to='gallary_img/%Y/%m/%d', blank=True,null=True)


    def __str__(self):
        return f'gallary' 
