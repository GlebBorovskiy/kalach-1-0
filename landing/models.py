from django.db import models

class Subsriber(models.Model):

    email = models.EmailField()
    name = models.CharField(max_length=128)

    def __str__(self):
        return "Пользователь %s %s" % (self.name, self.email,)

    class Meta:
        verbose_name = 'MySubsriber'            #произносимое имя
        verbose_name_plural = 'A lot of Subsribers'    #произносимое имя во множ. числе





