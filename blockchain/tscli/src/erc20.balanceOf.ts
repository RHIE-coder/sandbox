import { Provider, ethers } from "ethers";
import {
    getProvider,
    getWallet,
} from "./common";
import erc20ABI from "./ethlib/abi/erc20.json";

async function balanceOf(address: string | null){


    const provider:Provider = await getProvider()
    let target = null

    if(!address) {
        const wallet = await getWallet()
        target = wallet.address;
    } else {
        target = address;
    }
    
    const contract = new ethers.Contract(tokenAddress, erc20ABI, provider);
    const balanceWei = await contract.balanceOf(target);
    const symbol = await contract.symbol();
    const balanceEther = ethers.formatEther(balanceWei);
    console.log(`ERC20 Token Balance of ${target}: ${balanceEther} ${symbol}`);
}



(async()=>{
})()