import { JsonRpcProvider } from "ethers";
import {
    getProvider,
} from "./common";

async function blockNumber(){
    const provider:JsonRpcProvider = await getProvider()

    try {
      const syncingStatus = await provider.send('eth_syncing',[]);
      if (syncingStatus === false) {
        console.log('노드가 동기화되었습니다.');
      } else {
        console.log('노드가 동기화 중입니다:', syncingStatus);
      }
    } catch (error) {
      console.error('동기화 상태를 조회하는 중 오류 발생:', error);
    }
  
}

(async()=>{
  await blockNumber()
})()


