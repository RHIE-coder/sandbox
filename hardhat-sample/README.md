# Sample Hardhat Project

This project demonstrates a basic Hardhat use case. It comes with a sample contract, a test for that contract, and a Hardhat Ignition module that deploys that contract.

Try running some of the following tasks:

```shell
npx hardhat help
npx hardhat test
REPORT_GAS=true npx hardhat test
npx hardhat node
npx hardhat ignition deploy ./ignition/modules/Lock.ts
```

0000000000000000000000000000000000000000000000000000000000000000
bytecode

0x
initial part:  60806040523480156200001157600080fd5b506040518060400160405280600b81526020017f68656c6c6f20776f726c6400000000000000000000000000000000000000000081525060009081620000589190620002d9565b50620003c0565b600081519050919050565b7f4e487b7100000000000000000000000000000000000000000000000000000000600052604160045260246000fd5b7f4e487b7100000000000000000000000000000000000000000000000000000000600052602260045260246000fd5b60006002820490506001821680620000e157607f821691505b602082108103620000f757620000f662000099565b5b50919050565b60008190508160005260206000209050919050565b60006020601f8301049050919050565b600082821b905092915050565b600060088302620001617fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff8262000122565b6200016d868362000122565b95508019841693508086168417925050509392505050565b6000819050919050565b6000819050919050565b6000620001ba620001b4620001ae8462000185565b6200018f565b62000185565b9050919050565b6000819050919050565b620001d68362000199565b620001ee620001e582620001c1565b8484546200012f565b825550505050565b600090565b62000205620001f6565b62000212818484620001cb565b505050565b5b818110156200023a576200022e600082620001fb565b60018101905062000218565b5050565b601f82111562000289576200025381620000fd565b6200025e8462000112565b810160208510156200026e578190505b620002866200027d8562000112565b83018262000217565b50505b505050565b600082821c905092915050565b6000620002ae600019846008026200028e565b1980831691505092915050565b6000620002c983836200029b565b9150826002028217905092915050565b620002e4826200005f565b67ffffffffffffffff8111156200030057620002ff6200006a565b5b6200030c8254620000c8565b620003198282856200023e565b600060209050601f8311600181146200035157600084156200033c578287015190505b620003488582620002bb565b865550620003b8565b601f1984166200036186620000fd565b60005b828110156200038b5784890151825560018201915060208501945060208101905062000364565b86831015620003ab5784890151620003a7601f8916826200029b565b8355505b6001600288020188555050505b505050505050565b6105e180620003d06000396000f3fe

contract part: 608060405234801561001057600080fd5b50600436106100365760003560e01c80632d75552c1461003b5780637d40a30114610057575b600080fd5b6100556004803603810190610050919061018c565b610075565b005b61005f61008b565b60405161006c9190610269565b60405180910390f35b8181600091826100869291906104db565b505050565b60606000805461009a906102f4565b80601f01602080910402602001604051908101604052809291908181526020018280546100c6906102f4565b80156101135780601f106100e857610100808354040283529160200191610113565b820191906000526020600020905b8154815290600101906020018083116100f657829003601f168201915b5050505050905090565b600080fd5b600080fd5b600080fd5b600080fd5b600080fd5b60008083601f84011261014c5761014b610127565b5b8235905067ffffffffffffffff8111156101695761016861012c565b5b60208301915083600182028301111561018557610184610131565b5b9250929050565b600080602083850312156101a3576101a261011d565b5b600083013567ffffffffffffffff8111156101c1576101c0610122565b5b6101cd85828601610136565b92509250509250929050565b600081519050919050565b600082825260208201905092915050565b60005b838110156102135780820151818401526020810190506101f8565b60008484015250505050565b6000601f19601f8301169050919050565b600061023b826101d9565b61024581856101e4565b93506102558185602086016101f5565b61025e8161021f565b840191505092915050565b600060208201905081810360008301526102838184610230565b905092915050565b600082905092915050565b7f4e487b7100000000000000000000000000000000000000000000000000000000600052604160045260246000fd5b7f4e487b7100000000000000000000000000000000000000000000000000000000600052602260045260246000fd5b6000600282049050600182168061030c57607f821691505b60208210810361031f5761031e6102c5565b5b50919050565b60008190508160005260206000209050919050565b60006020601f8301049050919050565b600082821b905092915050565b6000600883026103877fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff8261034a565b610391868361034a565b95508019841693508086168417925050509392505050565b6000819050919050565b6000819050919050565b60006103d86103d36103ce846103a9565b6103b3565b6103a9565b9050919050565b6000819050919050565b6103f2836103bd565b6104066103fe826103df565b848454610357565b825550505050565b600090565b61041b61040e565b6104268184846103e9565b505050565b5b8181101561044a5761043f600082610413565b60018101905061042c565b5050565b601f82111561048f5761046081610325565b6104698461033a565b81016020851015610478578190505b61048c6104848561033a565b83018261042b565b50505b505050565b600082821c905092915050565b60006104b260001984600802610494565b1980831691505092915050565b60006104cb83836104a1565b9150826002028217905092915050565b6104e5838361028b565b67ffffffffffffffff8111156104fe576104fd610296565b5b61050882546102f4565b61051382828561044e565b6000601f8311600181146105425760008415610530578287013590505b61053a85826104bf565b8655506105a2565b601f19841661055086610325565b60005b8281101561057857848901358255600182019150602085019450602081019050610553565b868310156105955784890135610591601f8916826104a1565b8355505b6001600288020188555050505b5050505050505056fea264697066735822122041d3be5bcff112e1c1e5ce5afabffc34c37e38adae693869cdc75f29315627c364736f6c63430008140033

