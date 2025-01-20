import { keccak256 } from "@ethersproject/keccak256";

function toChecksummedAddress(address:string) {
    // Remove the prefix and convert to lower case
    const addressValue = address.slice(2).toLowerCase();
    // Hash the obtained value and remove the prefix
    const hash = keccak256(Buffer.from(addressValue)).toString().slice(2);
    
    let checksumAddress = '0x';
    
    // Loop through all the characters in the address value 
    for (let i = 0; i < addressValue.length; i++) {
        // Capitalize if not a digit and the matching hash hex digit
        // is greater or equal to 8
        if (!/^\d+$/.test(addressValue[i]) && parseInt(hash[i], 16) >= 8) {
            checksumAddress += addressValue[i].toUpperCase();
        } else {
            checksumAddress += addressValue[i];
        }
    }

    return checksumAddress;
}


(async()=>{
console.log(toChecksummedAddress("0x806b6F491875646998fc741f06a5E9EEfC493Cfc"))
console.log(toChecksummedAddress("0x806b6F491875646998fc741f06a5E9EEfC493Cfc"))
console.log(toChecksummedAddress("0xdE5228e40cBb87667169025d78E2b0ae6570A470"))
console.log(toChecksummedAddress("0xb493A10A405d47AbBE9A2875DF6230a5e8636F13"))
console.log(toChecksummedAddress("0x548B83D15dDA96Bb37380B4d80a8d036aB3e9e4D"))
console.log(toChecksummedAddress("0x35729624e1a8e5cFd3ED7587391b404baDDbFdC6"))
console.log(toChecksummedAddress("0xb0d0813c324AF66a0AfF100d76e6e666Ea5a3107"))
console.log(toChecksummedAddress("0x1A0679fcF47B1CD392000fa90BdB3202B2F2F2AB"))
console.log(toChecksummedAddress("0xaA575f7606d059aa12155f1840F02B3ab3EFD5b5"))
console.log(toChecksummedAddress("0xf83Be0009052ad693107D0b21B50A401Ed8c825F"))
console.log(toChecksummedAddress("0x8d8550D96267EB19764871eAE76810341029E906"))
console.log(toChecksummedAddress("0x5E65BB99991B32f62a17F9ebE69ec50E6072bEc5"))
console.log(toChecksummedAddress("0xa4e36E62cd524Ff8128c6Faf694B8dF9D0265171"))
console.log(toChecksummedAddress("0xF3b6cbE9B60f415dBCB1f8330FCf4B973EEa3C13"))
console.log(toChecksummedAddress("0xd4ACcA18d45008543b0d26BDfF38D0f93987b52e"))
console.log(toChecksummedAddress("0x1257d6EcA5F0AA2a8Afb1c4C6abd4d609CdBd3a0"))
console.log(toChecksummedAddress("0x97Bfd54367F711c6a3F71aBAb50E29209CC6F9e0"))
console.log(toChecksummedAddress("0xbA5167dE64A1627356df45F0EcB16d3c5Ec3AD38"))
console.log(toChecksummedAddress("0x6bfFC3c5F70b36b9048249f9B97A86163F8cc68f"))
console.log(toChecksummedAddress("0xcDFE4F3D2C3dca70F8E2a7Ac71940FA588F46E31"))
console.log(toChecksummedAddress("0xbad8AE13d5104ACF3064E6A9c22BaeFA273f7204"))
console.log(toChecksummedAddress("0x00C5522686097fa29018870c67eaD04294eAee5e"))
console.log(toChecksummedAddress("0x58B55FF134C683B996b59C30D64cB1faA44Be054"))
console.log(toChecksummedAddress("0x818A076346f8AB86AE1a961b2C48B289Cc01893a"))
console.log(toChecksummedAddress("0xC6f0FD0Ba272B8c1551b4015Fe3fdC0425b42945"))
console.log(toChecksummedAddress("0xEa9CC838345734132E893dEa14E40a90D6DA6CCf"))
console.log(toChecksummedAddress("0xA2D613E1c20dcb9490eC160E2964634BEB188b35"))
console.log(toChecksummedAddress("0xeDf021BfC70A47Ba8d89E5817fFBB3AF302C317C"))
console.log(toChecksummedAddress("0x4770C06aE52c81Af8A9a54e3ad4231Eb1731F314"))
console.log(toChecksummedAddress("0x8c8452CF0a7E527AdD98222aE78ED4E192D009C8"))
console.log(toChecksummedAddress("0xD93fac71437dcEC5844F313dFBC0649247E9946D"))
console.log(toChecksummedAddress("0x60D3d86e17F6BE83D7818b29407e400ada6100C7"))
console.log(toChecksummedAddress("0x0586490F9bF97d821b0e29b742E30e7eDE040ad2"))
console.log(toChecksummedAddress("0x5b4c52B0412681964B9eb23426935bDa063f45D0"))
console.log(toChecksummedAddress("0x1409f2e475b8c422555e27f2f9cb83C2c3B16d80"))
console.log(toChecksummedAddress("0xBF5b4677d83544f19E191C7E0C7544Bb5D696025"))
console.log(toChecksummedAddress("0x902D086D9e31Ac7bcE548C6b00515111370e6484"))
console.log(toChecksummedAddress("0xaD9a4bE654dde2c93985536adD73E3bA05f09700"))
console.log(toChecksummedAddress("0xFAa742D213904ae3a0933192Af59A8E49a1923Ff"))
console.log(toChecksummedAddress("0xe3570b2e8dC8873Ee30460EF11cDC78A810d59fd"))
console.log(toChecksummedAddress("0x2f0FFa7E40a13f1cf90d5e68F1b87F806f4333Ff"))
console.log(toChecksummedAddress("0x342C680AF9647784E37f75B0fDb6E6CbE7dF216E"))
console.log(toChecksummedAddress("0x2E4d259c218D993F002c8Afeb882bd14dA03A150"))
console.log(toChecksummedAddress("0xe7a6D5dadBcCd14605DB52Cde597aeb82Ef183C6"))
console.log(toChecksummedAddress("0x2e1A0a727985D4D8c988e207863292c8F8163a1D"))
console.log(toChecksummedAddress("0x6AFCcB3c20D38d15BA17d409F3913410E8a416fb"))
console.log(toChecksummedAddress("0x183391a5c2c9B2CbB2b681d996A97008cB7E888C"))
console.log(toChecksummedAddress("0xD7f2EC6B9B3cB24C46C4335907b96E6bCf202A7A"))
console.log(toChecksummedAddress("0x94e4EE21f1cd2D5baB26b2cceB8d7426bc27510F"))
console.log(toChecksummedAddress("0xB1C9c0Ea0F8033879832517d890483d589736c86"))
console.log(toChecksummedAddress("0x12A975740eF55e6e45bf01b67ca915777148D5c6"))

})()