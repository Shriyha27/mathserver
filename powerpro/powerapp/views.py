from django.shortcuts import render
def power(request):
	if request.method=="POST":
		intensity_value=int(request.POST.get("intensity"))
		resistance_value=int(request.POST.get("resistance"))
		power=(intensity_value**2)*resistance_value
		return render(request,'power.html',{"output":power})
	return render(request,'power.html')
