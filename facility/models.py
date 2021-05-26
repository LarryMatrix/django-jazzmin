from django.db import models
from utils.base_model import BaseModel


class Facility(BaseModel):
    Fac_IDNumber = models.CharField(max_length=100, unique=True)
    Name = models.CharField(max_length=100)
    Comm_FacName = models.CharField(max_length=100, blank=True, null=True)
    Region = models.CharField(max_length=100)
    Zone = models.CharField(max_length=100)
    Region_Code = models.CharField(max_length=100)
    District_Code = models.CharField(max_length=100)
    District = models.CharField(max_length=100)
    Council_Code = models.CharField(max_length=100)
    Council = models.CharField(max_length=100)
    Ward = models.CharField(max_length=100)
    Village = models.CharField(max_length=100, blank=True, null=True)
    FacilityTypeGroupCode = models.CharField(max_length=100)
    FacilityTypeGroup = models.CharField(max_length=100)
    FacilityTypeCode = models.CharField(max_length=100)
    FacilityType = models.CharField(max_length=100)
    OwnershipGroupCode = models.CharField(max_length=100)
    OwnershipGroup = models.CharField(max_length=100)
    OwnershipCode = models.CharField(max_length=100)
    Ownership = models.CharField(max_length=100)
    OperatingStatus = models.CharField(max_length=100)
    Latitude = models.CharField(max_length=100, blank=True, null=True)
    Longitude = models.CharField(max_length=100, blank=True, null=True)
    RegistrationStatus = models.CharField(max_length=100)
    OpenedDate = models.CharField(max_length=100)
    CreatedAt = models.CharField(max_length=100, blank=True, null=True)
    UpdatedAt = models.CharField(max_length=100, blank=True, null=True)
    ClosedDate = models.CharField(max_length=100, blank=True, null=True)
    OSchangeOpenedtoClose = models.CharField(max_length=100, blank=True, null=True)
    OSchangeClosedtoOperational = models.CharField(max_length=100, blank=True, null=True)
    PostorUpdate = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.Fac_IDNumber

    class Meta(BaseModel.Meta):
        ordering = ('-Fac_IDNumber',)


