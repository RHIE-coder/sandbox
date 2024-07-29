// @ts-check
const { test, expect } = require('@playwright/test');

test('playwright test', async ({ page }) => {
  await page.goto('https://playwright.dev/');
  await page.getByRole('link', { name: 'Docs' }).click();
  await page.getByRole('article').getByRole('link', { name: 'What\'s Installed', exact: true }).click();
  await expect(page.locator('#whats-installed')).toContainText('What\'s Installed');
  await page.getByRole('link', { name: 'Test use options' }).click();
  await expect(page.locator('#emulation-options')).toContainText('Emulation Options');
});