from django.db import models
import datetime;

class Team(models.Model):
    team_name = models.CharField(max_length=20)
    leader = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return self.team_name


class Employee(models.Model):
    last_name = models.CharField(max_length=30)
    first_name = models.CharField(max_length=30)
    email = models.CharField(max_length=50, unique=True)
    leader = models.BooleanField(default=False)
    team = models.ForeignKey(Team, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return (f'{self.first_name} {self.last_name}')


class Issue(models.Model):
    title = models.CharField(max_length=30)
    LOW = 'Low'
    MEDIUM = 'Medium'
    HIGH = 'High'
    PRIORITY_CHOICES = [
        (LOW, 'Low'),
        (MEDIUM, 'Medium'),
        (HIGH, 'High'),
    ]
    priority = models.CharField(max_length=10, choices=PRIORITY_CHOICES, default=LOW)
    INPROGRESS = 'In Progress'
    INREVIEW = 'In Review'
    COMPLETED = 'Completed'
    STATUS_CHOICES = [
        (INPROGRESS, 'In Progress'),
        (INREVIEW, 'In Review'),
        (COMPLETED, 'Completed')
    ]
    status = models.CharField(max_length=15, choices=STATUS_CHOICES, default=INPROGRESS)
    description = models.TextField()
    time_created = models.DateTimeField(auto_now_add=True)
    time_closed = models.DateTimeField(auto_now=False, null=True, blank=True)
    assigned_team = models.ForeignKey(Team, on_delete=models.CASCADE)
    assigned_emp = models.ManyToManyField(Employee)

    def __str__(self):
        return self.title


class Update(models.Model):
    title = models.CharField(max_length=50, null=True)
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    issue_id = models.ManyToManyField(Issue)
    comment = models.TextField()
    time_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title