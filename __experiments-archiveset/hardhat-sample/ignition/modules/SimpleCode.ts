import { buildModule } from "@nomicfoundation/hardhat-ignition/modules";

const SimpleCodeModule = buildModule("SimpleCodeModule", (m) => {
  const simple = m.contract("HelloWorld");

  return { simple };
});

export default SimpleCodeModule;
