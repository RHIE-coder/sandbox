import { ethers } from "ethers";

const ROLLUP_CONTRACT_ADDRESS = "0xB41a76fc71f83F1dD21c21133c3E55d3fb0E9065"; 

const provider = new ethers.JsonRpcProvider("");

// ABI 이벤트 정의
const ROLLUP_ABI = [
    "event NodeCreated(uint64 indexed nodeNum, bytes32 indexed parentNodeHash, bytes32 indexed nodeHash, bytes32 executionHash, bytes32 afterInboxBatchAcc, bytes32 wasmModuleRoot, uint256 inboxMaxCount)",
    "event NodeCreated(uint64 indexed nodeNum, bytes32 indexed parentNodeHash, bytes32 indexed nodeHash, bytes32 executionHash, tuple assertion, bytes32 afterInboxBatchAcc, bytes32 wasmModuleRoot, uint256 inboxMaxCount)",
    "event NodeConfirmed(uint64 indexed nodeNum, bytes32 blockHash, bytes32 sendRoot)"
];

// 컨트랙트 인터페이스 생성 (ethers.js v6 방식)
const contractInterface = new ethers.Interface(ROLLUP_ABI);

// 컨트랙트 인스턴스 생성
const rollupContract = new ethers.Contract(ROLLUP_CONTRACT_ADDRESS, ROLLUP_ABI, provider);

// 이벤트 조회 함수
async function fetchEvents() {
    try {
        // const fromBlock = await provider.getBlockNumber() - 500;
        const fromBlock = 0 ;
        const toBlock = "latest";

        // NodeCreated 이벤트 조회
        const nodeCreatedEvents = await rollupContract.queryFilter("NodeCreated", fromBlock, toBlock);
        console.log("🚀 NodeCreated 이벤트 로그:");
        nodeCreatedEvents.forEach(log => {
            const event = contractInterface.parseLog(log);
            if (event !== null) {  // event가 null인지 체크
                console.log({
                    nodeNum: event.args[0].toString(),
                    parentNodeHash: event.args[1],
                    nodeHash: event.args[2],
                    executionHash: event.args[3],
                    afterInboxBatchAcc: event.args[5],
                    wasmModuleRoot: event.args[6],
                    inboxMaxCount: event.args[7].toString(),
                    transactionHash: log.transactionHash
                });
            }
        });

        // NodeConfirmed 이벤트 조회
        const nodeConfirmedEvents = await rollupContract.queryFilter("NodeConfirmed", fromBlock, toBlock);
        console.log("🚀 NodeConfirmed 이벤트 로그:");
        nodeConfirmedEvents.forEach(log => {
            const event = contractInterface.parseLog(log);
            if (event !== null) {  // event가 null인지 체크
                console.log({
                    nodeNum: event.args[0].toString(),
                    blockHash: event.args[1],
                    sendRoot: event.args[2],
                    transactionHash: log.transactionHash
                });
            }
        });

    } catch (error) {
        console.error("⚠️ 이벤트 조회 중 오류 발생:", error);
    }
}

// 이벤트 조회 실행
fetchEvents();
