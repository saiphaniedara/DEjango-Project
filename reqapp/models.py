from django.db import models
class Agent(models.Model):
     first_name=models.CharField(max_length=20)
     last_name=models.CharField(max_length=20)
     experience=models.CharField(max_length=10)
     company_name=models.CharField(max_length=30)
     def __str__(self):
          return self.first_name+" "+self.last_name
class Location(models.Model):
     agent_id=models.ForeignKey(Agent,on_delete=models.CASCADE)
     loc_name=models.CharField(max_length=30)
     loc_city=models.CharField(max_length=30)
     loc_state=models.CharField(max_length=20)
     pincode=models.IntegerField()
     def __str__(self):
          return self.loc_name
class Contact_info(models.Model):
     agent_id=models.OneToOneField(Agent,on_delete=models.CASCADE)
     mobile_no=models.CharField(max_length=10)
     phone_no=models.CharField(max_length=10)
     email_id=models.EmailField()
     def __str__(self):
          return self.mobile_no+" "+self.email_id
class Address(models.Model):
     agent_id=models.ForeignKey(Agent,on_delete=models.CASCADE)
     add_line1=models.CharField(max_length=80)
     add_line2=models.CharField(max_length=80)
     city=models.CharField(max_length=30)
     state=models.CharField(max_length=30)
     pincode=models.IntegerField()
     landmark=models.CharField(max_length=30)
     def __str__(self):
          return self.city





     
     
