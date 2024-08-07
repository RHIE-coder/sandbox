import { HardhatUserConfig } from 'hardhat/config';
import '@nomicfoundation/hardhat-toolbox';
import * as Dotenv from 'dotenv';
import * as Path from 'path';

Dotenv.config({
    path: Path.join(__dirname, '.env'),
});

console.log(`https://eth-sepolia.g.alchemy.com/v2/${process.env.ALCHEMY_API_KEY!}`)
console.log(`https://sepolia.infura.io/v3/${process.env.INFURA_API_KEY!}`)
console.log(process.env.PRIVATE_KEY)

const config: HardhatUserConfig = {
    solidity: '0.8.20',
    networks: {
        // ganache: {
        //     url: process.env.PROVIDER_URL!,
        //     accounts: [process.env.PRIVATE_KEY!],
        // },
        sepolia: {
            url: `https://eth-sepolia.g.alchemy.com/v2/${process.env.ALCHEMY_API_KEY!}`,
            accounts: [process.env.PRIVATE_KEY!]
        },
    }
    // paths: {
    //     sources: './contracts', // Solidity 소스 코드 경로
    //     tests: './test', // 테스트 파일 경로
    //     cache: './cache', // 컴파일러 캐시 경로
    //     artifacts: './artifacts', // 아티팩트 파일 경로
    // },
};

export default config;