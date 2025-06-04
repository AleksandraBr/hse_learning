from django.db import models
from django.core.validators import FileExtensionValidator

class Student(models.Model):
    full_name = models.CharField(max_length=200, verbose_name="ФИО")
    photo = models.ImageField(upload_to='students/', verbose_name="Фото")
    email = models.EmailField(verbose_name="Электронная почта")
    phone = models.CharField(max_length=20, verbose_name="Телефон")
    resume = models.FileField(
        upload_to='resumes/',
        validators=[FileExtensionValidator(['pdf', 'doc', 'docx'])],
        verbose_name="Резюме"
    )

    def __str__(self):
        return self.full_name

    class Meta:
        verbose_name = "Студент"
        verbose_name_plural = "Студенты"


class Program(models.Model):
    title = models.CharField(max_length=200, verbose_name="Название программы")
    url = models.URLField(verbose_name="Ссылка на страницу ОП")
    description = models.TextField(verbose_name="Описание")
    what_ill_learn = models.TextField(verbose_name="Что я буду изучать")
    skills = models.TextField(verbose_name="Чему научусь")
    advantages = models.TextField(verbose_name="Преимущества программы")
    prospects = models.TextField(verbose_name="Перспективы после обучения")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Образовательная программа"
        verbose_name_plural = "Образовательные программы"


class Manager(models.Model):
    ROLE_CHOICES = [
        ('academic', 'Академический руководитель'),
        ('manager', 'Менеджер программы'),
    ]

    full_name = models.CharField(max_length=200, verbose_name="ФИО")
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, verbose_name="Роль")
    photo = models.ImageField(upload_to='managers/', verbose_name="Фото")
    email = models.EmailField(verbose_name="Электронная почта")

    def __str__(self):
        return f"{self.get_role_display()}: {self.full_name}"

    class Meta:
        verbose_name = "Руководитель/Менеджер"
        verbose_name_plural = "Руководители/Менеджеры"


class Classmate(models.Model):
    full_name = models.CharField(max_length=200, verbose_name="ФИО")
    photo = models.ImageField(upload_to='classmates/', verbose_name="Фото")
    email = models.EmailField(verbose_name="Электронная почта")
    phone = models.CharField(max_length=20, verbose_name="Телефон", blank=True)

    def __str__(self):
        return self.full_name

    class Meta:
        verbose_name = "Сокурсник"
        verbose_name_plural = "Сокурсники"
