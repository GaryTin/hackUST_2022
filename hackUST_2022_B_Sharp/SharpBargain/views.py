from django.shortcuts import render,HttpResponse,redirect
import json
from web3 import Web3
from django.middleware.csrf import get_token
from django.template import RequestContext, Template


# Create your views here.
infura_url = "https://ropsten.infura.io/v3/f28a0b5ddee744859bda3e9f79b01b8c"
web3 = Web3(Web3.HTTPProvider(infura_url))
abi = json.loads(
      """
      [
	{
		"anonymous": false,
		"inputs": [
			{
				"indexed": false,
				"internalType": "string",
				"name": "prod_index",
				"type": "string"
			}
		],
		"name": "retailer_receipt",
		"type": "event"
	},
	{
		"inputs": [
			{
				"internalType": "address",
				"name": "new_manufacturer",
				"type": "address"
			}
		],
		"name": "add_manufacturer",
		"outputs": [],
		"stateMutability": "nonpayable",
		"type": "function"
	},
	{
		"inputs": [
			{
				"internalType": "string",
				"name": "prod_type",
				"type": "string"
			},
			{
				"internalType": "address",
				"name": "m_address",
				"type": "address"
			},
			{
				"internalType": "uint256",
				"name": "prod_production_date",
				"type": "uint256"
			},
			{
				"internalType": "string",
				"name": "prod_wholesale_price",
				"type": "string"
			},
			{
				"internalType": "string",
				"name": "prod_retail_price",
				"type": "string"
			},
			{
				"internalType": "uint256",
				"name": "quantity",
				"type": "uint256"
			}
		],
		"name": "add_product",
		"outputs": [],
		"stateMutability": "nonpayable",
		"type": "function"
	},
	{
		"inputs": [
			{
				"internalType": "address",
				"name": "new_retailers",
				"type": "address"
			}
		],
		"name": "add_retailer",
		"outputs": [],
		"stateMutability": "nonpayable",
		"type": "function"
	},
	{
		"inputs": [
			{
				"internalType": "uint256[]",
				"name": "prod_id_list",
				"type": "uint256[]"
			},
			{
				"internalType": "address",
				"name": "b_address",
				"type": "address"
			},
			{
				"internalType": "uint256",
				"name": "purchase_date",
				"type": "uint256"
			}
		],
		"name": "buyer_purchase_from_retailer",
		"outputs": [],
		"stateMutability": "nonpayable",
		"type": "function"
	},
	{
		"inputs": [
			{
				"internalType": "address",
				"name": "m_address",
				"type": "address"
			}
		],
		"name": "remove_manufacturer",
		"outputs": [
			{
				"internalType": "bool",
				"name": "",
				"type": "bool"
			}
		],
		"stateMutability": "nonpayable",
		"type": "function"
	},
	{
		"inputs": [
			{
				"internalType": "address",
				"name": "r_address",
				"type": "address"
			}
		],
		"name": "remove_retailer",
		"outputs": [
			{
				"internalType": "bool",
				"name": "",
				"type": "bool"
			}
		],
		"stateMutability": "nonpayable",
		"type": "function"
	},
	{
		"inputs": [
			{
				"internalType": "address",
				"name": "m_address",
				"type": "address"
			},
			{
				"internalType": "address",
				"name": "r_address",
				"type": "address"
			},
			{
				"internalType": "string",
				"name": "prod_type",
				"type": "string"
			},
			{
				"internalType": "uint256",
				"name": "purchase_date",
				"type": "uint256"
			},
			{
				"internalType": "uint256",
				"name": "quantity",
				"type": "uint256"
			}
		],
		"name": "retailer_purchase_from_manu",
		"outputs": [],
		"stateMutability": "nonpayable",
		"type": "function"
	},
	{
		"inputs": [
			{
				"internalType": "uint256",
				"name": "pid",
				"type": "uint256"
			},
			{
				"internalType": "string",
				"name": "comment",
				"type": "string"
			},
			{
				"internalType": "uint8",
				"name": "rate",
				"type": "uint8"
			}
		],
		"name": "set_comment",
		"outputs": [],
		"stateMutability": "nonpayable",
		"type": "function"
	},
	{
		"inputs": [],
		"stateMutability": "nonpayable",
		"type": "constructor"
	},
	{
		"inputs": [
			{
				"internalType": "uint256",
				"name": "pid",
				"type": "uint256"
			}
		],
		"name": "buyer_view_comment",
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
				"name": "a",
				"type": "string"
			},
			{
				"internalType": "string",
				"name": "b",
				"type": "string"
			}
		],
		"name": "compareStrings",
		"outputs": [
			{
				"internalType": "bool",
				"name": "",
				"type": "bool"
			}
		],
		"stateMutability": "pure",
		"type": "function"
	},
	{
		"inputs": [
			{
				"internalType": "address",
				"name": "b_address",
				"type": "address"
			}
		],
		"name": "get_all_uncomment_prod",
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
				"internalType": "address",
				"name": "r_address",
				"type": "address"
			}
		],
		"name": "get_lastest_retailer_record",
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
				"internalType": "address",
				"name": "m_address",
				"type": "address"
			},
			{
				"internalType": "string",
				"name": "prod_type",
				"type": "string"
			}
		],
		"name": "get_remaining",
		"outputs": [
			{
				"internalType": "uint256",
				"name": "",
				"type": "uint256"
			}
		],
		"stateMutability": "view",
		"type": "function"
	},
	{
		"inputs": [
			{
				"internalType": "address",
				"name": "input_address",
				"type": "address"
			}
		],
		"name": "get_role",
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
				"internalType": "address",
				"name": "b_address",
				"type": "address"
			},
			{
				"internalType": "uint256",
				"name": "prod_id",
				"type": "uint256"
			}
		],
		"name": "get_uncomment_prod_by_id",
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
				"internalType": "address",
				"name": "b_address",
				"type": "address"
			}
		],
		"name": "get_user_history",
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
				"internalType": "address",
				"name": "m_address",
				"type": "address"
			}
		],
		"name": "manu_get_all_data",
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
				"internalType": "address",
				"name": "r_address",
				"type": "address"
			}
		],
		"name": "retailer_get_all_prod_type",
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
				"internalType": "uint256",
				"name": "pid",
				"type": "uint256"
			}
		],
		"name": "retailer_get_prod_info_by_pid",
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
				"internalType": "address",
				"name": "r_address",
				"type": "address"
			}
		],
		"name": "retailer_view_comment",
		"outputs": [
			{
				"internalType": "string",
				"name": "",
				"type": "string"
			}
		],
		"stateMutability": "view",
		"type": "function"
	}
]
      """)
