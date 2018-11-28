from django.db import models

class StaffMember(models.Model):

    # Short name for the staff member that can be used as an index lookup value.
    name_key = models.CharField(max_length=30, default="")

    # Fullname of the staf member (i.e. Dr. Dante Scala).
    name = models.CharField(max_length=100)

    # Title of the staff member.
    title = models.CharField(max_length=100)

    # Photo location, which can either be relative to web root or some other static url.
    photo_src = models.CharField(max_length=255)

    # Long description of staff member experience.  Only applies to dentists and will not be shown
    # for other staff members
    biography = models.TextField(default="")

    def __str__(self):
        """The string representation of this class will only return the staff members full name"""

        return self.name

