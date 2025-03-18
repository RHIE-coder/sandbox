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
  // await transfer('0x9396Dd8852E41b8051C032a971995FB5a2B6E3D7', '0.499156771898123')
  await transfer('0x9396Dd8852E41b8051C032a971995FB5a2B6E3D7', '1')
  // await transfer('0xccc52a0c0D24D40F4813FcB4f8E53630822FB7E8', '0.2')
  // await transfer("0xC3BC986F678c2008fc374712A8E9415c31B57012", "7654321")
  // await transfer("0x4614c14075a969A5F1FFD3961dE8A074a7BB8AfE", "1000")
  // await transfer("0xaaa85E444cfA3EA5F6bf65DDeb69b0d89037C754", "1000")
})()