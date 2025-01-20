import { Provider } from "ethers";
import {
    getProvider,
} from "./common";

async function blockNumber(){
    const provider:Provider = await getProvider()

    try {
      const blockNumber = await provider.getBlockNumber();
      console.log(`최신 블록 번호: ${blockNumber}`);
    } catch (error) {
      console.error('블록 번호를 조회하는 중 오류 발생:', error);
    }
  
}

(async()=>{
  await blockNumber()
})()


