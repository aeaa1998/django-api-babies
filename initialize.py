from django.contrib.auth.models import User
from parents.models import Parent

jhon = User.objects.create_user('john', 'j@j.com', '123456')
jhonParent = Parent(first_name='john', last_name='john', user=User.objects.get(email='j@j.com'))
jhonParent.save()
jhon2 = User.objects.create_user('john2', 'j2@j.com', '123456')
jhonParent2 = Parent(first_name='john2', last_name='john', user=User.objects.get(email='j2@j.com'))
jhonParent2.save()