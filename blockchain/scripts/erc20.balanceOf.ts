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
    console.log(chalk.bgGreen.bold("L3"))
    await balanceOf(providerL3, CA.L3_ERC20,"0x6020be28F0814Cb0443A90e22B76a0a50c5214CB")
    await balanceOf(providerL3, CA.L3_ERC20,"0x3a47f6e8d3BcFBb4f1582462f0020b05194994ee")
    console.log(chalk.bgGreen.bold("L2"))
    await balanceOf(providerL2, CA.L2_ERC20,"0x3a47f6e8d3BcFBb4f1582462f0020b05194994ee")
})()