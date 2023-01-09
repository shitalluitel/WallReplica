from django.db import models

# Create your models here.
class Post(models.Model):
    text = models.TextField(max_length=10000, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)
    is_hidden = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self) -> str:
        return self.text

    class Meta:
        ordering = ('created_at', )
        verbose_name = 'Post'
        verbose_name_plural = 'Posts'