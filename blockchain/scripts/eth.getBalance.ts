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
    const balanceWei = await provider.getBalance(wallet.address);
    const balanceEther = ethers.formatEther(balanceWei);
    console.log(`Balance of ${wallet.address}: ${balanceEther} ETH`);
}

(async ()=> {
    console.log(chalk.bgGreen.bold("L1"))
    await getBalance(providerL1, walletL1)
    console.log(chalk.bgGreen.bold("L2"))
    await getBalance(providerL2, walletL2)
    console.log(chalk.bgGreen.bold("L3"))
    await getBalance(providerL3, walletL3)
})()