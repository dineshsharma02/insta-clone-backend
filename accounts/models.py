from email.policy import default
from django.db.models.signals import post_save
from tokenize import Token
from django.conf import settings
from django.db import models
from django.dispatch import receiver
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User

from django.db.models.signals import post_save
from django.dispatch import receiver

####################### CUSTOM USER TO FULFILL PROFILE NEEDS #########################

from django.db import models
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser
)


# class CustomUser(AbstractBaseUser):
#     # email = models.EmailField(
#     #     verbose_name='email address',
#     #     max_length=255,
#     #     unique=True,
#     # )
#     username = models.CharField(max_length=50,unique=True)
#     is_active = models.BooleanField(default=True)
#     staff = models.BooleanField(default=False) # a admin user; non super-user
#     admin = models.BooleanField(default=False) # a superuser
#     bio = models.CharField(default = "",max_length=300)
#     profile_pic = models.ImageField(default="media/dp/def_prof_pic.jpg",upload_to="media/dp/", height_field=None, width_field=None, max_length=100)

#     # notice the absence of a "Password field", that is built in.

#     USERNAME_FIELD = 'username'
#     REQUIRED_FIELDS = [] # username & Password are required by default.

#     def get_full_name(self):
#         # The user is identified by their username address
#         return self.username

#     def get_short_name(self):
#         # The user is identified by their username address
#         return self.username

#     def __str__(self):
#         return self.username

#     def has_perm(self, perm, obj=None):
#         "Does the user have a specific permission?"
#         # Simplest possible answer: Yes, always
#         return True

#     def has_module_perms(self, app_label):
#         "Does the user have permissions to view the app `app_label`?"
#         # Simplest possible answer: Yes, always
#         return True

#     @property
#     def is_staff(self):
#         "Is the user a member of staff?"
#         return self.staff

#     @property
#     def is_admin(self):
#         "Is the user a admin member?"
#         return self.admin


# class UserManager(BaseUserManager):
#     def create_user(self, username, password=None):
#         """
#         Creates and saves a User with the given username and password.
#         """
#         if not username:
#             raise ValueError('Users must have an username address')

#         user = self.model(
#             username=self.normalize_username(username),
#         )

#         user.set_password(password)
#         user.save(using=self._db)
#         return user

#     def create_staffuser(self, username, password):
#         """
#         Creates and saves a staff user with the given username and password.
#         """
#         user = self.create_user(
#             username,
#             password=password,
#         )
#         user.staff = True
#         user.save(using=self._db)
#         return user

#     def create_superuser(self, username, password):
#         """
#         Creates and saves a superuser with the given username and password.
#         """
#         user = self.create_user(
#             username,
#             password=password,
#         )
#         user.staff = True
#         user.admin = True
#         user.save(using=self._db)
#         return user

# # hook in the New Manager to our Model
# class User(AbstractBaseUser): # from step 2
#     ...
#     objects = UserManager()



################ MODEL TO STORE USER FOLLOWER DATA ##############################

class UserFollower(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE,related_name='user_id')
    follower_id = models.ForeignKey(User, on_delete=models.CASCADE)
    follow_status = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('user_id','follower_id')

################## PROFILE DATA EXTENDING USER ONE TO ONE FIELD #######################
class Profile(models.Model):
    # user = models.OneToOneField(User, on_delete=models.CASCADE,primary_key=True)
    user = models.ForeignKey(User,unique=True, on_delete=models.CASCADE)
    image = models.ImageField(default="def_prof_pic.jpg",upload_to='media/profile_photos')
    gender = models.CharField(default="male",max_length=50)
    # def __str__(self):
    #     return f'{self.user.username}'

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):

    instance.Profile.save()


