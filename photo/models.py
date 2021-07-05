from django.db import models

#  Create your models here.
class Location(models.Model):
    photo_location = models.CharField(max_length =30)

    
    def save_location(self):
        self.save()
    
    def delete_location(self):
        self.delete()
    
    def update_location(self, update):
        self.photo_location = update
        self.save()  

    @classmethod
    def get_location_id(cls, id):
        locate = Location.objects.get(pk = id)
        return locate
    def __str__(self):
        return self.photo_location 

class Category(models.Model):
    photo_category = models.CharField(max_length =30)

    def save_category(self):
        self.save()

    def delete_category(self):
        self.delete()
    
    def update_category(self, update):
        self.photo_category = update
        self.save()
    def get_category_id(cls,id):
        category = Category.object.get(pk = id)
        return category

    def __str__(self):
        return self.photo_category 

class Image(models.Model):
    title = models.CharField(max_length =30)
    description = models.TextField(max_length =30)
    image = models.ImageField(upload_to = 'photos/', default='No image')
    location = models.ForeignKey(Location,on_delete=models.CASCADE,)
    category = models.ForeignKey(Category,on_delete=models.CASCADE,)
    pub_date = models.DateTimeField(auto_now_add=True, null=True) 

    def save_image(self):
        self.save()

    def delete_image(self):
        self.delete()

    @classmethod
    def update_image(cls,id,title,description,image,location,category,pub_date):
        image = cls.objects.filter(id = id).update(title =title,image = image,pub_date=pub_date,description = description ,location = location,category = category)

    classmethod
    def get_all_images(cls):
        all_images = Image.objects.all()
        return all_images
    
    @classmethod
    def get_image_by_id(cls, id):
        image = Image.objects.get(id=id)
        return image    

    @classmethod
    def search_by_category(cls,image_category):
        image = Image.objects.filter(image_category__name__icontains=image_category)
        return image_category   

    @classmethod
    def filter_by_location(cls, image_location):
       images_location = Image.objects.filter(image_location__id=image_location)
       return images_location 

    def __str__(self):
        return self.name
    class Meta:
        ordering = ['name']

