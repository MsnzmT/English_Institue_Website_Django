from django.db import models

# Create your models here.



class Option(models.Model):
    key = models.CharField("کلید", max_length=200, unique=True, null=False, blank=False)
    value = models.CharField("مقدار", max_length=1000, null=True, blank=True)
    is_public = models.BooleanField(default=True)

    @staticmethod
    def get_option(key, default="", include_all=True):
        try:
            option = Option.objects.get(key=key)
            if include_all or option.is_public:
                return option.value
            return default
        except:
            return default

    def __str__(self):
        return self.key