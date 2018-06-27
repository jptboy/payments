from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader
import braintree
import hashlib
import random
import json
from django.http import JsonResponse
from django.utils.six import BytesIO
from django.views.decorators.csrf import csrf_exempt
# Create your views here.

class Tokens():#i use this class to make an object that can hold a token value
    __token=-1
    def GetToken(self):
        self.__token=random.randint(1,1000000)
        return self.__token
    def getCurrentToken(self):
        return self.__token



currenttokenobj=Tokens()

class paymentval():
    __paymentamt=0
    def getPaymentVal(self):
        return self.__paymentamt
@csrf_exempt
def getToken(request):
    return JsonResponse({'token':currenttokenobj.GetToken()})

      
def payments(request):
    gateway = braintree.BraintreeGateway(
            braintree.Configuration(
            environment=braintree.Environment.Sandbox,
            merchant_id='t2w5dbzprv32crd7',
            public_key='q2np62tjvdmmn6fk',
            private_key='814c67e277a7bc12bdfa448c6ed32e6f'  )
    )
    client_token = gateway.client_token.generate()
    if request.method=='POST':
        
        #return redirect("/takethis")
        nonce=request.POST.get('payment_method_nonce',None)
        payment_amt=request.POST.get('payment_amt',"ERROR")
        try:
            if(float(payment_amt)<0 or float(payment_amt)>100000):
                return JsonResponse({"LOL":"NO"})
        except:
            return JsonResponse({"LOL":"NO"})

        print(payment_amt)
        result = gateway.transaction.sale({
            "amount": payment_amt,
            "payment_method_nonce": nonce,
            "options": {
            "submit_for_settlement": True
            }
        })
        if result.is_success:
            return JsonResponse({"LOL":"YUH"})
        else:
            return JsonResponse({"LOL":"NO"})
    context={"token":client_token}
    template=loader.get_template('payments/index.html')
    return HttpResponse(template.render(context,request))
    #return redirect("/success")

def success(request):
    return render(request,"payments/foo.html")
def error(request):
    return render(request,"payments/bar.html")