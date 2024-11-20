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
} from "~/scripts/common"

async function getBalance(provider: Provider, wallet: Wallet){
    const address = "0xC3BC986F678c2008fc374712A8E9415c31B57012"
    const balanceWei = await provider.getBalance(wallet.address);
    // const balanceWei = await provider.getBalance(address);
    const balanceEther = ethers.formatEther(balanceWei);
    console.log(`Balance of ${wallet.address}: ${balanceEther} ETH`);
    // console.log(`Balance of ${address}: ${balanceEther} ETH`);
}

(async ()=> {
    console.log(chalk.bgGreen.bold("L1"))
    await getBalance(providerL1, walletL1)
    console.log(chalk.bgGreen.bold("L2"))
    await getBalance(providerL2, walletL2)
    console.log(chalk.bgGreen.bold("L3"))
    await getBalance(providerL3, walletL3)
})()