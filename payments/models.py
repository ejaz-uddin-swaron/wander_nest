from django.db import models
import uuid
from django.contrib.auth import get_user_model

User = get_user_model()

class Payment(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='payments')
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    tran_id = models.CharField(max_length=100, unique=True)
    status = models.CharField(max_length=20, default='Pending')  # Pending / Success / Failed
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.tran_id} - {self.user.username} - {self.status}"
