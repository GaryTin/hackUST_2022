from django.shortcuts import render,HttpResponse
import json
from web3 import Web3
from django.middleware.csrf import get_token
from django.template import RequestContext, Template


# Create your views here.
def home(request):
    return render(request,'SharpBargain/home.html')

def Test(request):
    if request.method =="POST" and 'run' in request.POST:
        print("start")
        print(request.POST["v1"])
        print(request.POST["v2"])
        print(request.POST["userAddress"])
        return render(request, 'SharpBargain/test.html')
    else:
        return render(request,'SharpBargain/test.html')

def MetaMaskTestPage(request):

        return render(request, 'SharpBargain/MetaMaskTestPage.html',)

def some_func(request):
    if request.method == 'POST':
        param1 = request.POST.get('v1')
        param2 = request.POST.get('v2')
        print(param1, param2)

        response_data = 'successful!'

    return render(request, 'SharpBargain/test.html')

def read_name(request):
    if request.method == 'GET':
        infura_url = "https://ropsten.infura.io/v3/f28a0b5ddee744859bda3e9f79b01b8c"
        web3 = Web3(Web3.HTTPProvider(infura_url))

        abi = json.loads(
            """[
           {
               "inputs": [
                   {
                       "internalType": "string",
                       "name": "_name",
                       "type": "string"
                   }
               ],
               "stateMutability": "nonpayable",
               "type": "constructor"
           },
           {
               "inputs": [],
               "name": "say_hi",
               "outputs": [
                   {
                       "internalType": "string",
                       "name": "",
                       "type": "string"
                   }
               ],
               "stateMutability": "view",
               "type": "function"
           },
           {
               "inputs": [
                   {
                       "internalType": "string",
                       "name": "_name",
                       "type": "string"
                   }
               ],
               "name": "set_name",
               "outputs": [],
               "stateMutability": "nonpayable",
               "type": "function"
           }
       ]""")

        # smart contract address
        address = web3.toChecksumAddress('0x676a9e2BB951D0DD7bc5B4cFAF733d2c04aD907e')
        User_address = web3.toChecksumAddress("0xceb45891f0b9761d9d7d950710aa5f9d785f87d6")
        contract = web3.eth.contract(address=address, abi=abi)
        name = contract.functions.say_hi().call()

        response_data = name

        return HttpResponse(
            json.dumps(response_data),
            content_type="application/json"
        )
