from django.db import models


class TimeStampedModel(models.Model):
    """
    Abstract model for created and modified dates
    """

    created = models.DateTimeField(auto_now_add=True, db_index=True)
    modified = models.DateTimeField(auto_now=True, db_index=True)

    class Meta:
        abstract = True
