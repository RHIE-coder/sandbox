// @ts-check
const { test } = require('@playwright/test');

// test.describe.configure({ mode: 'serial' }); // on-off here

test.beforeAll(async ({ page }) => {
  const timeout = 2000;
  page.setDefaultNavigationTimeout(timeout);
  page.setDefaultTimeout(timeout);
});

// test.describe('section 1', ()=>{
//   test('runs first',async ({ page }) => {
//     await page.goto('https://playwright.dev/');
//   });
// })

// test.describe('section 2', ()=>{
// test('runs second', async ({ page }) => {
//   await page.goto('https://playwright.dev/');
//   await page.getByText('Get Started').click();
// });

// test('error will be occured', async ({ page }) => {
//   await page.goto('https://playwright.dev/');
//   await page.getByText('Get Started').click();
//   await page.getByText('not exist text to make an error').click();
// })

// test('runs third', async ({ page }) => {
//   await page.goto('https://playwright.dev/');
//   await page.getByText('Get Started').click();
//   await page.getByRole('link', { name: 'Retries' }).click();
// });
// })

// test.describe('section 3', ()=>{
// test('runs fourth',async ({ page }) => {
//   await page.goto('https://playwright.dev/');
//   await page.getByText('Get Started').click();
//   await page.getByRole('link', { name: 'Retries' }).click();
//   await page.getByText('Running 3 tests using 1 worker ✓ example.spec.ts:4:2 › first passes (438ms) x').click();
// })
// })

test.describe('section', ()=>{
  test('runs first',async ({ page }) => {
    await page.goto('https://playwright.dev/');
  });
test('runs second', async ({ page }) => {
  await page.goto('https://playwright.dev/');
  await page.getByText('Get Started').click();
});

test('error will be occured', async ({ page }) => {
  await page.goto('https://playwright.dev/');
  await page.getByText('Get Started').click();
  await page.getByText('not exist text to make an error').click();
})

test('runs third', async ({ page }) => {
  await page.goto('https://playwright.dev/');
  await page.getByText('Get Started').click();
  await page.getByRole('link', { name: 'Retries' }).click();
});
test('runs fourth',async ({ page }) => {
  await page.goto('https://playwright.dev/');
  await page.getByText('Get Started').click();
  await page.getByRole('link', { name: 'Retries' }).click();
  await page.getByText('Running 3 tests using 1 worker ✓ example.spec.ts:4:2 › first passes (438ms) x').click();
})
})