import json
from web3 import Web3
import time


# Fill in your infura API key here
def main():
    infura_url = "https://ropsten.infura.io/v3/f28a0b5ddee744859bda3e9f79b01b8c"
    # infura_url = "https://deaxjqnqrbvx.usemoralis.com:2053/server"
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
    address = web3.toChecksumAddress('0xAAC07FAa48619b2F0Ce852DD8B22914383Aded1a')
    User_address = web3.toChecksumAddress("0xceb45891f0b9761d9d7d950710aa5f9d785f87d6")
    contract = web3.eth.contract(address=address, abi=abi)
    SC_OWNER_ADDR = '0xF5EB01007e46c3296087063a155b5F68d9D72157'
    web3.eth.defaultAccount = User_address

    #nonce = web3.eth.getTransactionCount(SC_OWNER_ADDR)
    #print(nonce)
    # print(contract.functions.say_hi().call({'from': SC_OWNER_ADDR}))

    #transaction = contract.functions.add_retailer("0xC64367bA7165d318EC82A53b72D9806dFbF8fdE7").buildTransaction(
    #    {
    #        'gasPrice': web3.toWei('200', 'gwei'),
    #        'from': SC_OWNER_ADDR,
    #        'nonce': nonce
    #    }
    #)

    private_key = "0x380143b9a67553f5fe93c6c827b30e1cdfaf050ba75e3836878cebcff1c17af6"
    #signed_txn = web3.eth.account.signTransaction(transaction, private_key=private_key)
    #print(signed_txn)

    #txn_receipt = web3.eth.sendRawTransaction(signed_txn.rawTransaction)
    #print(txn_receipt)

    #web3.eth.waitForTransactionReceipt(txn_receipt)
    #nonce = web3.eth.getTransactionCount(SC_OWNER_ADDR)
    #print(nonce)
    #print(contract.functions.say_hi().call({'from': SC_OWNER_ADDR}))
    #transaction = contract.functions.add_retailer("0xB18Ad402c99221FdDa1E732A7719b4D744c86D16").buildTransaction(
    #   {
    #      'gasPrice':web3.eth.gasPrice,
    #       'from': SC_OWNER_ADDR,
    #       'nonce': nonce
    #    }
    #)


    #signed_txn = web3.eth.account.signTransaction(transaction, private_key=private_key)
    #print(signed_txn)

    #txn_receipt = web3.eth.sendRawTransaction(signed_txn.rawTransaction)
    #print(txn_receipt)

    #web3.eth.waitForTransactionReceipt(txn_receipt)
    #print("Done")

    nonce = web3.eth.getTransactionCount(SC_OWNER_ADDR)
    print(nonce)

    transaction = contract.functions.add_retailer("0xC64367bA7165d318EC82A53b72D9806dFbF8fdE7").buildTransaction(
        {
            'gasPrice': web3.eth.gasPrice,
            'from': SC_OWNER_ADDR,
            'nonce': nonce
        }
    )

    signed_txn = web3.eth.account.signTransaction(transaction, private_key=private_key)
    print(signed_txn)

    txn_receipt = web3.eth.sendRawTransaction(signed_txn.rawTransaction)
    print(txn_receipt)

    web3.eth.waitForTransactionReceipt(txn_receipt)
    print("Done")



if __name__ == "__main__":
    main()

