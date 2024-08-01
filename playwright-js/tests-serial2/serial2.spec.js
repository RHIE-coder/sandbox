// @ts-check
const { test, expect } = require("@playwright/test");
const fs = require("fs");

// test.describe.configure({ mode: "serial" });

/** @type {import('@playwright/test').Page} */
let page;
let errors = [];

test.beforeAll(async ({ browser }) => {
  const timeout = 3000;
  page = await browser.newPage();
  page.setDefaultNavigationTimeout(timeout);
  page.setDefaultTimeout(timeout);
});

test.afterAll(async () => {
  console.log(errors)
  await page.close();
});

test("runs first", async () => {
  await page.goto("https://playwright.dev/");
});

test.describe("single browser test", () => {
  test("runs second", async () => {
    await page.getByText("Get Started").click();
  });

  test("error will be occured", async () => {
    try {
      await page.getByText("not exist text to make an error").click();
    } catch (e) {
      const logStream = fs.createWriteStream("test-log.txt", { flags: "a" });
      logStream.write("Starting test...\n");
      errors.push(test.info())
      console.log(test.info())
      // test.info().status = 'failed';
    }
  });

  test("runs third", async () => {
    await page.getByRole("link", { name: "Retries" }).click();
  });
});

test("runs fourth", async () => {
  await page
    .getByText(
      "Running 3 tests using 1 worker ✓ example.spec.ts:4:2 › first passes (438ms) x"
    )
    .click();
});
