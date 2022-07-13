from django.db import models


# define author model
class Author(models.Model):
    full_name = models.CharField(
        verbose_name="author full name",
        max_length=100
    )
    # Leaving these out for now
    # created_at = models.DateTimeField(auto_now_add=True)
    # updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.full_name


# since we know we will need a picture at some point but not details about it, we cna create a placeholder model
class Picture(models.Model):
    pass


# define article model with many-to-one relationship with Author
class Article(models.Model):
    title = models.CharField(max_length=300)
    body_text = models.TextField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='articles')
    # we know a picture will be used in the future, so for now we are just assuming a many-to-many relationship,
    # since we know an Article can have more than one Pictures, but a Picture could also be featured in many Articles
    pictures = models.ManyToManyField(Picture, related_name='articles')
    # Leaving these out for now
    # created_at = models.DateTimeField(auto_now_add=True)
    # updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
