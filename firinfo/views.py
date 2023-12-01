from django.shortcuts import render
from myapp.models import CASE_FIR, witnessInfo, victimInfo, PhysicalStructure, UserProfile, UserNotificationPanel
from django.shortcuts import get_object_or_404, redirect
from myapp.models import CASE_FIR, witnessInfo, victimInfo, PhysicalStructure, AdminProfile
from django.urls import reverse
# Create your views here.
def firinfo(request,fir_id,admin_id):
    admin_info = AdminProfile.objects.filter(id=admin_id)
    case_info = CASE_FIR.objects.get(id=fir_id)
    witness_infos = witnessInfo.objects.filter(fir_id=case_info)
    victim_infos = victimInfo.objects.get(id=case_info.victim_name.id)
    physical_structure_infos = PhysicalStructure.objects.get(fir_id=case_info)
    if admin_info:
        if request.method == 'POST':
            custom_message = request.POST.get('feedback_message')
            status = request.POST.get('stat-btn')
            temp_user_id = case_info.case_uploader
            temp_image = 'E:/kosom django final system/CIS-System-Project-main/media/noti_default_img.jpg'
            if status == 'accept':
                case_info.case_status = 'Accepted'
                temp_title = f'Case #{fir_id} has been accepted'
                temp_message = f'Follow the #{fir_id}. {custom_message}'
                case_info.save()
            else:
                case_info.case_status = 'Rejected'
                temp_title = f'Case #{fir_id} has been rejected'
                temp_message = f'Follow the #{fir_id}.{custom_message}'
                case_info.save()
            obj = UserNotificationPanel.objects.create(
                    for_user = temp_user_id,
                    noti_message =temp_message,
                    noti_image = temp_image,
                    Title = temp_title,
                )
            return redirect(reverse('AdminHomePage', args=[admin_id]))
        print(admin_info[0].email) 
        return render(request, 'firinfo.html', {'user':admin_info[0], 'case_info' : case_info,'witness_infos':witness_infos,'victim_infos':victim_infos,'physical_structure_infos':physical_structure_infos })
    else:
        admin_info = UserProfile.objects.filter(id=admin_id)   
    return render(request, 'firinfo.html', {'user':admin_info[0], 'case_info' : case_info,'witness_infos':witness_infos,'victim_infos':victim_infos,'physical_structure_infos':physical_structure_infos })

def applyfir(request, user_id):
    return render(request, 'applyfir.html', {'user_id': user_id})