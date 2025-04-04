import http from 'k6/http';
import { check, sleep } from 'k6';

// Ethereum JSON-RPC 서버 URL
const RPC_URL = '';

// JSON-RPC 요청 본문
const payload = JSON.stringify({
    jsonrpc: "2.0",
    method: "eth_call",
    params: [
        {
            to: "0x4e383fc32176d381Bcac78399495bf0913948206",
            data: "0x",
        },
    ],
});
// // JSON-RPC 요청 본문
// const payload = JSON.stringify({
//     jsonrpc: "2.0",
//     method: "eth_blockNumber",
//     params: [],
//     id: 1
// });

// HTTP 요청 헤더
const headers = { 'Content-Type': 'application/json' };

// 부하 테스트 시나리오
export const options = {
    stages: [
        { duration: '30s', target: 5000 }, // 30초 동안 5000명 증가
        { duration: '30s', target: 5000 }, // 30초 동안 5000명 유지
        // { duration: '20s', target: 50 }, // 20초 동안 50명 유지
        // { duration: '10s', target: 0 },  // 10초 동안 0명으로 감소
    ],
};

export default function () {
    // let res = http.post(RPC_URL, payload, { headers });

    // check(res, {
    //     'is status 200': (r) => r.status === 200,
    //     'is block number received': (r) => JSON.parse(r.body).result !== undefined,
    // });

    // console.log('Block Number:', JSON.parse(res.body).result);

    // sleep(1); // 1초 대기 후 반복 실행
    // 빈 eth_call 요청
    let res = http.post(RPC_URL, payload, { headers });

    // 응답 검증
    check(res, {
        'is status 200': (r) => r.status === 200,
        // 'is eth_call successful': (r) => JSON.parse(r.body).result !== undefined,
    });

    // 결과 출력
    if(res.status !== 200 ) {
        console.log('Response:', res.status);
    }

    sleep(1)
}