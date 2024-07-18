const { remote } = require("webdriverio");

const capabilities = {
  "appium:deviceName": "ce10171ab8c35a4004", // adb devices
  platformName: "Android",
  "appium:automationName": "uiautomator2", // appium device list
  "appium:appPackage": "com.sec.android.app.popupcalculator",
  "appium:appActivity": "com.sec.android.app.popupcalculator.Calculator",
};

const wdOpts = {
  hostname: process.env.APPIUM_HOST || "localhost",
  port: parseInt(process.env.APPIUM_PORT, 10) || 4723,
  logLevel: "info",
  capabilities,
};

async function runTest() {
  const driver = await remote(wdOpts);
  await driver.actions([driver.action("pointer").move(420, 1530).down().up()]);
  (await driver.$('#calc_keypad_btn_08')).click();
  const result$ = await driver.$('#calc_edt_formula');
  console.log("-----------------------")
  const val = await result$.getText()
  console.log("The Value is : " + val)
  console.log("-----------------------")

  return driver;
}


runTest().then((driver)=>{
    driver.deleteSession()
}).catch(console.error)
