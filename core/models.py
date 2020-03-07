from django.db import models
import datetime

# Create your models here.



class Excavator(models.Model):
    date_added = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    unit_id = models.AutoField(primary_key=True)
    nama = models.CharField(max_length=140)
    merk = models.CharField(max_length=140)
    unit_model = models.CharField(max_length=140)

    def __str__(self):
        return "ID:{0}, {1} {2} {3}".format(self.unit_id, self.nama, self.merk, self.unit_model)        

class DumpTruck(models.Model):
    date_added = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    exacavator_id = models.ForeignKey(to='Excavator', on_delete=models.SET_NULL, null=True)    
    nama = models.CharField(max_length=140)
    merk = models.CharField(max_length=140)
    unit_model = models.CharField(max_length=140)

    def __str__(self):
        return "{0} unit_ID: {1} adalah {2} merk {3}".format(self.nama, self.id, self.merk, self.unit_model)

class Lokasi(models.Model):
    date_added = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    lokasi = models.CharField(max_length=140)
    sublokasi = models.TextField(max_length=140)


    def __str__(self):
        return "{0} Lokasi:{1} sublokasi: {2}".format(str(self.date_added.strftime("%d-%m-%Y %H:%M")), self.lokasi, self.sublokasi)

class Material(models.Model):
    COAL = 'COAL'
    MATERIAL_OB = 'OB'

    material_choices = (
        (COAL, 'COAL'),
        (MATERIAL_OB, 'OB')
    )

    material_inti = models.CharField(default=COAL, choices=material_choices, max_length=50)
    submaterial = models.CharField(max_length=50, blank=True)

    def __str__(self):
        return "Material: {0} Submaterial: {1}".format(self.material_inti, self.submaterial)

class Worker(models.Model):
    date_added = models.DateTimeField(auto_now_add=True, blank=True)
    employee_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=140, blank=False)

    OPERATOR = 'OPERATOR'
    DRIVER = 'DRIVER'
    WORKER_CHOICES = (
        (OPERATOR, 'Operator'),
        (DRIVER, 'Driver'),
    )
    tipe_pekerja = models.CharField(default=DRIVER,choices=WORKER_CHOICES, max_length=140)

    def __str__(self):
        return "{0}, ID: {1}, {2}".format(str(self.employee_id), str(self.name), str(self.tipe_pekerja))
    

class Muatan(models.Model):
    date_added = models.DateTimeField(auto_now_add=True, blank=True)
    
    shift = models.CharField(max_length=50)
    shift_start_time = models.TimeField()
    shift_end_time = models.TimeField()

    excavator = models.ForeignKey(Excavator, on_delete=models.DO_NOTHING)
    operator_excavator = models.ForeignKey(Worker, on_delete=models.DO_NOTHING, related_name='%(class)s_operator_excavator')
    
    dumpTruck = models.ForeignKey(DumpTruck, on_delete=models.DO_NOTHING, null=True)
    driver_dumptruck = models.ForeignKey(Worker, on_delete=models.DO_NOTHING, related_name='%(class)s_driver_dumptruck')

    lokasi = models.ForeignKey(Lokasi, on_delete=models.DO_NOTHING)
    material = models.ForeignKey(Material, on_delete=models.DO_NOTHING)
    
    ritasi = models.PositiveIntegerField()
    bcm = models.PositiveIntegerField()
    reported_problem = models.TextField(blank=True)

    def __str__(self):
        return "{0} MuatanID: {1} Ritasi: {2} BCM: {3} Problem: {4}".format(str(self.date_added.strftime("%d-%m-%Y %H:%M")), str(self.id), str(self.ritasi), str(self.bcm), self.reported_problem)
    
# class ExcavatorManager(models.Manager):
    # def get_queryset(self):
        # return super().get_queryset().filter(unit_id='0')
