from django.shortcuts import render,HttpResponse,redirect
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

def index(request):
    return render(request,'SharpBargain/index.html')

def cusDashboard(request,account_address):
    print(account_address)
    return render(request, 'SharpBargain/cusDashboard.html')

def retailerDashboard(request):
    return render(request, 'SharpBargain/retailerDashboard.html')

def manuDashboard(request):
    return render(request, 'SharpBargain/manuDashboard.html')

def login_test(request):
    if request.method == 'GET':
        infura_url = "https://ropsten.infura.io/v3/f28a0b5ddee744859bda3e9f79b01b8c"
        web3 = Web3(Web3.HTTPProvider(infura_url))

        abi = json.loads(
            """
            [
            {
                "inputs": [],
                "stateMutability": "nonpayable",
                "type": "constructor"
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
                        "internalType": "address",
                        "name": "m_address",
                        "type": "address"
                    },
                    {
                        "internalType": "string",
                        "name": "prod_type",
                        "type": "string"
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
                        "name": "prod_production_date",
                        "type": "uint256"
                    },
                    {
                        "internalType": "uint256",
                        "name": "quantity",
                        "type": "uint256"
                    }
                ],
                "name": "add_product",
                "outputs": [
                    {
                        "internalType": "uint256[]",
                        "name": "",
                        "type": "uint256[]"
                    }
                ],
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
                        "internalType": "address",
                        "name": "buyer_address",
                        "type": "address"
                    },
                    {
                        "internalType": "uint256",
                        "name": "prod_id",
                        "type": "uint256"
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
                        "internalType": "uint256",
                        "name": "product_id",
                        "type": "uint256"
                    }
                ],
                "name": "buyer_view_comment",
                "outputs": [
                    {
                        "components": [
                            {
                                "internalType": "uint256",
                                "name": "prod_id",
                                "type": "uint256"
                            },
                            {
                                "internalType": "uint256",
                                "name": "batch_id",
                                "type": "uint256"
                            },
                            {
                                "internalType": "string",
                                "name": "prod_type",
                                "type": "string"
                            },
                            {
                                "internalType": "address",
                                "name": "manu_address",
                                "type": "address"
                            },
                            {
                                "internalType": "address",
                                "name": "retailer_address",
                                "type": "address"
                            },
                            {
                                "internalType": "address",
                                "name": "buyer_address",
                                "type": "address"
                            },
                            {
                                "internalType": "uint256",
                                "name": "prod_production_date",
                                "type": "uint256"
                            },
                            {
                                "internalType": "uint256",
                                "name": "procure_date",
                                "type": "uint256"
                            },
                            {
                                "internalType": "uint256",
                                "name": "purchase_date",
                                "type": "uint256"
                            },
                            {
                                "internalType": "string",
                                "name": "prod_wholesale_price",
                                "type": "string"
                            },
                            {
                                "internalType": "string",
                                "name": "purchase_retail_price",
                                "type": "string"
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
                        "internalType": "struct SharpBargain.Chain_Product[]",
                        "name": "",
                        "type": "tuple[]"
                    }
                ],
                "stateMutability": "nonpayable",
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
                        "name": "m_address",
                        "type": "address"
                    },
                    {
                        "internalType": "string",
                        "name": "p_type",
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
                        "internalType": "bool",
                        "name": "pull_all",
                        "type": "bool"
                    },
                    {
                        "internalType": "address",
                        "name": "b_address",
                        "type": "address"
                    }
                ],
                "name": "get_user_history",
                "outputs": [
                    {
                        "components": [
                            {
                                "internalType": "uint256",
                                "name": "prod_id",
                                "type": "uint256"
                            },
                            {
                                "internalType": "uint256",
                                "name": "batch_id",
                                "type": "uint256"
                            },
                            {
                                "internalType": "string",
                                "name": "prod_type",
                                "type": "string"
                            },
                            {
                                "internalType": "address",
                                "name": "manu_address",
                                "type": "address"
                            },
                            {
                                "internalType": "address",
                                "name": "retailer_address",
                                "type": "address"
                            },
                            {
                                "internalType": "address",
                                "name": "buyer_address",
                                "type": "address"
                            },
                            {
                                "internalType": "uint256",
                                "name": "prod_production_date",
                                "type": "uint256"
                            },
                            {
                                "internalType": "uint256",
                                "name": "procure_date",
                                "type": "uint256"
                            },
                            {
                                "internalType": "uint256",
                                "name": "purchase_date",
                                "type": "uint256"
                            },
                            {
                                "internalType": "string",
                                "name": "prod_wholesale_price",
                                "type": "string"
                            },
                            {
                                "internalType": "string",
                                "name": "purchase_retail_price",
                                "type": "string"
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
                        "internalType": "struct SharpBargain.Chain_Product[]",
                        "name": "",
                        "type": "tuple[]"
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
                    }
                ],
                "name": "manu_get_all_data",
                "outputs": [
                    {
                        "components": [
                            {
                                "internalType": "uint256",
                                "name": "prod_id",
                                "type": "uint256"
                            },
                            {
                                "internalType": "uint256",
                                "name": "batch_id",
                                "type": "uint256"
                            },
                            {
                                "internalType": "string",
                                "name": "prod_type",
                                "type": "string"
                            },
                            {
                                "internalType": "address",
                                "name": "manu_address",
                                "type": "address"
                            },
                            {
                                "internalType": "address",
                                "name": "retailer_address",
                                "type": "address"
                            },
                            {
                                "internalType": "address",
                                "name": "buyer_address",
                                "type": "address"
                            },
                            {
                                "internalType": "uint256",
                                "name": "prod_production_date",
                                "type": "uint256"
                            },
                            {
                                "internalType": "uint256",
                                "name": "procure_date",
                                "type": "uint256"
                            },
                            {
                                "internalType": "uint256",
                                "name": "purchase_date",
                                "type": "uint256"
                            },
                            {
                                "internalType": "string",
                                "name": "prod_wholesale_price",
                                "type": "string"
                            },
                            {
                                "internalType": "string",
                                "name": "purchase_retail_price",
                                "type": "string"
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
                        "internalType": "struct SharpBargain.Chain_Product[]",
                        "name": "",
                        "type": "tuple[]"
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
                        "name": "r_address",
                        "type": "address"
                    }
                ],
                "name": "retailer_get_all_prod_type",
                "outputs": [
                    {
                        "internalType": "string[]",
                        "name": "",
                        "type": "string[]"
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
                        "name": "quantity",
                        "type": "uint256"
                    }
                ],
                "name": "retailer_purchase_from_manu_demo",
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
                        "internalType": "uint256[]",
                        "name": "pid_array",
                        "type": "uint256[]"
                    }
                ],
                "name": "retailer_purchase_from_manu_final",
                "outputs": [],
                "stateMutability": "nonpayable",
                "type": "function"
            },
            {
                "inputs": [
                    {
                        "internalType": "address",
                        "name": "r_address",
                        "type": "address"
                    },
                    {
                        "internalType": "string",
                        "name": "p_type",
                        "type": "string"
                    }
                ],
                "name": "retailer_view_comment",
                "outputs": [
                    {
                        "components": [
                            {
                                "internalType": "uint256",
                                "name": "prod_id",
                                "type": "uint256"
                            },
                            {
                                "internalType": "uint256",
                                "name": "batch_id",
                                "type": "uint256"
                            },
                            {
                                "internalType": "string",
                                "name": "prod_type",
                                "type": "string"
                            },
                            {
                                "internalType": "address",
                                "name": "manu_address",
                                "type": "address"
                            },
                            {
                                "internalType": "address",
                                "name": "retailer_address",
                                "type": "address"
                            },
                            {
                                "internalType": "address",
                                "name": "buyer_address",
                                "type": "address"
                            },
                            {
                                "internalType": "uint256",
                                "name": "prod_production_date",
                                "type": "uint256"
                            },
                            {
                                "internalType": "uint256",
                                "name": "procure_date",
                                "type": "uint256"
                            },
                            {
                                "internalType": "uint256",
                                "name": "purchase_date",
                                "type": "uint256"
                            },
                            {
                                "internalType": "string",
                                "name": "prod_wholesale_price",
                                "type": "string"
                            },
                            {
                                "internalType": "string",
                                "name": "purchase_retail_price",
                                "type": "string"
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
                        "internalType": "struct SharpBargain.Chain_Product[]",
                        "name": "",
                        "type": "tuple[]"
                    }
                ],
                "stateMutability": "nonpayable",
                "type": "function"
            },
            {
                "inputs": [
                    {
                        "internalType": "string",
                        "name": "input_comment",
                        "type": "string"
                    },
                    {
                        "internalType": "uint8",
                        "name": "input_rate",
                        "type": "uint8"
                    },
                    {
                        "internalType": "uint256",
                        "name": "product_id",
                        "type": "uint256"
                    }
                ],
                "name": "set_comment",
                "outputs": [],
                "stateMutability": "nonpayable",
                "type": "function"
            }
        ]

            """)

        # smart contract address
        address = web3.toChecksumAddress('0x0DbE5540e23925849f2E6F5237ff4E0D89312790')
        contract = web3.eth.contract(address=address, abi=abi)
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
