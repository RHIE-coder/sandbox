const { remote } = require("webdriverio");

const capabilities = {
  "appium:udid": "00008120-001C30263E82201E",
  platformName: "iOS",
  "appium:automationName": "XCUITest",
};

const wdOpts = {
  hostname: process.env.APPIUM_HOST || "localhost",
  port: parseInt(process.env.APPIUM_PORT, 10) || 4723,
  logLevel: "info",
  capabilities,
};

async function runTest() {
  const driver = await remote(wdOpts);
//   const elem = await driver.$$('bleepy test');
  const selector = '**/XCUIElementTypeIcon[`name == "bleepy test"`]'
  const elem = await driver.$(`-ios class chain:${selector}`)
  console.log("-----------------")
  console.log(await elem.click())
//   await driver.actions([driver.action("pointer").move(65, 555).down().up()]);
  console.log("-----------------")

  return driver;
}

runTest()
  .then((driver) => {
    driver.deleteSession();
  })
  .catch(console.error);
