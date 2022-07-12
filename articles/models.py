from django.db import models


# define author model
class Author(models.Model):
    full_name = models.CharField(
        verbose_name="author full name",
        max_length=100
    )

    def __str__(self):
        return self.full_name


# since we know we will need a picture at some point but not details about it, we cna create a placeholder model
class Picture(models.Model):
    pass


# define article model
class Article(models.Model):
    title = models.CharField(max_length=300)
    story = models.TextField()
    last_edited = models.DateTimeField('last changed')
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='author')
    # we know a picture will be used in the future, so for now we are just allowing its FK reference to be null
    picture = models.ForeignKey(Picture, on_delete=models.CASCADE, related_name='Picture', null=True)

    def __str__(self):
        return self.title
