from django.contrib import admin
# Register your models here.

from .models import ServicesOfPolice,publicRoles,InvestigatorRoles,IGPS,TandC,EMERGENCY,FIR_CRIMINAL,UserNotificationPanel, CriminalProfile, UserTable,Notice,FAQ, UserProfile, MapMarker , AdminProfile, DistrictNames, victimInfo,witnessInfo,Case_related,PhysicalStructure, CASE_FIR,Crimetype,Relation


admin.site.register(UserTable)
admin.site.register(UserProfile)
admin.site.register(MapMarker)
admin.site.register(AdminProfile)
admin.site.register(DistrictNames)
admin.site.register(victimInfo)
admin.site.register(witnessInfo)
admin.site.register(Case_related)
admin.site.register(PhysicalStructure)
admin.site.register(CASE_FIR)
admin.site.register(Crimetype)
admin.site.register(Relation)
admin.site.register(CriminalProfile)
admin.site.register(TandC)
admin.site.register(IGPS)
admin.site.register(publicRoles)
admin.site.register(InvestigatorRoles)
admin.site.register(ServicesOfPolice)
admin.site.register(Notice)
admin.site.register(FAQ)
admin.site.register(UserNotificationPanel)
admin.site.register(FIR_CRIMINAL)
admin.site.register(EMERGENCY)