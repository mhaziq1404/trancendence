from flask import Flask, request, jsonify
from web3 import Web3

app = Flask(__name__)

# Connect to the Ethereum testnet (e.g., Ropsten)
infura_url = 'https://ropsten.infura.io/v3/YOUR_INFURA_PROJECT_ID'
web3 = Web3(Web3.HTTPProvider(infura_url))

# Check if connected
if not web3.isConnected():
    raise Exception("Failed to connect to the Ethereum network")

# Ethereum account and private key (for test purposes)
account = 'YOUR_TEST_ACCOUNT_ADDRESS'
private_key = 'YOUR_TEST_ACCOUNT_PRIVATE_KEY'

# Smart contract ABI and address
contract_address = 'YOUR_CONTRACT_ADDRESS'
contract_abi = [
    # Your contract's ABI here
]

contract = web3.eth.contract(address=contract_address, abi=contract_abi)

@app.route('/store_result', methods=['POST'])
def store_result():
    data = request.get_json()
    player = data['player']
    score = data['score']

    # Create a transaction
    nonce = web3.eth.getTransactionCount(account)
    tx = contract.functions.storeResult(player, score).buildTransaction({
        'chainId': 3,  # Ropsten Testnet ID
        'gas': 70000,
        'gasPrice': web3.toWei('20', 'gwei'),
        'nonce': nonce,
    })

    # Sign the transaction
    signed_tx = web3.eth.account.signTransaction(tx, private_key)

    # Send the transaction
    tx_hash = web3.eth.sendRawTransaction(signed_tx.rawTransaction)

    return jsonify({'tx_hash': web3.toHex(tx_hash)})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
