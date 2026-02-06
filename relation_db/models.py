from django.db import models


class Tag(models.Model):
    name = models.CharField(max_length=100)


    def __str__(self):
        return self.name

class Person(models.Model):
    namePerson = models.CharField(max_length=100, default='Иванов Иван Иванович')
    age_person = models.CharField(max_length=100)
    tags = models.ManyToManyField(Tag)

    def __str__(self):
        return f'{self.namePerson} --- {', '.join(i.name for i in self.tags.all() )}'
    

class Tour(models.Model):
    choice_person = models.OneToOneField(Person, on_delete=models.CASCADE, related_name="person", null=True)
    nameTour = models.CharField(max_length=100)

    def __str__(self):
        return self.nameTour
    

class Review(models.Model):
    MARKS = (
        ('1', '1'),
        ('2', '2'),
        ('3', '3'),
        ('4', '4'),
        ('5', '5'),
    )
    choice_person = models.ForeignKey(Person, on_delete=models.CASCADE, related_name='review', null=True)
    marks = models.CharField(max_length=100, choices=MARKS, default='5')
    text = models.CharField(max_length=100, default='хороший тур', null=True)
    created_at = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return f'Пользователь: {self.choice_person} - Оценка: {self.marks} - Комментарий: {self.text}'

