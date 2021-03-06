from django.db import models
from Book.models import Book
from Order.models import BookInUse
from django.contrib.auth.models import (
    AbstractBaseUser,
    AbstractUser)


# Create your models here.

class User(models.Model):
    qr_number = models.CharField(max_length=16)
    full_name = models.CharField(max_length=256)
    logo = models.ImageField(name="Аватар", upload_to='img/users')
    role = models.CharField(max_length=20)
    # university = models.ForeignKey('University.University', on_delete=models.PROTECT, related_name='Университет')
    faculty = models.ForeignKey('University.Faculty', on_delete=models.PROTECT, related_name='Факультет')

    # reading_books = models.ManyToManyField(Book, name='Полученные книги')

    # used_books = models.ManyToManyField(Book, name='Сданные книги', default='')
    # time_of_get_book = models.ManyToManyField(BookInUse)

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

    def __str__(self):
        return self.full_name

    def __unicode__(self):
        return self.full_name


#
# class MyUserManager(BaseUserManager):
#     def create_user(self, email, date_of_birth, password=None):
#         """
#         Creates and saves a User with the given email, date of
#         birth and password.
#         """
#         if not email:
#             raise ValueError('Users must have an email address')
#
#         user = self.model(
#             email=self.normalize_email(email),
#             date_of_birth=date_of_birth,
#         )
#
#         user.set_password(password)
#         user.save(using=self._db)
#         return user
#
#     def create_superuser(self, email, date_of_birth, password=None):
#         """
#         Creates and saves a superuser with the given email, date of
#         birth and password.
#         """
#         user = self.create_user(
#             email,
#             password=password,
#             date_of_birth=date_of_birth,
#         )
#         user.is_admin = True
#         user.save(using=self._db)
#         return user
#
#
# class MyUser(AbstractBaseUser):
#     email = models.EmailField(
#         verbose_name='email address',
#         max_length=255,
#         unique=True,
#     )
#     date_of_birth = models.DateField()
#     is_superuser = models.BooleanField(default=True)
#     is_active = models.BooleanField(default=True)
#     is_admin = models.BooleanField(default=False)
#     university_id = models.ForeignKey('User.User', on_delete=models.PROTECT, related_name='Университет')
#     objects = MyUserManager()
#     USERNAME_FIELD = 'email'
#     REQUIRED_FIELDS = ['date_of_birth', 'university_id', ]
#
#     def __str__(self):
#         return self.email
#
#     def has_perm(self, perm, obj=None):
#         "Does the user have a specific permission?"
#         # Simplest possible answer: Yes, always
#         return True
#
#     def has_module_perms(self, app_label):
#         "Does the user have permissions to view the app `app_label`?"
#         # Simplest possible answer: Yes, always
#         return True
#
#     @property
#     def is_staff(self):
#         "Is the user a member of staff?"
#         # Simplest possible answer: All admins are staff
#         return self.is_admin

#
class Profile(AbstractUser):
    university_id = models.ForeignKey('University.University', on_delete=models.PROTECT, related_name='Университет')
    location = models.CharField(max_length=30, blank=True)
    birth_date = models.DateField(null=True, blank=True)

    class Meta:
        verbose_name = 'Админ'
        verbose_name_plural = 'Админ'

    def __str__(self):
        return "{}".format(self.university_id)
