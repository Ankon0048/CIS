from django.shortcuts import render
from myapp.models import CASE_FIR, witnessInfo, victimInfo, PhysicalStructure, UserProfile, UserNotificationPanel
from django.shortcuts import get_object_or_404, redirect
from myapp.models import FIR_CRIMINAL,CriminalProfile,CASE_FIR, witnessInfo, victimInfo, PhysicalStructure, AdminProfile
from django.urls import reverse
# Create your views here.

def filtering(fir_id):
    case_obj = CASE_FIR.objects.get(id=fir_id)
    sus_inputted_obj = PhysicalStructure.objects.get(fir_id = case_obj)
    find_objs = []
    if sus_inputted_obj.gender and sus_inputted_obj.age and sus_inputted_obj.skinTone and sus_inputted_obj.hairLength and sus_inputted_obj.hairStyle and sus_inputted_obj.hairColor and sus_inputted_obj.faceShape and sus_inputted_obj.facialHair and sus_inputted_obj.dis_guis_mark:
        temp = CriminalProfile.objects.filter(
            criminal_gender__iexact=sus_inputted_obj.gender,
            criminal_age__iexact=sus_inputted_obj.age,
            criminal_skin_tone__iexact=sus_inputted_obj.skinTone,
            criminal_hair_length__iexact=sus_inputted_obj.hairLength,
            criminal_hair_style__iexact=sus_inputted_obj.hairStyle,
            criminal_hair_color__iexact=sus_inputted_obj.hairColor,
            criminal_face_shape__iexact=sus_inputted_obj.faceShape,
            criminal_facial_hair__iexact=sus_inputted_obj.facialHair,
            criminal_mark_type=sus_inputted_obj.dis_guis_mark,
        )
        find_objs.append(temp)
    if sus_inputted_obj.gender and sus_inputted_obj.age and sus_inputted_obj.skinTone and sus_inputted_obj.hairLength and sus_inputted_obj.hairStyle and sus_inputted_obj.hairColor and sus_inputted_obj.faceShape and sus_inputted_obj.facialHair:
        temp = CriminalProfile.objects.filter(
            criminal_gender__iexact=sus_inputted_obj.gender,
            criminal_age__iexact=sus_inputted_obj.age,
            criminal_skin_tone__iexact=sus_inputted_obj.skinTone,
            criminal_hair_length__iexact=sus_inputted_obj.hairLength,
            criminal_hair_style__iexact=sus_inputted_obj.hairStyle,
            criminal_hair_color__iexact=sus_inputted_obj.hairColor,
            criminal_face_shape__iexact=sus_inputted_obj.faceShape,
            criminal_facial_hair__iexact=sus_inputted_obj.facialHair,
        )
        for j in range(0, len(find_objs)):
            for i in find_objs[j]:
                temp = temp.exclude(id=i.id)
        find_objs.append(temp)
    if sus_inputted_obj.gender and sus_inputted_obj.age and sus_inputted_obj.skinTone and sus_inputted_obj.hairLength and sus_inputted_obj.hairStyle and sus_inputted_obj.hairColor and sus_inputted_obj.faceShape:
        temp = CriminalProfile.objects.filter(
            criminal_gender__iexact=sus_inputted_obj.gender,
            criminal_age__iexact=sus_inputted_obj.age,
            criminal_skin_tone__iexact=sus_inputted_obj.skinTone,
            criminal_hair_length__iexact=sus_inputted_obj.hairLength,
            criminal_hair_style__iexact=sus_inputted_obj.hairStyle,
            criminal_hair_color__iexact=sus_inputted_obj.hairColor,
            criminal_face_shape__iexact=sus_inputted_obj.faceShape,
        )
        for j in range(0, len(find_objs)):
            if find_objs[j]:
                for i in find_objs[j]:
                    temp = temp.exclude(id=i.id)
        if temp:
            find_objs.append(temp)
    if sus_inputted_obj.gender and sus_inputted_obj.age and sus_inputted_obj.skinTone and sus_inputted_obj.hairLength and sus_inputted_obj.hairStyle and sus_inputted_obj.hairColor:
        temp = CriminalProfile.objects.filter(
            criminal_gender__iexact=sus_inputted_obj.gender,
            criminal_age__iexact=sus_inputted_obj.age,
            criminal_skin_tone__iexact=sus_inputted_obj.skinTone,
            criminal_hair_length__iexact=sus_inputted_obj.hairLength,
            criminal_hair_style__iexact=sus_inputted_obj.hairStyle,
            criminal_hair_color__iexact=sus_inputted_obj.hairColor,
        )
        for j in range(0,len(find_objs)):
            for i in find_objs[j]:
                temp = temp.exclude(id=i.id)
        find_objs.append(temp)
    if sus_inputted_obj.gender and sus_inputted_obj.age and sus_inputted_obj.skinTone and sus_inputted_obj.hairLength and sus_inputted_obj.hairStyle:
        temp = CriminalProfile.objects.filter(
            criminal_gender__iexact=sus_inputted_obj.gender,
            criminal_age__iexact=sus_inputted_obj.age,
            criminal_skin_tone__iexact=sus_inputted_obj.skinTone,
            criminal_hair_length__iexact=sus_inputted_obj.hairLength,
            criminal_hair_style__iexact=sus_inputted_obj.hairStyle,
        )
        for j in range(0,len(find_objs)):
            for i in find_objs[j]:
                temp = temp.exclude(id=i.id)
        find_objs.append(temp)
    if sus_inputted_obj.gender and sus_inputted_obj.age and sus_inputted_obj.skinTone and sus_inputted_obj.hairLength:
        temp = CriminalProfile.objects.filter(
            criminal_gender__iexact=sus_inputted_obj.gender,
            criminal_age__iexact=sus_inputted_obj.age,
            criminal_skin_tone__iexact=sus_inputted_obj.skinTone,
            criminal_hair_length__iexact=sus_inputted_obj.hairLength,
        )
        for j in range(0,len(find_objs)):
            for i in find_objs[j]:
                temp = temp.exclude(id=i.id)
        find_objs.append(temp)
    if sus_inputted_obj.gender and sus_inputted_obj.age and sus_inputted_obj.skinTone:
        temp = CriminalProfile.objects.filter(
            criminal_gender__iexact=sus_inputted_obj.gender,
            criminal_age__iexact=sus_inputted_obj.age,
            criminal_skin_tone__iexact=sus_inputted_obj.skinTone,
        )
        for j in range(0,len(find_objs)):
            for i in find_objs[j]:
                temp = temp.exclude(id=i.id)
        find_objs.append(temp)
    if sus_inputted_obj.gender and sus_inputted_obj.age:
        temp = CriminalProfile.objects.filter(
            criminal_gender__iexact=sus_inputted_obj.gender,
            criminal_age__iexact=sus_inputted_obj.age,
        )
        for j in range(0,len(find_objs)):
            for i in find_objs[j]:
                temp = temp.exclude(id=i.id)
        find_objs.append(temp)
    if sus_inputted_obj.gender:
        temp = CriminalProfile.objects.filter(criminal_gender__iexact=sus_inputted_obj.gender)
        for j in range(0,len(find_objs)):
            for i in find_objs[j]:
                temp = temp.exclude(id=i.id)
        find_objs.append(temp)
    return find_objs

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
            elif status == 'reject':
                case_info.case_status = 'Rejected'
                temp_title = f'Case #{fir_id} has been rejected'
                temp_message = f'Follow the #{fir_id}.{custom_message}'
                case_info.save()
            else:
                temp_message = custom_message
                case_info.additional_info = temp_message
                temp_title = f'Case #{fir_id} has been completed'
                case_info.case_status = 'Completed'
                case_info.save()
            obj = UserNotificationPanel.objects.create(
                    for_user = temp_user_id,
                    noti_message =temp_message,
                    noti_image = temp_image,
                    Title = temp_title,
                )
            return redirect(reverse('AdminHomePage', args=[admin_id]))
        return render(request, 'firinfo.html', {'user':admin_info[0], 'case_info' : case_info,'witness_infos':witness_infos,'victim_infos':victim_infos,'physical_structure_infos':physical_structure_infos })
    else:
        admin_info = UserProfile.objects.filter(id=admin_id)
        if case_info.case_status == 'Accepted':
            objs = filtering(fir_id)
            # count = 0
            # for obj in objs:
            #     count += 1
            # print(f'count is {count}')
            return render(request, 'firinfo.html', {'user':admin_info[0], 'potential_suspects':objs , 'case_info' : case_info,'witness_infos':witness_infos,'victim_infos':victim_infos,'physical_structure_infos':physical_structure_infos })
    return render(request, 'firinfo.html', {'user':admin_info[0], 'case_info' : case_info,'witness_infos':witness_infos,'victim_infos':victim_infos,'physical_structure_infos':physical_structure_infos })

