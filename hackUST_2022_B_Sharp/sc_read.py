import json
from web3 import Web3


# Fill in your infura API key here
def main():
    infura_url = "https://ropsten.infura.io/v3/f28a0b5ddee744859bda3e9f79b01b8c"
    # infura_url = "https://deaxjqnqrbvx.usemoralis.com:2053/server"
    web3 = Web3(Web3.HTTPProvider(infura_url))

    abi = json.loads(
    """
    [
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
				"internalType": "uint256",
				"name": "pro_date",
				"type": "uint256"
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
				"internalType": "uint256",
				"name": "pro_date",
				"type": "uint256"
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
	},
	{
		"inputs": [],
		"stateMutability": "nonpayable",
		"type": "constructor"
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
	}
]
    """)

    # smart contract address
    address = web3.toChecksumAddress('0xfe5E3b5A9490B116aCF1FB0e6f9635e91853Bbe4')
    User_address = web3.toChecksumAddress("0xceb45891f0b9761d9d7d950710aa5f9d785f87d6")
    contract = web3.eth.contract(address=address, abi=abi)
    SC_OWNER_ADDR = '0xF5EB01007e46c3296087063a155b5F68d9D72157'
    web3.eth.defaultAccount = User_address

    #nonce = web3.eth.getTransactionCount(SC_OWNER_ADDR)
    #print(nonce)
    #print(contract.functions.get_role('0xcEB45891F0b9761D9d7D950710aA5f9d785F87d6').call({'from': SC_OWNER_ADDR}))
    #print(web3.eth.gasPrice)
    m_address = web3.toChecksumAddress('0xcEB45891F0b9761D9d7D950710aA5f9d785F87d6')
    print(contract.functions.manu_get_all_data(m_address).call({'from': m_address}))

if __name__ == "__main__":
    main()

