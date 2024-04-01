from django.db import models

# Create your models here.

class IceCream(models.Model):
    fullname=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    phone=models.CharField(max_length=100)
    message=models.CharField(max_length=100)


"""class TagStatus(models.Model):
    user = models.ForeignKey(User, null=True, unique=True)
    status = models.CharField(max_length=2, choices=tag_statuses)
    tag = models.ForeignKey(Tag, null=True, blank=True)

    def __unicode__(self):
        return self.status

    def save(self, *args, **kwargs):
        super(TagStatus, self).save(*args, **kwargs)
        """