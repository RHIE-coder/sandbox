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
    await getBalance(null)
    await getBalance('0x9396Dd8852E41b8051C032a971995FB5a2B6E3D7')
    await getBalance("0xaaa85E444cfA3EA5F6bf65DDeb69b0d89037C754")
    await getBalance("0xbbb06fe690b20917f558879a8283132A80D34B7E")
    await getBalance("0xccc52a0c0D24D40F4813FcB4f8E53630822FB7E8")
    await getBalance("0xddd0591929FF4f8AAC827C9c31fec2dAEBBC84d7")
    await getBalance("0xeeeC155568E828c68b3FF617Ec04B6A153F7A59a")
})()


