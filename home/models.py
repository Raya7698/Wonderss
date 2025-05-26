from tabnanny import verbose

from django.db import models



# Create your models here.

class Main(models.Model):
    site_name = models.CharField(verbose_name="Имя сайта", max_length=50)

    def __str__(self):
        return self.title


class Blog(models.Model):
    photo = models.ImageField(upload_to='home/', blank=True, null=True)
    title = models.CharField("Заголовок", max_length=300)
    description = models.TextField("Описание")
    created_at = models.DateTimeField("Дата создания", auto_now_add=True)

    def __str__(self):
        return self.title


class AboutUs(models.Model):
    photo = models.ImageField(upload_to='about/', blank=True, null=True)
    title = models.CharField("Заголовок", max_length=300)
    description = models.TextField("Описание")


    def __str__(self):
        return self.description

class Gallery(models.Model):
    image = models.ImageField(upload_to='gallery/')

    def __str__(self):
        return self.image.name


class PhotoGallery(models.Model):
    photo = models.ImageField(upload_to='photo/')

    def __str__(self):
        return self.photo.name



class ContactUs(models.Model):
    full_name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=200)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.subject


class Comments(models.Model):
        email = models.EmailField()
        name = models.CharField("Имя", max_length=50)
        content = models.TextField("Комментарий", max_length=2000)
        post = models.ForeignKey(Blog,
            verbose_name='Публикация',
            on_delete=models.CASCADE,
            related_name='comments')
        created_at = models.DateTimeField(auto_now_add=True)

        def __str__(self):
            return f"{self.name} - {self.post}"


        class Meta:
            verbose_name = 'Комментарий'
            verbose_name_plural = 'Комментарии'