def applyfir(request, user_id):
    return render(request, 'applyfir.html', {'user_id': user_id})


def fircomplete(request,fir_id,admin_id,criminal_id=None):
    admin_info = UserProfile.objects.filter(id=admin_id)
    case_info = CASE_FIR.objects.get(id=fir_id)
    witness_infos = witnessInfo.objects.filter(fir_id=case_info)
    victim_infos = victimInfo.objects.get(id=case_info.victim_name.id)
    physical_structure_infos = PhysicalStructure.objects.get(fir_id=case_info)
    case_info.case_status = 'On Going'
    case_info.save()
    print(f'criminal_id is {criminal_id}')
    if criminal_id:
        criminal_infos = CriminalProfile.objects.get(id=criminal_id)
        fir_criminal_relation = FIR_CRIMINAL.objects.create(
            case_related = case_info,
            criminal_related = criminal_infos
        )
        fir_criminal_relation = FIR_CRIMINAL.objects.filter(case_related = case_info)
        return render(request, 'firinfo.html', {'user':admin_info[0], 'case_info' : case_info,'witness_infos':witness_infos,'victim_infos':victim_infos,'physical_structure_infos':physical_structure_infos, 'criminal_found':fir_criminal_relation[0] }) 
    return render(request, 'firinfo.html', {'user':admin_info[0], 'case_info' : case_info,'witness_infos':witness_infos,'victim_infos':victim_infos,'physical_structure_infos':physical_structure_infos}) 