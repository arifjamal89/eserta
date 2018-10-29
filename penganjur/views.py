from django.shortcuts import render
from .models import Aktiviti
from .forms import AktivitiForm
# Create your views here.

# Home penganjur
def home(request):

	# aktivitiid = request.GET['aktivitiid']
	print(request.GET['aktivitiid'])				#sama macam get php id

	#List of record
	a = Aktiviti.objects.all()						#semua object/data letak dalam a
	#print(a.tajuk)
	for ak in a:									#Papar data di cmd
	 	print (ak.tajuk,ak.tempat,ak.penceramah)

	return render(request,'penganjur/home.html') 

#update aktiviti
def update_penganjur(request,pk):
	#dapatkan id aktiviti dan cari rekod
	aktiviti = get_object_or_404(Aktiviti,pk)
	aktiviti = Aktiviti(tajuk='Not Cheddar Update',tempat='Anyplace update',
		penceramah='Anybody Update',hadpeserta=20)
	aktiviti.save()

	return render(request,'penganjur/home.html') 

#tambah aktiviti
def add_penganjur(request):

	#tambah aktiviti setiap kali request
	akt = Aktiviti(tajuk='Not',tempat='Anyplaces',
		penceramah='Anybody',hadpeserta=55)
	akt.save() #Tambah Data

	return render(request,'penganjur/home.html') 

#delete penganjur
def delete_penganjur(request,pk):
	#get id aktiviti dan cari rekod
	aktiviti = get_object_or_404(Aktiviti,pk)

	#confirm delete
	aktiviti.delete()

	return render(request,'penganjur/home.html') 


#tambah aktiviti forms py
def addaktiviti(request):

	if request.method == "POST":
		pass # temporary kosong 
	else:
		form= AktivitiForm()

	return render(request,'penganjur/tambahaktiviti.html',{'form' : form})


