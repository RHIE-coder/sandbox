const { chromium } = require('playwright');
const fs = require('fs');
const { TodoPage } = require('./todo-page');

(async () => {
  const browser = await chromium.launch();
  const context = await browser.newContext();
  const page = await context.newPage()
  const todoPage = new TodoPage(page);
  await todoPage.goto();
  await todoPage.addToDo('item1');
  await todoPage.addToDo('item2');
  await context.storageState({ path:'storage.json'})
  browser.close();
})();