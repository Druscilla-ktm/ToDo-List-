from django.db import models
#Todo model
class ToDo(models.Model):
    title = models.CharField(max_length=200)
    completed = models.BooleanField(default=False)
    create_at = models.DateTimeField(auto_created=True, auto_now_add=True)

    def _str_(self):
        return self.title
    

