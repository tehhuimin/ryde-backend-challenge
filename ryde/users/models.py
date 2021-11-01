from djongo import models

class Address(models.Model):
   address_1 = models.CharField(max_length=128)
   address_2 = models.CharField(max_length=128, blank=True)
   city = models.CharField(max_length=64)
   state = models.CharField(max_length=64)
   zip_code = models.CharField(max_length=6)


class Users(models.Model):
   name = models.CharField(max_length=100, blank=False)     # user name
   description = models.TextField(blank=True, default='')
   createdAt = models.DateTimeField(auto_now_add=True)
   dob = models.DateField(null=True)
   id = models.CharField(max_length=20, null=False, primary_key=True)   # user id
   address = models.EmbeddedModelField(
      model_container=Address
   )    

   objects = models.DjongoManager()
