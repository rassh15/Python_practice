import email
from django.db import models

# Create your models here.


class Tag(models.Model):
    caption = models.CharField(max_length=20)
    def __str__(self) -> str:
        return f"{self.caption}"

class Author(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email_address = models.EmailField()

    def __str__(self) -> str:
        return f"{self.first_name} {self.last_name}"
    

class Post(models.Model):
    title = models.CharField(max_length=20)
    excerpt = models.CharField(max_length=200)
    image = models.ImageField(upload_to="posts",null=True)
    author = models.ForeignKey(Author, on_delete=models.SET_NULL,null=True)
    date = models.DateTimeField()
    slug = models.SlugField(unique=True)
    content = models.TextField()
    tags = models.ManyToManyField(Tag)

    def __str__(self) -> str:
        return f"{self.title} {self.author}"

class Comment(models.Model):
    user_name = models.CharField(max_length=100)
    user_email = models.EmailField()
    text = models.TextField(max_length=300)
    post = models.ForeignKey(
        "Post", 
        related_name="comments", on_delete=models.CASCADE)