# smart contract address
address = web3.toChecksumAddress('0xAB6A4705D5d077294C418f175A9f4De597298F7e')
contract = web3.eth.contract(address=address, abi=abi)

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

def index(request):
    return render(request,'SharpBargain/index.html')

def cusHistory(request):
    return render(request, 'SharpBargain/cusHistory.html')

def cusComment(request):
    return render(request, 'SharpBargain/cusComment.html')

def cusView(request):
    return render(request, 'SharpBargain/cusView.html')

def cusDashboard(request,account_address):

    user_ac = web3.toChecksumAddress(account_address)
    user_history_raw = contract.functions.get_user_history(user_ac).call({'from':user_ac})
    print(user_history_raw) #[prod_type/prod_id/purchase_date/price/comment/rate],[.....
    img_urls = None
    user_history = {}
    user_historys = []
    user_historys.append(
        {"prod_type": "Test", "prod_id": "123321", "purchase_date": "111", "price": "9999", "not_comment": True})
    user_historys.append(
        {"prod_type": "Test2", "prod_id": "14444", "purchase_date": "11122", "price": "888", "not_comment": False})
    next_open_bracket_index= 0
    while (next_open_bracket_index< len(user_history_raw)):
        close_bracket_index =user_history_raw.find(']')
        next_open_bracket_index = close_bracket_index+2
        one_history = user_history_raw[1:close_bracket_index] #prod_type/prod_id/purchase_date/price/comment/rate
        history_array = one_history.spilt('/')
        user_history = {"prod_type":history_array[0],"prod_id":history_array[1],"purchase_date":history_array[2],"price":history_array[3],"not_comment":history_array[4]==""}
        user_historys.append(user_history)
        if (next_open_bracket_index< user_history_raw.length()):
            user_history_raw = user_history_raw[next_open_bracket_index:]

    return render(request, 'SharpBargain/cusDashboard.html',{
        "user_historys":user_historys,
    })

def retailerDashboard(request,account_address):
    return render(request, 'SharpBargain/retailerDashboard.html')

def retailerPOS(request):
    return render(request, 'SharpBargain/retailerPOS.html')

def retailerView(request):
    return render(request, 'SharpBargain/retailerView.html')

def manuDashboard(request,account_address):
    return render(request, 'SharpBargain/manuDashboard.html')

def login_test(request):
    if request.method == 'GET':

        ac = web3.toChecksumAddress(request.GET.get('ac'))
        print(ac)
        role = contract.functions.get_role(ac).call()
        role = role+"/"+ac

        return HttpResponse(
            json.dumps(role),
            content_type="application/json"
        )

def testm(request):
    return render(request,"SharpBargain/testm.html")


