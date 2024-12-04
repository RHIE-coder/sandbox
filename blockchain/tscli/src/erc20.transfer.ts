import { Provider, Wallet, ethers } from 'ethers';
import { getProvider, getWallet } from './common';
import erc20ABI from './abi/erc20.json';

async function transfer(to: string | null, amount: string) {


    if (!to) {
        throw new Error('Address is required');
    }

    // Get provider and wallet (signer)
    const provider: Provider = await getProvider();
    const signer: Wallet = await getWallet();

    // Make sure the signer is connected to the provider
    const connectedSigner = signer.connect(provider);

    // Create a contract instance for the ERC-20 token
    const tokenContract = new ethers.Contract(tokenAddress, erc20ABI, connectedSigner);

    // Convert amount to the smallest unit (usually Wei or smallest token unit)
    const tokenAmount = ethers.parseUnits(amount, await tokenContract.decimals());

    try {
        // Send the transfer transaction
        const txResponse = await tokenContract.transfer(to, tokenAmount);
        console.log(`Transaction sent! Hash: ${txResponse.hash}`);

        // Wait for the transaction to be mined
        const receipt = await txResponse.wait();

        if (receipt) {
            console.log(`Transaction confirmed in block: ${receipt.blockNumber}`);
        } else {
            console.error("Transaction failed or was not mined in time.");
        }
    } catch (error) {
        console.error("Transaction failed:", error);
    }
}

(async () => {
})();
