# rule_engine/models.py
from django.db import models

class Rule(models.Model):
    rule_name = models.CharField(max_length=50)
    rule_string = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.rule_name
