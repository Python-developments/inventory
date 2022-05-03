from .models import Staff


def extras(request):
    myStaff = Staff.objects.all()
    return {'staffs': myStaff}
