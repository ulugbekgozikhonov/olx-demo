from django.db import models # type: ignore
from users.models import Base, User

class Category(models.Model):
    name = models.CharField(max_length=255, unique=True)
    image = models.ImageField(upload_to='products/categories/', null=True, blank=True)
    slug = models.SlugField(unique=True)
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='subcategories')
    
    def __str__(self):
        return self.name

class Advertisement(Base):
    title = models.CharField(max_length=70, null=False, db_index=True)
    description = models.TextField(null=False)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="advertisements")
    price = models.DecimalField(max_digits=10, decimal_places=2)
    seller = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True, related_name='advertisements')
    is_new = models.BooleanField(default=False)
    address = models.CharField(max_length=100)
    status = models.BooleanField(default=True)
    contact_number = models.CharField(max_length=25)
    bitm = models.CharField(max_length=55)
    
    
    
class AdvertisementImage(Base):
    advertisement = models.ForeignKey(Advertisement, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to='products/', null=False)