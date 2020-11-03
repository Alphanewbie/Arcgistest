from django.shortcuts import render
from .models import OperationLogModel, DTGDataModel
from django.db.models import Avg, Min, Max, F
# Create your views here.
def index(request):

    oplog = OperationLogModel.objects.get(pk=3)
    dtgs = DTGDataModel.objects.filter(oplog = oplog)
    
    dtg_detail = dtgs.aggregate(
            datetimes = Min('datetimes'),
            time_start = Min('datetimes'),
            time_end = Max('datetimes'),
            daily_drive = Max('daily_drive'),
            stack_drive = Max('stack_drive'),
            center_lon = Avg('longitude'), 
            center_lat = Avg('latitude')
        )
    context = {
        'dtgs' : dtgs,
        'dtg_detail' : dtg_detail,
    }
    return render(request, 'interface/index.html', context)