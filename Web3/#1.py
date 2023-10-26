from web3 import Web3

infura_url = "https://mainnet.infura.io/v3/d7705f44a1f24aa58ee905b2b4408441"
web3 = Web3(Web3.HTTPProvider(infura_url))
#Verificar conexion con infura
print(web3.is_connected())
#Saber el numero del bloque mas reciente
print(web3.eth.block_number)
#obtener balance de Eth de una DW
balance = web3.eth.get_balance("0x6aE7dE9548Fdb333738813c6468915719dAB6e56")
print(web3.from_wei(balance, "ether"))