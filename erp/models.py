from django.db import models

# Create your models here.


class Course(models.Model):
    title = models.CharField(max_length=50)
    modules_count = models.IntegerField(default=1)
    studiying_now = models.IntegerField(default=0)
    teacher = models.CharField(max_length=250)
    start_date = models.DateField()
    end_date = models.DateField()
    image = models.ImageField(upload_to="course_images/", null=True, blank=True)
    rating = models.FloatField(default=5)
    def __str__(self):
        return self.title



class Subject(models.Model):
    topic = models.CharField(max_length=100)
    video = models.URLField()
    video_duration = models.TimeField()
    description = models.CharField(max_length=255)
    rating = models.FloatField(default=0)
    homework = models.CharField(max_length=255)

    def __str__(self):
        return self.topic


class Module(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name="modules")
    passed_exam = models.IntegerField(default=0)
    failed_exam = models.IntegerField(default=0)
    exam_date = models.DateField(null=True, blank=True)
    subjects = models.ManyToManyField(Subject, related_name="module_subjects")
    title = models.CharField(max_length=100)
    rating = models.FloatField(default=0)
    
    def __str__(self):
        return self.title


