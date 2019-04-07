from django.db import models
from django.utils import timezone
from django.db.models import Sum
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _

# Create your models here.
SCORECHOICES = (
    (0, '0' ),
    (1, '1'),
    (2, '2'),
    (3, '3'),
    (4, '4')
)


class Evaluation(models.Model):
    nameOfTester = models.ForeignKey(User, verbose_name="User ID of Test Conductor", on_delete=models.CASCADE)
    nameOfTestee = models.CharField(max_length=30, verbose_name="First Name of Testee")
    emailOfTestee = models.EmailField(max_length=50, verbose_name="Email of Testee")
    startOfTestDatetime = models.DateTimeField(default=timezone.now, verbose_name="Start of Test Date and Time")
    startOfStep1Time = models.TimeField(default=timezone.now, verbose_name="Start of Step 1 Time")
    step1Score = models.IntegerField(default=2, choices=SCORECHOICES, verbose_name="Step 1 Score" )
    endOfStep1Time = models.TimeField(default=timezone.now, verbose_name="End of Step 1 Time")
    step2Score = models.IntegerField(default=2, choices=SCORECHOICES, verbose_name="Step 2 Score" )
    step3Score = models.IntegerField(default=2, choices=SCORECHOICES, verbose_name="Step 3 Score" )
    step4Score = models.IntegerField(default=2, choices=SCORECHOICES, verbose_name="Step 4 Score" )
    step5Score = models.IntegerField(default=2, choices=SCORECHOICES, verbose_name="Step 5 Score" )
    startOfStep6Time = models.TimeField(default=timezone.now, verbose_name="Start of Step 6 Time")
    step6Score = models.IntegerField(default=2, choices=SCORECHOICES, verbose_name="Step 6 Score" )
    endOfStep6Time = models.TimeField(default=timezone.now, verbose_name="End of Step 6 Time")
    startOfStep7Time = models.TimeField(default=timezone.now, verbose_name="Start of Step 7 Time")
    step7Score = models.IntegerField(default=2, choices=SCORECHOICES, verbose_name="Step 7 Score" )
    endOfStep7Time = models.TimeField(default=timezone.now, verbose_name="End of Step 7 Time")
    startOfStep8aTime = models.TimeField(default=timezone.now, verbose_name="Start of Step 8a Time")
    step8aScore = models.IntegerField(default=2, choices=SCORECHOICES, verbose_name="Step 8a Score" )
    endOfStep8aTime = models.TimeField(default=timezone.now, verbose_name="End of Step 8a Time")
    startOfStep8bTime = models.TimeField(default=timezone.now, verbose_name="Start of Step 8b Time")
    step8bScore = models.IntegerField(default=2, choices=SCORECHOICES, verbose_name="Step 8b Score" )
    endOfStep8bTime = models.TimeField(default=timezone.now, verbose_name="End of Step 8b Time")
    step9Score = models.IntegerField(default=2, choices=SCORECHOICES, verbose_name="Step 9 Score" )
    step10Score = models.IntegerField(default=2, choices=SCORECHOICES, verbose_name="Step 10 Score" )
    additionalComments = models.TextField(max_length = 500, blank=True)
    totalScore = models.IntegerField(verbose_name="Total Score", default=0)
    def save(self,*args, **kwargs):
        allScores = [self.step1Score,self.step2Score,self.step3Score,self.step4Score,self.step5Score,self.step6Score,self.step7Score,self.step8aScore,self.step8bScore,self.step9Score,self.step10Score]
        self.totalScore = sum(allScores)
        super().save(*args, **kwargs)  # Call the "real" save() method.