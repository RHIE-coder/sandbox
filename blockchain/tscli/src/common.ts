import { ethers } from 'ethers';
import Dotenv from 'dotenv'
Dotenv.config();
const PRIVATE_KEY:string = process.env.PRIVATE_KEY!;
// const RPC_URL:string = process.env.L1_RPC_URL!;
// const RPC_URL:string = process.env.L2_RPC_URL!;
// const RPC_URL:string = process.env.L3_RPC_URL!;
// const RPC_URL:string = process.env.LOCAL_RPC_URL!;
const RPC_URL:string = process.env.RELAYER_RPC_URL!
// const RPC_URL:string = process.env.FULLNODE_RPC_URL!;
// const RPC_URL:string = process.env.ARCHIVE_RPC_URL!;
console.log(RPC_URL)

async function getProvider() {
    return new ethers.JsonRpcProvider(RPC_URL);
}

async function getWallet() {
    const provider = await getProvider()
    const wallet = new ethers.Wallet(PRIVATE_KEY);
    wallet.connect(provider)
    return wallet
}

export  {
    getProvider,
    getWallet,
}
