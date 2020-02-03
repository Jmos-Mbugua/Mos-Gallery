from django.db import models



# from .models import CustomUser
# Create your models here.
class Category(models.Model):
    image_category = models.CharField(max_length=200)

    def __str__(self):
        return self.image_category

    def save_category(self):
        '''
        This method saves the post
        '''
        return self.save()



class Location(models.Model):
    image_location = models.CharField(max_length=200)

    def __str__(self):
        return self.image_location

    def save_location(self):
        '''
        This method saves the post's location
        '''
        return self.save()

    @classmethod 
    def find_images_by_location(cls, id):
        return cls.objects.filter(image_location_id = id)




class Post(models.Model):
    image = models.ImageField(upload_to='images')
    title = models.CharField(max_length=200)
    image_description = models.TextField()
    post_date = models.DateTimeField(auto_now_add=True)
    category = models.ManyToManyField(Category)
    image_location = models.ForeignKey(Location, on_delete=models.CASCADE)
    
    def __str__(self):
        '''
        returns a string representation
        '''
        return self.title


    def save_post(self):
        '''
        This method saves the post
        '''
        return self.save()

    @classmethod
    def delete_post(cls, id):
        '''
        Method that deletes a post
        '''
        return cls.objects.filter(id = id).delete()


  
    @classmethod
    def show_all_posts(cls):
        """
        A method to return all photos posted in order of the most recent to oldest
        """
        return cls.objects.order_by("post_date")[::-1]

    @classmethod
    def search_photo_by_category(cls, search):
        """
        A method to return all photos that fall under a certain catergory
        """
        return cls.objects.filter(category__image_category__icontains = search)

    @classmethod
    def filter_by_location(cls, id):
        """
        A method to filter all photos based on the location in which they were taken
        """
        return cls.objects.filter(image_location__id = id)
    
    @classmethod
    def get_photo_by_id(cls, id):
        """
        A method to get a photo based on its id
        """
        return cls.objects.filter(id = id)[0]

    


    




