import { ethers } from 'ethers';
import Dotenv from 'dotenv'
Dotenv.config()
const PRIVATE_KEY = process.env.PRIVATE_KEY
const L1_RPC_URL = process.env.L1_RPC_URL
const L2_RPC_URL = process.env.L2_RPC_URL
const L3_RPC_URL = process.env.L3_RPC_URL

if(!PRIVATE_KEY) {
    throw new ReferenceError("PRIVATE_KEY is not exists")
}

if(!L1_RPC_URL) {
    throw new ReferenceError("L1_URL is not exists")
}
if(!L2_RPC_URL) {
    throw new ReferenceError("L2_URL is not exists")
}
if(!L3_RPC_URL) {
    throw new ReferenceError("L3_URL is not exists")
}
console.log(PRIVATE_KEY)
const providerL1 = new ethers.JsonRpcProvider(L1_RPC_URL);
const providerL2 = new ethers.JsonRpcProvider(L2_RPC_URL);
const providerL3 = new ethers.JsonRpcProvider(L3_RPC_URL);
const walletL1 = new ethers.Wallet(PRIVATE_KEY);
const walletL2 = new ethers.Wallet(PRIVATE_KEY);
const walletL3 = new ethers.Wallet(PRIVATE_KEY);
walletL1.connect(providerL1)
walletL2.connect(providerL2)
walletL3.connect(providerL3)

export {
    providerL1,
    providerL2,
    providerL3,
    walletL1,
    walletL2,
    walletL3,
}