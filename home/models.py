from django.db import models

class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=200)
    message = models.TextField()
    is_answered = models.BooleanField(default=False)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    class Meta: 
        ordering = ['-created_date']
        verbose_name = 'Contact'
        verbose_name_plural = 'Cotanct Messages'

    def __str__(self):
        return f"{self.subject}: {self.name}"
    
class NewsLetter(models.Model):
    email = models.EmailField()
    created_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_date']
        verbose_name = 'News Letter'
        verbose_name_plural = 'News Letter Emails'

    def __str__(self):
        return self.email

