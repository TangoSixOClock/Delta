from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from datetime import datetime

class Course(models.Model):
    name = models.CharField(max_length=40,null=False)
    slug = models.CharField(max_length=40,null=False,unique=True)
    description = models.CharField(max_length=300,null=True)
    price = models.IntegerField(null=False)
    discount = models.IntegerField(null=False,default=0)
    active = models.BooleanField(default=False)
    thumbnail = models.ImageField(upload_to='files/thumbnail/')
    date = models.DateTimeField(auto_now_add=True)
    resource = models.FileField(upload_to='files/resource/')
    length = models.IntegerField(null=False)

    def __str__(self):
        return self.name

class CourseProperty(models.Model):
    description = models.CharField(max_length=300,null=False)
    course = models.ForeignKey(Course,null=False,on_delete=models.CASCADE)

    class Meta:
        abstract = True

class Learning(CourseProperty):
    pass

class Chapter(models.Model):
    course = models.ForeignKey(Course,null=True,on_delete=models.CASCADE)
    title =  models.CharField(max_length=100,null=True)
    thumbnail = models.ImageField(upload_to='files/thumbnail/',null=True)
    is_preview = models.BooleanField(default=False)
    slug = models.CharField(max_length=40,null=True,unique=True)
    serial_number = models.IntegerField(null=True)
    number_of_videos = models.IntegerField(null=True)

    def __str__(self):
        return self.title

class Video(models.Model):
    chapter = models.ForeignKey(Chapter,null=True,on_delete=models.CASCADE)
    course = models.ForeignKey(Course,null=True,on_delete=models.CASCADE)
    thumbnail = models.ImageField(upload_to='files/thumbnail/',null=True)
    title =  models.CharField(max_length=100,null=True)
    serial_number = models.IntegerField(null=True)
    video_id = models.CharField(max_length=100,null=True)

    def __str__(self):
        return self.title
    
class UserCourse(models.Model):
    user = models.ForeignKey(User,null=False,on_delete=models.CASCADE)
    course = models.ForeignKey(Course,null=False,on_delete=models.CASCADE)
    course_complete = models.BooleanField(default=False)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.user.username} - {self.course.name}'

class Payment(models.Model):
    order_id = models.CharField(max_length=50,null=False)
    payment_id = models.CharField(max_length=50,null=False)
    usercourse = models.ForeignKey(UserCourse,null=False,blank=True,on_delete=models.CASCADE)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    course = models.ForeignKey(Course,on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)
    status = models.BooleanField(default=False)


class ContactDetail(models.Model):
    name = models.CharField(max_length=50,null=True)
    email = models.EmailField(max_length=50,null=True)
    phone = models.CharField(max_length=20,null=True)
    message = models.CharField(max_length=250,null=True,blank=True)

    def __str__(self):
        return f'{self.name} - {self.email} - {self.phone}'
    
class UserProfile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    name = models.CharField(max_length=50,null=True)
    phone = models.CharField(max_length=20,null=True)
    photo = models.ImageField(upload_to='files/profile/',default='profile.jpg')
    sex = models.CharField(max_length=20,null=True)
    dob = models.CharField(max_length=20,null=True)
    profileid = models.CharField(max_length=30,null=True)
    institude = models.CharField(max_length=60,null=True)
    profession = models.CharField(max_length=30,null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.user.username
    
@receiver(post_save,sender=User)
def create_profile(sender,instance,created,**kwargs):
    if created:
        def generate_token():
            import random

            # Provided string
            full_name = str(instance)

            # Splitting the full name into first and last names
            
            random_letters_first_name = random.sample(full_name[1:], 2)

           

            # Constructing the final string
            result = full_name[0] + ''.join(random_letters_first_name) 

            current_datetime = datetime.now()
            

            # Format the date and time according to the desired format
            token_format = "{:02d}{:02d}{:02d}{:02d}{:02d}{:02d}".format(
                current_datetime.day,
                current_datetime.month,
                current_datetime.year % 100,
                current_datetime.hour,
                current_datetime.minute,
                current_datetime.second
            )

            return result.upper() + token_format
        token = generate_token()
        UserProfile.objects.create(user=instance,profileid=token)

class CouponCode(models.Model):
    code = models.CharField(max_length=6)
    name = models.CharField(max_length=60,null=True)
    pan_number = models.CharField(max_length=20,null=True)
    course = models.ForeignKey(Course,on_delete=models.CASCADE)
    discount = models.IntegerField(default=0)