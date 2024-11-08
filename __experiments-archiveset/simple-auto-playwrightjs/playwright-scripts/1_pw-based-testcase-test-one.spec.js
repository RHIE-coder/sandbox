import { test, expect } from '@playwright/test';

test('Playwright TODO MVC', async ({page})=>{
  const timeout = 5000;
  page.setDefaultNavigationTimeout(timeout);
  page.setDefaultTimeout(timeout);
  await page.goto("https://demo.playwright.dev/todomvc")

  await expect(page.getByRole("heading", {name: "todos"})).toBeVisible()
  await expect(page.getByPlaceholder("What needs to be done?")).toBeVisible()
  await page.getByPlaceholder("What needs to be done?").fill("Rhie1234 민!@#")
  await page.getByPlaceholder("What needs to be done?").press("Enter")
  await page.getByLabel("Toggle Todo").click()
  await page.getByTestId("todo-title").hover()
  await page.getByLabel("Delete").click()
})
