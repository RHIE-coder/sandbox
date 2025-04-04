import { ethers } from 'ethers';

const PRIVATE_KEY = ''; // 송신자 계정의 개인 키
const RPC_URL = ''; // 네트워크 RPC URL
const RECEIVER_ADDRESS = ''; // 수신자 주소
const AMOUNT_TO_SEND = ethers.parseUnits('1', 'wei');

const provider = new ethers.JsonRpcProvider(RPC_URL);
const wallet = new ethers.Wallet(PRIVATE_KEY, provider);

async function sendTransaction() {
    try {
        const tx = {
            to: RECEIVER_ADDRESS,
            value: AMOUNT_TO_SEND,
            gasLimit: 21000,
        };

        const signedTx = await wallet.sendTransaction(tx);
        const receipt = await signedTx.wait();

        if (receipt === null) {
            console.log('Error! receipt is null');
        } else {
            const block = await provider.getBlock(receipt.blockNumber);
            if (block) {
                const timestamp = Number(block.timestamp)
                console.log(
                    `block:${receipt.blockNumber}, time:${timestamp} (${new Date(
                        timestamp * 1000,
                    ).toLocaleString()}), hash: ${signedTx.hash}`,
                );
            } else {
                console.log(`Block ${receipt.blockNumber} not found.`);
            }
        }
    } catch (error) {
        console.error('Failed to send transaction:', error);
    }
}

async function startSendingTransactions() {
    console.log('Starting to send transactions every 30 seconds...');
    await sendTransaction()
    setInterval(sendTransaction, 30*1000);
}

startSendingTransactions();
