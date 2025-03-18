import { Provider, ethers } from "ethers";
import {
    getProvider,
    getWallet,
} from "./common";
import erc20ABI from "./ethlib/abi/erc20.json";

async function balanceOf(address: string | null){

    // const tokenAddress = '0x3fc9db68F6c09089C25E2482A924c9B5C5996C46' // L1
    // const tokenAddress = '0x0fE3B8330f253890848764B893530c21E768A798' // L2
    // const tokenAddress = '0x3cfD5ac56480aF929E0D939637431b861781191A' // L3
    const tokenAddress = '0x7a1edDA8CfF0FA8C50b33494e40560F229378C00' // L3 
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
    // await balanceOf("0x9396Dd8852E41b8051C032a971995FB5a2B6E3D7")
    // await balanceOf("0x5ec6337A97Da31103b7BE2E4D22e986b1923f49a")
    // await balanceOf("0xaaa85E444cfA3EA5F6bf65DDeb69b0d89037C754")
    // await balanceOf("0xbbb06fe690b20917f558879a8283132A80D34B7E")
    // await balanceOf("0xccc52a0c0D24D40F4813FcB4f8E53630822FB7E8")
    // await balanceOf("0xddd0591929FF4f8AAC827C9c31fec2dAEBBC84d7")
    // await balanceOf("0xeeeC155568E828c68b3FF617Ec04B6A153F7A59a")
    await balanceOf("0x0e0116df0180f3800900019c06a9d7698670c574")
})()