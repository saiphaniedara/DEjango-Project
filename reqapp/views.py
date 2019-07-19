from django.shortcuts import render
from django.views.generic import View
from reqapp.models import Agent,Location,Contact_info,Address
class GetInput(View):
     def get(self,request):
          return render(request,"insert.html")
class Relationship_test(View):         
     def post(self,request):
          try:
                fn=request.POST["fn"]
                ln=request.POST["ln"]
                exp=request.POST['exp']
                cn=request.POST['cn']               
                lcn1=request.POST["lcn"]
                lcc=request.POST['lcc']
                lcs=request.POST['lcs']
                lpin=int(request.POST['lpc'])               
                mn=request.POST['mn']
                pn=request.POST['pn']
                eml=request.POST['email']                
                al1=request.POST['adl1']
                al2=request.POST['adl2']
                cit=request.POST['ac']
                st=request.POST['as']
                apin=int(request.POST['apc'])
                lmk=request.POST['lmk']
                a=Agent(first_name=fn,last_name=ln,experience=exp,company_name=cn)
                a.save()
                l=Location(agent_id=a,loc_name=lcn1,loc_city=lcc,loc_state=lcs,pincode=lpin)
                l.save()
                ci=Contact_info(agent_id=a,mobile_no=mn,phone_no=pn,email_id=eml)
                ci.save()
                ad=Address(agent_id=a,add_line1=al1,add_line2=al2,city=cit,state=st,pincode=apin,landmark=lmk)
                ad.save()
                return render(request,"result.html")
          except(ValueError):
                return render(request,"insert.html")
class Result(View):
     def post(self,request):
          resp=request.POST['ab']
          if resp=='Display Agents':
               res=Agent.objects.all()
               return render(request,"dispag.html",{'agents':res})
          elif resp=='Register New Agent':
               return render(request,"insert.html")
          elif resp=='Add Location to Existing Agent':
               res=Agent.objects.all()
               return render(request,"addloc.html",{'agents':res})
          elif resp=='Add Address to Existing Agent':
               res=Agent.objects.all()
               return render(request,"addadd.html",{'agents':res})
class Add_Location_details(View):
     def post(self,request):
          try:
               agid=int(request.POST['id'])
               lcn1=request.POST["lcn"]
               lcc=request.POST['lcc']
               lcs=request.POST['lcs']
               lpin=int(request.POST['lpc'])
               a=Agent.objects.get(id=agid)
               l=Location(agent_id=a,loc_name=lcn1,loc_city=lcc,loc_state=lcs,pincode=lpin)
               l.save()
               return render(request,'result.html')
          except(ValueError):
               return render(request,"addloc.html")
class Add_Address_details(View):
     def post(self,request):
          try:
               agid=int(request.POST['id'])
               al1=request.POST['adl1']
               al2=request.POST['adl2']
               cit=request.POST['ac']
               st=request.POST['as']
               apin=int(request.POST['apc'])
               lmk=request.POST['lmk']
               a=Agent.objects.get(id=agid)
               ad=Address(agent_id=a,add_line1=al1,add_line2=al2,city=cit,state=st,pincode=apin,landmark=lmk)
               ad.save()
               return render(request,'result.html')
          except(ValueError):
               return render(request,"addadd.html")
class Display(View):
     def post(self,request):
          return render(request,"result.html")
               
          
               
         

     
