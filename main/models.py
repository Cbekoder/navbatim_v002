from django.db import models



class Category(models.Model):
    name = models.CharField(max_length=100)
    icon = models.CharField(max_length=10)

    def __str__(self):
        return self.name


class Service(models.Model):
    name = models.CharField(max_length=200)
    address = models.CharField(max_length=255)
    image = models.ImageField(upload_to='services/', null=True, blank=True)
    rating = models.DecimalField(max_digits=3, decimal_places=1, null=True, blank=True)
    reviews_count = models.IntegerField(default=0)
    is_award_winner = models.BooleanField(default=False)
    award_year = models.CharField(max_length=10, null=True, blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='services')
    is_vip = models.BooleanField(default=False)
    is_company = models.BooleanField(default=True)  # False means it's a specialist

    def __str__(self):
        return self.name

    @property
    def rating_display(self):
        if self.rating:
            return f"{self.rating} ({self.reviews_count})"
        return None

    @property
    def award_display(self):
        if self.is_award_winner and self.award_year:
            return f"AWARDS '{self.award_year}"
        return None
