async function loadWeb3() {
        if (window.ethereum) {
            window.web3 = new Web3(window.ethereum);
            window.ethereum.enable();
        }
    }

    async function load() {
        await loadWeb3();
        window.contract = await loadContract();
        updateStatus('Ready!');
    }

    function updateStatus(status) {
        const statusEl = document.getElementById('status');
        statusEl.innerHTML = status;
        console.log(status);
    }
    async function loadContract() {
        return await new window.web3.eth.Contract(
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
		"outputs": [
			{
				"internalType": "string",
				"name": "",
				"type": "string"
			}
		],
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
			, '0x23D774025440f42c8C2d6872c85410A362A497f9');
    }

    async function getCurrentAccount() {
        const accounts = await window.web3.eth.getAccounts();
        return accounts[0];
    }

    load();