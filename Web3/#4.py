import json
import web3.eth
from web3 import Web3
ganache_url = "http://127.0.0.1:7545"
web3 = Web3(Web3.HTTPProvider(ganache_url))

web3.eth.default_account = web3.eth.accounts[0]
abi = json.loads('[
	{
		"constant": false,
		"inputs": [
			{
				"name": "_message",
				"type": "string"
			},
			{
				"name": "_name",
				"type": "string"
			}
		],
		"name": "setMessage",
		"outputs": [],
		"payable": true,
		"stateMutability": "payable",
		"type": "function"
	},
	{
		"constant": true,
		"inputs": [],
		"name": "getMessage",
		"outputs": [
			{
				"name": "",
				"type": "string"
			},
			{
				"name": "",
				"type": "string"
			}
		],
		"payable": false,
		"stateMutability": "view",
		"type": "function"
	}
]')
address = web3.to_checksum_address("0x6830EDe8c1ACa4EfCce38a42b6926583b78D3FcD")

contract = web3.eth.contract(address=address, abi=abi)

print(contract.functions.greet().call())

tx_hash = contract.functions.setGreeting('Hooola').transact()
print(tx_hash)
web3.eth.wait_for_transaction_receipt(tx_hash)
print('Updated greeting: {}'.format(
    contract.functions.greet().call()
))