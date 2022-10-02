from django.db import models
from django.template.defaultfilters import slugify


class Fromage(models.Model):
    PATEMOLLES = "PMO"
    PATEPRESSESCUITES = "PPC"
    PATEFLEURIES = "PFL"
    FROMAGEDECHEVRES = "FCH"
    FROMAGEDEBREBIS = "FBR"
    PATEPERSILLEES = "PPE"
    TRIPLECREMES = "TCR"
    PATEFORTES = "PFO"

    COMPOSITION = [
        (PATEMOLLES, "patemolles"),
        (PATEPRESSESCUITES, "patepresseescuites"),
        (PATEFLEURIES, "patefleuries"),
        (FROMAGEDECHEVRES, "fromagedechevres"),
        (FROMAGEDEBREBIS, "fromagedebrebis"),
        (PATEPERSILLEES, "patepersillees"),
        (TRIPLECREMES, "triplecremes"),
        (PATEFORTES, "patefortes"),
    ]

    name = models.CharField(max_length=150)
    slug = models.SlugField(max_length=150, unique=True, blank=True)
    origin = models.CharField(max_length=100, blank=True, verbose_name="origine")
    category = models.CharField(max_length=100, blank=True, choices=COMPOSITION, verbose_name="categories")
    description = models.TextField(blank=True)
    composition = models.CharField(max_length=100, blank=True)
    stock = models.BooleanField(default=False)
    thumbnail = models.ImageField(upload_to="Fromages", blank=True, null=True)
    price = models.FloatField(blank=True, null=True, verbose_name="prix")

    class Meta:
        verbose_name = "Les fromage"

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)
