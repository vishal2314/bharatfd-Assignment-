from django.db import models

from django.db import models
from ckeditor.fields import RichTextField
from googletrans import Translator

class FAQ(models.Model):
    question = models.TextField()
    answer = RichTextField()
    question_hi = models.TextField(blank=True, null=True)
    question_bn = models.TextField(blank=True, null=True)

    def get_translated_question(self, lang='en'):
        if lang == 'hi':
            return self.question_hi or self.question
        elif lang == 'bn':
            return self.question_bn or self.question
        return self.question  

    def save(self, *args, **kwargs):
        if not self.question_hi or not self.question_bn:
            translator = Translator()
            self.question_hi = translator.translate(self.question, dest='hi').text
            self.question_bn = translator.translate(self.question, dest='bn').text
        super().save(*args, **kwargs)
