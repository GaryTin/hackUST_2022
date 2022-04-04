from django.shortcuts import render, HttpResponse, redirect
import json
from web3 import Web3
from django.middleware.csrf import get_token
from django.template import RequestContext, Template
import time
from .forms import *
from .models import *
import datetime
from dateutil.relativedelta import relativedelta

# Create your views here.
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
				"internalType": "address",
				"name": "r_address",
				"type": "address"
			},
			{
				"internalType": "string",
				"name": "_prod_type",
				"type": "string"
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
	}
]
    """)
# smart contract address
address = web3.toChecksumAddress('0x8dCEDE30c2a8bD175654b67e010F898061fF0072')
contract = web3.eth.contract(address=address, abi=abi)
data_dic = {"Jan": 1, "Feb": 2, "Mar": 3, "Apr": 4, "May": 5, "Jun": 6, "Jul": 7, "Aug": 8, "Sep": 9, "Oct": 10,
            "Nov": 11, "Dec": 12}


def home(request):
    return render(request, 'SharpBargain/home.html')


def Test(request):
    if request.method == "POST" and 'run' in request.POST:
        print("start")
        print(request.POST["v1"])
        print(request.POST["v2"])
        print(request.POST["userAddress"])
        return render(request, 'SharpBargain/test.html')
    else:
        return render(request, 'SharpBargain/test.html')


def MetaMaskTestPage(request):
    return render(request, 'SharpBargain/MetaMaskTestPage.html', )


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
    return render(request, 'SharpBargain/index.html')


def cusHistory(request, account_address):
    user_ac = web3.toChecksumAddress(account_address)
    user_history_raw = contract.functions.get_user_history(user_ac).call({'from': user_ac})
    # print(user_history_raw) #[prod_type/prod_id/purchase_date/price/comment/rate],[.....
    img_urls = None
    user_history = {}
    user_historys = []
    next_open_bracket_index = 0
    count = 0
    buy_count = 0
    total_payment = 0
    uncomment_count = 0
    check = True
    while (check and count < 10):
        close_bracket_index = user_history_raw.find(']')
        next_open_bracket_index = close_bracket_index + 2
        one_history = user_history_raw[1:close_bracket_index]  # prod_type/prod_id/purchase_date/price/comment/rate
        history_array = one_history.split('/')
        py_date = int(history_array[2]) / 1000
        one_week_before = py_date - (3600 * 24 * 7)
        if (py_date >= one_week_before):
            buy_count = buy_count + 1
            total_payment = total_payment + float(history_array[3])
            uncomment_count = uncomment_count + (1 if history_array[4] == "" else 0)
        if (py_date >= one_week_before or count < 10):
            time_temp = str(time.ctime(py_date)).split(" ")
            time_temp[:] = [x for x in time_temp if x != '']

            prod_type = history_array[0][0:history_array[0].rfind('_')]

            product = DB_Product.objects.get(prod_type=history_array[0])
            format_time = time_temp[2] + "/" + str(data_dic[time_temp[1]]) + "/" + time_temp[4]

            user_history = {"prod_type": prod_type, "prod_id": history_array[1], "purchase_date": format_time,
                            "price": history_array[3], "not_comment": history_array[4] == "",
                            "img_url": product.prod_img.url}
            user_historys.append(user_history)
            count = count + 1
        check = False
        if (next_open_bracket_index < len(user_history_raw)):
            user_history_raw = user_history_raw[next_open_bracket_index:]
            check = True
    return render(request, 'SharpBargain/cusHistory.html', {
        "user_historys": user_historys,
        "buy_count": buy_count,
        "total_payment": total_payment,
        "uncomment_count": uncomment_count,
    })


def cusComment(request, account_address, product_id):
    status = ""
    if (product_id == 0):
        is_show = False
        prod_type = ""
        purchase_date = ""
        price = ""
        format_time = ""
        img_url = ""
        product_data = [[]]
    else:
        is_show = True

        user_ac = web3.toChecksumAddress(account_address)
        product_data = contract.functions.get_uncomment_prod_by_id(user_ac, product_id).call({'from': user_ac})[
                       1:-2].split('/')
        print(product_data)
        if (len(product_data) == 1):
            is_show = False
            prod_type = ""
            purchase_date = ""
            price = ""
            format_time = ""
            img_url = ""
            product_data = [[]]
            status = "Already comment!"
        else:
            prod_type = product_data[0][0:product_data[0].rfind('_')]
            purchase_date = int(product_data[2])
            price = product_data[3]
            py_date = int(product_data[2]) / 1000
            time_temp = str(time.ctime(py_date)).split(" ")
            time_temp[:] = [x for x in time_temp if x != '']
            format_time = time_temp[2] + "/" + str(data_dic[time_temp[1]]) + "/" + time_temp[4]
            # print(product_data)
            product = DB_Product.objects.get(prod_type=product_data[0])
            img_url = product.prod_img.url
    return render(request, 'SharpBargain/cusComment.html',
                  {
                      "is_show": is_show,
                      'prod_id': product_id,
                      "prod_type": prod_type,
                      "purchase_date": format_time,
                      "price": price,
                      "img_url": img_url,
                      "prod_type_raw": product_data[0],
                      "status": status,
                  })


def cusView(request, account_address, product_id):
    comment_data = []
    f_comment_data = ""
    other_comment_data = ""
    if product_id == 0:
        is_show = False
    else:
        is_show = True
        user_ac = web3.toChecksumAddress(account_address)
        comment_data_raw = contract.functions.buyer_view_comment(product_id).call({'from': user_ac}).split(",")
        comment_count = len(comment_data_raw)
        if (comment_count == 0):
            is_show = False
        else:
            comment_data_raw[:] = [x[1:-1] for x in comment_data_raw]
            comment_data_raw = comment_data_raw[:-1]
            comment_data = []
            count = 0
            for data in comment_data_raw:

                data = data.split("/")
                prod_type = data[1][:data[1].rfind("_")]

                py_date = int(data[0]) / 1000
                time_temp = str(time.ctime(py_date)).split(" ")
                time_temp[:] = [x for x in time_temp if x != '']
                format_time = time_temp[2] + "/" + str(data_dic[time_temp[1]]) + "/" + time_temp[4]
                comment = data[2]
                rate = int(data[3])
                star = []
                for i in range(1, 6):
                    if i == rate:
                        star.append("checked")
                    else:
                        star.append("")
                product = DB_Product.objects.get(prod_type=data[1])
                img_url = product.prod_img.url

                temp_d = {"prod_type": prod_type, "date": format_time, "comment": comment, "rate": rate, "s1": star[0],
                          "s2": star[1], "s3": star[2], "s4": star[3], "s5": star[4], "img_url": img_url, "pk": count}
                count = count + 1
                comment_data.append(temp_d)

            print(comment_data)
    if (len(comment_data) == 1):
        f_comment_data = comment_data[0]
    elif (len(comment_data) > 1):
        f_comment_data = comment_data[0]
        other_comment_data = comment_data[1:]
    else:
        is_show = False

    return render(request, 'SharpBargain/cusView.html',
                  {
                      "is_show": is_show,
                      "f_comment_data": f_comment_data,
                      "other_comment_data": other_comment_data,

                  })


def cusDashboard(request, account_address):
    user_ac = web3.toChecksumAddress(account_address)
    user_history_raw = contract.functions.get_user_history(user_ac).call({'from': user_ac})
    # print(user_history_raw) #[prod_type/prod_id/purchase_date/price/comment/rate],[.....
    img_urls = None
    user_history = {}
    user_historys = []
    next_open_bracket_index = 0
    count = 0
    buy_count = 0
    total_payment = 0
    uncomment_count = 0
    check = True
    while (check and count < 10):
        close_bracket_index = user_history_raw.find(']')
        next_open_bracket_index = close_bracket_index + 2
        one_history = user_history_raw[1:close_bracket_index]  # prod_type/prod_id/purchase_date/price/comment/rate
        history_array = one_history.split('/')
        py_date = int(history_array[2]) / 1000
        one_week_before = time.time() - (3600 * 24 * 7)

        if (py_date >= one_week_before):
            buy_count = buy_count + 1
            total_payment = total_payment + float(history_array[3])
            uncomment_count = uncomment_count + (1 if history_array[4] == "" else 0)
        if (py_date >= one_week_before or count < 10):
            time_temp = str(time.ctime(py_date)).split(" ")
            time_temp[:] = [x for x in time_temp if x != '']

            prod_type = history_array[0][0:history_array[0].rfind('_')]

            product = DB_Product.objects.get(prod_type=history_array[0])
            format_time = time_temp[2] + "/" + str(data_dic[time_temp[1]]) + "/" + time_temp[4]
            user_history = {"prod_type": prod_type, "prod_id": history_array[1], "purchase_date": format_time,
                            "price": history_array[3], "not_comment": history_array[4] == "",
                            "img_url": product.prod_img.url}
            user_historys.append(user_history)
            count = count + 1
        check = False
        if (next_open_bracket_index < len(user_history_raw)):
            user_history_raw = user_history_raw[next_open_bracket_index:]
            check = True

    return render(request, 'SharpBargain/cusDashboard.html', {
        "user_historys": user_historys,
        "buy_count": buy_count,
        "total_payment": total_payment,
        "uncomment_count": uncomment_count,
    })


def retailerDashboard(request, account_address):
    user_ac = web3.toChecksumAddress(account_address)
    retailer_prod_type_array = list(
        set(contract.functions.retailer_get_all_prod_type(user_ac).call({'from': user_ac}).split(",")[:-1]))
    total_comment_count_last_30_days = 0
    total_rate_sum = 0
    total_count = 0
    comment_count_all = 0
    highest_rate_prod = "--"
    max = -1
    for retailer_prod_type_raw in retailer_prod_type_array:
        rate_sum = 0
        comment_data_array = contract.functions.retailer_view_comment(user_ac, retailer_prod_type_raw).call(
            {'from': user_ac}).split(
            ",")[:-1]
        comment_count_all = len(comment_data_array)

        for full_comment_data in comment_data_array:
            full_comment_data = full_comment_data[1:-1].split("/")
            rate_sum = rate_sum + int(full_comment_data[2])

            py_date = int(full_comment_data[0]) / 1000
            one_week_before = time.time() - (3600 * 24 * 30)

            if (py_date >= one_week_before):
                total_comment_count_last_30_days = total_comment_count_last_30_days + 1
        if comment_count_all == 0:
            average_rate = 0
        else:
            average_rate = rate_sum / comment_count_all
        # print(average_rate)

        if (average_rate > max):
            highest_rate_prod = retailer_prod_type_raw[:retailer_prod_type_raw.rfind("_")]
        # print(total_comment_count_last_30_days)
        total_rate_sum = total_rate_sum + rate_sum
        total_count = total_count + comment_count_all

    if comment_count_all == 0:
        total_average_rate = 0
    else:
        total_average_rate = str(total_rate_sum / total_count)
        total_average_rate = total_average_rate[0:total_average_rate.find(".") + 2]

    return render(request, 'SharpBargain/retailerDashboard.html',
                  {
                      "total_comment_count_last_30_days": total_comment_count_last_30_days,
                      "total_average_rate": total_average_rate,
                      "highest_rate_prod": highest_rate_prod,
                  })


def retailerPOS(request, account_address):
    return render(request, 'SharpBargain/retailerPOS.html')


def retailerView(request, account_address):
    user_ac = web3.toChecksumAddress(account_address)
    retailer_prod_type_array = list(
        set(contract.functions.retailer_get_all_prod_type(user_ac).call({'from': user_ac}).split(",")[:-1]))
    print(retailer_prod_type_array)
    prod_type_data = []
    for full_prod_type in retailer_prod_type_array:
        product = DB_Product.objects.get(prod_type=full_prod_type)
        img_url = product.prod_img.url
        temp = {"prod_type": full_prod_type[:full_prod_type.rfind("_")],
                "address": full_prod_type[full_prod_type.rfind("_") + 1:], "img_url": img_url}
        prod_type_data.append(temp)

    return render(request, 'SharpBargain/retailerView.html',
                  {
                      "prod_type_data": prod_type_data,

                  })


def retailerViewComment(request, account_address, prod_type):
    user_ac = web3.toChecksumAddress(account_address)
    comment_data_array = contract.functions.retailer_view_comment(user_ac, prod_type).call({'from': user_ac}).split(
        ",")[:-1]
    # print(comment_data_array)
    comment_data = []
    for full_comment_data in comment_data_array:
        full_comment_data = full_comment_data[1:-1].split("/")
        py_date = int(full_comment_data[0]) / 1000
        time_temp = str(time.ctime(py_date)).split(" ")
        time_temp[:] = [x for x in time_temp if x != '']
        format_time = time_temp[2] + "/" + str(data_dic[time_temp[1]]) + "/" + time_temp[4]
        comment = full_comment_data[1]
        rate = int(full_comment_data[2])
        star = []
        for i in range(1, 6):
            if i == rate:
                star.append("checked")
            else:
                star.append("")
        temp = {"date": format_time, "comment": comment, "s1": star[0], "s2": star[1], "s3": star[2], "s4": star[3],
                "s5": star[4]}
        comment_data.append(temp)

    return render(request, 'SharpBargain/retailerViewComment.html',
                  {
                      "prod_type": prod_type[:prod_type.rfind("_")],
                      "comment_data": comment_data,

                  })


def manuDashboard(request, account_address):
    user_ac = web3.toChecksumAddress(account_address)
    manu_data_raw = contract.functions.manu_get_all_data(user_ac).call({'from': user_ac}).split(",")[:-1]
    manu_data_raw[:] = [x[1:-1].split("/") for x in manu_data_raw]
    prod_type_in_stock_dict = {}
    total = len(manu_data_raw)
    r_count = 0
    for data in manu_data_raw:
        prod_type = data[0][:data[0].rfind("_")]
        product = DB_Product.objects.get(prod_type=data[0])
        img_url = product.prod_img.url
        if prod_type in prod_type_in_stock_dict:
            if (data[4] == "In manufacturer stock"):
                prod_type_in_stock_dict[prod_type]["Stock"] = prod_type_in_stock_dict[prod_type]["Stock"] + 1

            prod_type_in_stock_dict[prod_type]["Total"] = prod_type_in_stock_dict[prod_type]["Total"] + 1

        else:
            prod_type_in_stock_dict[prod_type] = {"prod_type": prod_type, "Total": 1,
                                                  "Stock": (1 if data[4] == "In manufacturer stock" else 0),
                                                  "sell_rate": 0, "img_url": img_url}
            r_count = r_count +1
        prod_type_in_stock_dict[prod_type]["sell_rate"] = str(
            (prod_type_in_stock_dict[prod_type]["Total"] - prod_type_in_stock_dict[prod_type]["Stock"]) / \
            prod_type_in_stock_dict[prod_type]["Total"] * 100)
        prod_type_in_stock_dict[prod_type]["sell_rate"] = prod_type_in_stock_dict[prod_type]["sell_rate"][
                                                          :prod_type_in_stock_dict[prod_type]["sell_rate"].find(
                                                              ".") + 3]
    prod_type_in_stock_list = list(prod_type_in_stock_dict.values())
    best_sell_item = max(prod_type_in_stock_list, key=lambda x: float(x['sell_rate']))["prod_type"]
    print(best_sell_item)

    return render(request, 'SharpBargain/manuDashboard.html',
                  {
                      "best_sell_item":best_sell_item,
                      "total":total,
                      "r_count":r_count,
                  })


def manuProdInput(request):
    if request.method == "GET":
        ai_form = add_img_form()

        return render(request, 'SharpBargain/manuProdInput.html',
                      {
                          "add_img_form": ai_form,
                      })
    elif request.method == "POST":
        ai_form = add_img_form(request.POST, request.FILES)
        if ai_form.is_valid():  # check valid
            ai_form.save()  # save to DB
        ai_form = add_img_form()
        return render(request, "SharpBargain/manuProdInput.html",
                      {
                          "add_img_form": ai_form,
                      })


def manuWS(request):
    return render(request, 'SharpBargain/manuWS.html')


def manuView(request, account_address):
    user_ac = web3.toChecksumAddress(account_address)
    manu_data_raw = contract.functions.manu_get_all_data(user_ac).call({'from': user_ac}).split(",")[:-1]
    manu_data_raw[:] = [x[1:-1].split("/") for x in manu_data_raw]
    prod_type_in_stock_dict = {}
    for data in manu_data_raw:
        prod_type = data[0][:data[0].rfind("_")]
        product = DB_Product.objects.get(prod_type=data[0])
        img_url = product.prod_img.url
        if prod_type in prod_type_in_stock_dict:
            if (data[4] == "In manufacturer stock"):
                prod_type_in_stock_dict[prod_type]["Stock"] = prod_type_in_stock_dict[prod_type]["Stock"] + 1

            prod_type_in_stock_dict[prod_type]["Total"] = prod_type_in_stock_dict[prod_type]["Total"] + 1

        else:
            prod_type_in_stock_dict[prod_type] = {"prod_type": prod_type, "Total": 1,
                                                  "Stock": (1 if data[4] == "In manufacturer stock" else 0),
                                                  "sell_rate": 0, "img_url": img_url}
        prod_type_in_stock_dict[prod_type]["sell_rate"] = str(
            (prod_type_in_stock_dict[prod_type]["Total"] - prod_type_in_stock_dict[prod_type]["Stock"]) / \
            prod_type_in_stock_dict[prod_type]["Total"] * 100)
        prod_type_in_stock_dict[prod_type]["sell_rate"] = prod_type_in_stock_dict[prod_type]["sell_rate"][
                                                          :prod_type_in_stock_dict[prod_type]["sell_rate"].find(
                                                              ".") + 3]
    prod_type_in_stock_list = list(prod_type_in_stock_dict.values())
    return render(request, 'SharpBargain/manuView.html',
                  {
                      "prod_type_in_stock_list": prod_type_in_stock_list,

                  })


def manuViewData(request, account_address, prod_type):
    user_ac = web3.toChecksumAddress(account_address)
    manu_data_raw = contract.functions.manu_get_all_data(user_ac).call({'from': user_ac}).split(",")[:-1]
    manu_data_raw[:] = [x[1:-1].split("/") for x in manu_data_raw if
                        x[1:-1].split("/")[0][:x[1:-1].split("/")[0].rfind("_") + 1] + (
                        x[1:-1].split("/")[0][x[1:-1].split("/")[0].rfind("_") + 1:]).lower() == prod_type]  #
    in_m_stock = 0
    in_r_stock = 0
    sold = 0
    time_array = []
    py_time_array = []
    show_month = 6
    count = [0] * show_month
    data_dict = {}
    for i in range(show_month):
        date = (datetime.datetime.today().replace(day=1) + relativedelta(months=-(i))).timestamp()
        py_time_array.append(date)

        month = (datetime.datetime.today().replace(day=1) + relativedelta(months=-(i))).strftime('%B')[:3]
        time_array.append(month)
    #print(time_array, py_time_array)
    retailer_list =[]
    for data in manu_data_raw:
        status = data[4]

        retailer_address = data[1]
        if (retailer_address not in data_dict and retailer_address!=""):
            data_dict[retailer_address] = {"address":"0x"+retailer_address,"count":count,"in_stock":0,"sold":0,"total":0}

        if (retailer_address!=""):
            py_date = float(data[2])/1000
            loop_count = 0
            for py_date_ref in py_time_array:
                if (py_date>=py_date_ref):
                    data_dict[retailer_address]["count"][loop_count] = data_dict[retailer_address]["count"][loop_count] + 1
                    break
                loop_count = loop_count +1

        if status == "In manufacturer stock":
            in_m_stock = in_m_stock + 1
        elif status == "In retailer stock":
            in_r_stock = in_r_stock + 1
            data_dict[retailer_address]["in_stock"] = data_dict[retailer_address]["in_stock"] + 1
            data_dict[retailer_address]["total"] = data_dict[retailer_address]["total"] + 1
        elif status == "Sold to Buyer":
            sold = sold + 1
            data_dict[retailer_address]["sold"] = data_dict[retailer_address]["sold"] + 1
            data_dict[retailer_address]["total"] = data_dict[retailer_address]["total"] + 1

    data_list = list(data_dict.values())
    print(data_list)
    total = in_m_stock + in_r_stock + sold
    in_m_stock_ratio = str(in_m_stock/total *100)
    in_m_stock_ratio = in_m_stock_ratio[:in_m_stock_ratio.find(".")+3]
    in_r_stock_ratio = str(in_r_stock / total *100)
    in_r_stock_ratio = in_r_stock_ratio[:in_r_stock_ratio.find(".") + 3]
    sold_ratio = str(sold / total *100)
    sold_ratio = sold_ratio[:sold_ratio.find(".") + 3]

    return render(request, 'SharpBargain/manuViewData.html',
                  {
                      "in_m_stock_ratio":in_m_stock_ratio,
                      "in_r_stock_ratio":in_r_stock_ratio,
                      "sold_ratio":sold_ratio,
                      "prod_type":prod_type[:prod_type.rfind("_")],
                      "in_m_stock": in_m_stock,
                      "in_r_stock": in_r_stock,
                      "sold": sold,
                      "time_array": time_array,
                      "data_list":data_list,
                  })


def login_test(request):
    if request.method == 'GET':
        ac = web3.toChecksumAddress(request.GET.get('ac'))
        print(ac)
        role = contract.functions.get_role(ac).call()
        role = role + "/" + ac

        return HttpResponse(
            json.dumps(role),
            content_type="application/json"
        )


def testm(request):
    if request.method == "GET":
        ai_form = add_img_form()
        return render(request, "SharpBargain/testm.html",
                      {
                          "add_img_form": ai_form,
                      })
    elif request.method == "POST":
        ai_form = add_img_form(request.POST, request.FILES)
        if ai_form.is_valid():  # check valid
            ai_form.save()  # save to DB
        ai_form = add_img_form()
        return render(request, "SharpBargain/testm.html",
                      {
                          "add_img_form": ai_form,
                      })
