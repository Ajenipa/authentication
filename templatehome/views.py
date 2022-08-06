from django.shortcuts import render

# Create your views here.

def get_home_view(request):
    contex = {
   }
    return render(request,"landing/index.html", context=contex)
    #return render(request,"proj_16_sonia/sign-in.html", context=contex)
def get_landing_view(request):
    contex = {
    }
    return render(request,"landing/index.html", context=contex)
