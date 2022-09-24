from django.shortcuts import render
from django.core.mail import send_mail

def home(request):
    if(request.method=="POST"):
        photo=""
        edit=""
        #raise Exception(request.POST.get('phtography'))
        msg_email=request.POST['email']
        msg_message=request.POST['message']
        msg_date=request.POST['date']
        try:
            msg_phtography=request.POST['phtography']
            msg_editing=request.POST['edit']
        except Exception as ec:    
            msg_phtography=""
            msg_editing=""
        # raise Exception(msg_phtography)

        try:
            if(request.POST['phtography']=='phtography'):
                photo='photo'
                raise Exception(photo)
        except Exception as ecc:  
                print("")

        try:     
            if(request.POST['edit']=='edit'): 
                edit='edit'  
                raise Exception(edit)
        except Exception as ecc1:  
                print("")

        # raise Exception(msg_editing)          
        send_mail(
                msg_message,
                edit,
                msg_email,
                ['ahmedkasraoui97@gmail.com'],       
        )

        return render(request,'home.html',{})
    else:
        return render(request,'home.html',{})