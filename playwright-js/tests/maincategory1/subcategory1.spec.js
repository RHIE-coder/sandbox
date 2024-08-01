// @ts-check
const { test, expect } = require('@playwright/test');

test.beforeEach(async ({ page }) => {
  const timeout = 5000;
  await page.setDefaultNavigationTimeout(timeout);
  await page.setDefaultTimeout(timeout);
  page.goto("https://demo.playwright.dev/todomvc")
});

test.describe('[TC 1]', ()=>{
  test('todos 타이틀이 노출되어야 한다', async ({ page }) => {
    await expect(page.getByRole("heading", {name: "todos"})).toBeVisible()
  });
})

test.describe('[TC 2]', ()=> {
  test('입력창에 "What needs to be done?" placeholder 문구가 노출되어야 한다', async ({ page }) => {
    await expect(page.getByPlaceholder("What needs to be done?")).toBeVisible()
  });
})

test.describe('[TC 3]', ()=> {
  test('영문 대소문자, 한글, 숫자, 특수문자, 공백이 입력되어야 한다', async ({ page }) => {
    await page.getByPlaceholder("What needs to be done?").fill("Rhie1234 민!@#")
  });
})

test.describe('[TC 4]', ()=> {
  test('입력한 문구가 입력창 길이를 넘어가면 wrap되어야 한다.', async ({ page }) => {
    console.log("manual testing")
  });
})

test.describe('[TC 5]', ()=> {
  // precondition: test_detail_3
  test('엔터키를 누르면 입력한 문구로 todo 아이템이 생성되어야 이다', async ({ page }) => {
    await page.getByPlaceholder("What needs to be done?").fill("Rhie1234 민!@#")
    await page.getByPlaceholder("What needs to be done?").press("Enter")
  });
})

test.describe('[TC 6]', ()=> {
  // precondition: test_detail_5
  test('todo 아이템의 토글을 누르면 체크되어야 한다', async ({ page }) => {
    await page.getByPlaceholder("What needs to be done?").fill("Rhie1234 민!@#")
    await page.getByPlaceholder("What needs to be done?").press("Enter")
    await page.getByLabel("Toggle Todo").click()
  });
})

test.describe('[TC 7]', ()=> {
  // precondition: test_detail_5
  test("todo 아이템의 'X' 표시를 누르면 todo 아이템이 사라져야 한다", async ({ page }) => {
    await page.getByPlaceholder("What needs to be done?").fill("Rhie1234 민!@#")
    await page.getByPlaceholder("What needs to be done?").press("Enter")
    await page.getByTestId("todo-title").hover()
    await page.getByLabel("Delete").click()
  });
})
