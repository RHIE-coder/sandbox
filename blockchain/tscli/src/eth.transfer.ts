import { Provider, Wallet, ethers } from "ethers";
import { getProvider, getWallet } from "./common";

async function transfer(to: string | null, amount: string) {
  if (!to) {
    throw new Error("Address is required");
  }

  // Get provider and wallet (signer)
  const provider: Provider = await getProvider();
  const signer: Wallet = await getWallet();

  // Make sure the signer is connected to the provider
  const connectedSigner = signer.connect(provider);

  // Create the transaction object
  const transaction = {
    to,
    value: ethers.parseEther(amount),  // Convert amount to Wei
  };

  // Send the transaction
  try {
    const txResponse = await connectedSigner.sendTransaction(transaction);
    console.log(`Transaction sent! Hash: ${txResponse.hash}`);
    
    // Wait for the transaction to be mined
    const receipt = await txResponse.wait();

    if (receipt) {
      // Receipt is not null, so we can safely access its properties
      console.log(`Transaction confirmed in block: ${receipt.blockNumber}`);
    } else {
      console.error("Transaction failed or was not mined in time.");
    }
  } catch (error) {
    console.error("Transaction failed:", error);
  }
}

(async()=>{
})()