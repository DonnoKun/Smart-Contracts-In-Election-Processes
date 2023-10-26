from web3 import Web3

ganache_url = "http://127.0.0.1:7545"
web3 = Web3(Web3.HTTPProvider(ganache_url))

account_1 = "0x356A13AeC4831ffca831b57384bb7A7767e1Ad8c"
account_2 = "0xaA6Ce266526EeCBc6Cd8a9569ff40c524Ba86fe6"
private_key_1 = "0x12383f7e4c7ea1d73ce30d67c6ba9a43a281ee7d6fbe6c83a0a8482ad11426a2"
private_key_2 = "0xb025d7208134ec5b83b6f04924d7cee70fbafbe1fc5e623742e8a1cb56b9b5a1"

# Conseguir el Nonce
nonce = web3.eth.get_transaction_count(account_2)
# Construir la transaccion
tx = {
    'nonce': nonce,
    'to': account_1,
    'value': web3.to_wei(1, 'ether'),
    'gas': 2000000,
    'gasPrice': web3.to_wei('50', 'gwei')

}
# Firmar la transaccion
signed_tx = web3.eth.account.sign_transaction(tx, private_key_2)
# Se envia la transaccion
# Conseguir el hash de la transaccion
tx_hash = web3.eth.send_raw_transaction(signed_tx.rawTransaction)
print(web3.to_hex(tx_hash))