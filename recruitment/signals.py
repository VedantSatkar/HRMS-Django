from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils import timezone
from .models import Recruitment
from employees.models import Employee, Department, Role
from attendance.models import Attendance


@receiver(post_save, sender=Recruitment)
def auto_create_employee_on_hire(sender, instance, created=False, **kwargs):
    """
    Automatically create an Employee record when Recruitment status changes to 'hired'
    Also creates attendance records for the employee
    """
    if instance.status == 'hired' and not instance.employee_created:
        try:
            # Generate auto-increment employee ID (emp00001, emp00002, etc.)
            last_employee = Employee.objects.all().order_by('id').last()
            last_id = int(last_employee.employee_id.replace('emp', '')) if last_employee else 0
            new_emp_id = f"emp{str(last_id + 1).zfill(5)}"
            
            # Get or create Department and Role
            department, _ = Department.objects.get_or_create(name='New Hires')
            role, _ = Role.objects.get_or_create(name=instance.position)
            
            # Create Employee
            employee = Employee.objects.create(
                name=instance.candidate_name,
                employee_id=new_emp_id,
                email=instance.email,
                department=department,
                role=role,
                date_of_joining=instance.hired_date or timezone.now().date()
            )
            
            # Mark as processed
            instance.employee_created = True
            instance.save(update_fields=['employee_created'])
            
            print(f"✓ Auto-created Employee: {employee.name} ({new_emp_id})")
            print(f"  - Department: {department.name}")
            print(f"  - Role: {role.name}")
            print(f"  - Email: {employee.email}")
            
        except Exception as e:
            print(f"❌ Error creating employee: {str(e)}")
