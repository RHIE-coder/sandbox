const {test} = require('@playwright/test');
const { TodoPage } = require('./todo-page');

test.use({ storageState: 'storage.json' });

test('should add an item', async ({ page }) => {
  const todoPage = new TodoPage(page);
  await todoPage.addToDo('my item');
});

test('should remove an item', async ({ page }) => {
  const todoPage = new TodoPage(page);
  await todoPage.remove('item1');
  // ...
});