deployedBytecode

0x
contract part: 608060405234801561001057600080fd5b50600436106100365760003560e01c80632d75552c1461003b5780637d40a30114610057575b600080fd5b6100556004803603810190610050919061018c565b610075565b005b61005f61008b565b60405161006c9190610269565b60405180910390f35b8181600091826100869291906104db565b505050565b60606000805461009a906102f4565b80601f01602080910402602001604051908101604052809291908181526020018280546100c6906102f4565b80156101135780601f106100e857610100808354040283529160200191610113565b820191906000526020600020905b8154815290600101906020018083116100f657829003601f168201915b5050505050905090565b600080fd5b600080fd5b600080fd5b600080fd5b600080fd5b60008083601f84011261014c5761014b610127565b5b8235905067ffffffffffffffff8111156101695761016861012c565b5b60208301915083600182028301111561018557610184610131565b5b9250929050565b600080602083850312156101a3576101a261011d565b5b600083013567ffffffffffffffff8111156101c1576101c0610122565b5b6101cd85828601610136565b92509250509250929050565b600081519050919050565b600082825260208201905092915050565b60005b838110156102135780820151818401526020810190506101f8565b60008484015250505050565b6000601f19601f8301169050919050565b600061023b826101d9565b61024581856101e4565b93506102558185602086016101f5565b61025e8161021f565b840191505092915050565b600060208201905081810360008301526102838184610230565b905092915050565b600082905092915050565b7f4e487b7100000000000000000000000000000000000000000000000000000000600052604160045260246000fd5b7f4e487b7100000000000000000000000000000000000000000000000000000000600052602260045260246000fd5b6000600282049050600182168061030c57607f821691505b60208210810361031f5761031e6102c5565b5b50919050565b60008190508160005260206000209050919050565b60006020601f8301049050919050565b600082821b905092915050565b6000600883026103877fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff8261034a565b610391868361034a565b95508019841693508086168417925050509392505050565b6000819050919050565b6000819050919050565b60006103d86103d36103ce846103a9565b6103b3565b6103a9565b9050919050565b6000819050919050565b6103f2836103bd565b6104066103fe826103df565b848454610357565b825550505050565b600090565b61041b61040e565b6104268184846103e9565b505050565b5b8181101561044a5761043f600082610413565b60018101905061042c565b5050565b601f82111561048f5761046081610325565b6104698461033a565b81016020851015610478578190505b61048c6104848561033a565b83018261042b565b50505b505050565b600082821c905092915050565b60006104b260001984600802610494565b1980831691505092915050565b60006104cb83836104a1565b9150826002028217905092915050565b6104e5838361028b565b67ffffffffffffffff8111156104fe576104fd610296565b5b61050882546102f4565b61051382828561044e565b6000601f8311600181146105425760008415610530578287013590505b61053a85826104bf565b8655506105a2565b601f19841661055086610325565b60005b8281101561057857848901358255600182019150602085019450602081019050610553565b868310156105955784890135610591601f8916826104a1565b8355505b6001600288020188555050505b5050505050505056fea264697066735822122041d3be5bcff112e1c1e5ce5afabffc34c37e38adae693869cdc75f29315627c364736f6c63430008140033


리믹스 배포
0x82ee1533c9a0e254a284f9e0d55603cbcfc0bcc3