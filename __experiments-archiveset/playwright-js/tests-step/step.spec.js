// @ts-check
const { test } = require("@playwright/test");

// test.describe("single browser test", ({ page })=>{ <-- undefined: page 주입 없음
//   test('runs first', async ({ page }) => {
//     await page.goto('https://playwright.dev/');
//   });

//   test('runs second', async ({ page }) => {
//     await page.getByText('Get Started').click();
//   });
// })

test("runs first", async ({ page }) => {
    const timeout = 3000;
    page.setDefaultNavigationTimeout(timeout);
    page.setDefaultTimeout(timeout);
    await page.goto("https://playwright.dev/");

    await test.step("runs second", async () => {
        await page.getByText("Get Started").click();
    });
    await test.step('error will be occured', async () => {
        await page.getByText('not exist text to make an error').click();
    })
    await test.step("runs third", async () => {
        await page.getByRole("link", { name: "Retries" }).click();
    });

    await test.step("runs fourth", async () => {
        await page
            .getByText(
            "Running 3 tests using 1 worker ✓ example.spec.ts:4:2 › first passes (438ms) x"
            )
            .click();
    });
});



