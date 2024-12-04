import chalk from 'chalk';
import { ethers } from "ethers";
import { Provider, Wallet} from "ethers";
import {
    providerL1,
    providerL2,
    providerL3,
    walletL1,
    walletL2,
    walletL3,
} from "./common";
import erc20ABI from "./abi/erc20.json";
import {
    CA
} from "./common/addresses"

async function balanceOf(provider:Provider, contractAddress:string, address:string){
    const contract = new ethers.Contract(contractAddress, erc20ABI, provider);
    const balanceWei = await contract.balanceOf(address);
    const symbol = await contract.symbol();
    const balanceEther = ethers.formatEther(balanceWei);
    console.log(`Balance of ${address}: ${balanceEther} ${symbol}`);
}

(async ()=> {
    // console.log(chalk.bgGreen.bold("L3"))
    // await balanceOf(providerL3, "0x5066926aa0038724423A03D68514b06d7a65812C","0xaaa85E444cfA3EA5F6bf65DDeb69b0d89037C754")
    console.log(chalk.bgGreen.bold("L2"))
    await balanceOf(providerL2, "0x5066926aa0038724423A03D68514b06d7a65812C","0xd644352A429F3fF3d21128820DcBC53e063685b1")
})()