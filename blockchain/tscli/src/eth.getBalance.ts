import { Provider, ethers } from "ethers";
import {
    getProvider,
    getWallet,
} from "./common";

async function getBalance(address: string | null){
    const provider:Provider = await getProvider()
    let target = null

    if(!address) {
        const wallet = await getWallet()
        target = wallet.address;
    } else {
        target = address;
    }
    const balanceWei = await provider.getBalance(target);
    const balanceEther = ethers.formatEther(balanceWei);
    console.log(`Balance of ${target}: ${balanceEther} ETH`);
}

(async()=>{
})()


