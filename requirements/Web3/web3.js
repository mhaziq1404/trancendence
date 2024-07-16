const Web3 = require('web3');
const web3 = new Web3('http://Web3:8545'); // Connect to your Ethereum node

const contractAddress = '0xContractAddress'; // Deployed contract address
const contractABI = [{"inputs":[],"name":"getGameCount","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256","name":"_index","type":"uint256"}],"name":"getGame","outputs":[{"internalType":"address","name":"player","type":"address"},{"internalType":"uint256","name":"score","type":"uint256"},{"internalType":"uint256","name":"timestamp","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256","name":"_score","type":"uint256"}],"name":"storeGameResult","outputs":[],"stateMutability":"nonpayable","type":"function"}];

const contract = new web3.eth.Contract(contractABI, contractAddress);

// Example function to store game result
async function storeGameResult(score) {
    const accounts = await web3.eth.getAccounts();
    await contract.methods.storeGameResult(score).send({ from: accounts[0] });
    console.log('Game result stored on blockchain.');
}

// Example function to retrieve game results
async function getGameResults() {
    const gameCount = await contract.methods.getGameCount().call();
    for (let i = 0; i < gameCount; i++) {
        const result = await contract.methods.getGame(i).call();
        console.log(`Game ${i + 1}: Player ${result.player}, Score ${result.score}, Timestamp ${new Date(result.timestamp * 1000)}`);
    }
}
