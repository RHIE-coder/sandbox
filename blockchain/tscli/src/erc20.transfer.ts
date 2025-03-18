import { Provider, Wallet, ethers } from 'ethers';
import { getProvider, getWallet } from './common';
import erc20ABI from './ethlib/abi/erc20.json';

async function transfer(to: string | null, amount: string) {


    if (!to) {
        throw new Error('Address is required');
    }
    const tokenAddress = '0x3fc9db68F6c09089C25E2482A924c9B5C5996C46' // L1
    // const tokenAddress = '0x0fE3B8330f253890848764B893530c21E768A798' // L2
    // const tokenAddress = '0x3cfD5ac56480aF929E0D939637431b861781191A' // L3
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
    await transfer("0x9396Dd8852E41b8051C032a971995FB5a2B6E3D7", "200")
})();
