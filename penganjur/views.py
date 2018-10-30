from django.shortcuts import render,redirect,get_object_or_404
from .models import Aktiviti
from .forms import AktivitiForm
from django.urls import reverse_lazy

# Create your views here.

# Home penganjur
def home(request):

	# aktivitiid = request.GET['aktivitiid']
	#print(request.GET['aktivitiid'])				#sama macam get php id

	#List of record
	a = Aktiviti.objects.all()						#semua object/data letak dalam a
	#print(a.tajuk)   
	# for ak in a:									#Papar data di cmd
	#  	print (ak.tajuk,ak.tempat,ak.penceramah)

	return render(request,'penganjur/home.html',{'aktiviti': a}) 

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
		
		form = AktivitiForm(request.POST) 			#value akan submit ke form

		if form.is_valid(): 								#validate semak semua dah isi
			aktiviti = form.save(commit=False) 				#simpan dalam memori
			aktiviti.save() 								#save ke db
			return redirect(reverse_lazy('home_penganjur'))
		#print("POST DAH MASUK") 							#ini macam echo nak semak masuk POST ke x


	else:
		form= AktivitiForm()
		#print(form)

	return render(request,'penganjur/tambahaktiviti.html',{'form' : form})

#hapus aktiviti guna form
def delete_aktiviti(request,pk):

	aktiviti = get_object_or_404(Aktiviti,pk=pk)

	if request.method == 'POST':

		if request.POST.get("submit_yes"):
			print(request.method)
			aktiviti.delete()
			return redirect(reverse_lazy('home_penganjur'))

	#View page confirm delete	
	return render(request,'penganjur/confirm_delete_aktiviti.html',{'aktiviti':aktiviti})

#edit aktiviti forms py
def editaktiviti(request,pk):

	#Dapatkan rekod berdasarkan pk yang dihantar
	aktiviti= get_object_or_404(Aktiviti,pk=pk)


	if request.method == "POST":
		
		form = AktivitiForm(request.POST,instance=aktiviti) #value akan submit ke form

		if form.is_valid(): 								#validate semak semua dah isi
			aktiviti = form.save(commit=False) 				#simpan dalam memori
			aktiviti.save() 								#save ke db
			return redirect(reverse_lazy('home_penganjur'))
		#print("POST DAH MASUK") 							#ini macam echo nak semak masuk POST ke x


	else:
		form= AktivitiForm(instance=aktiviti) #yang ni dapatkan id untuk papar
		#print(form)

	return render(request,'penganjur/editaktiviti.html',{'form' : form})