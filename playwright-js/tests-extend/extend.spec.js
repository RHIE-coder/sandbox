const base = require('@playwright/test');
const { TodoPage } = require('./todo-page');

// Extend basic test by providing a "todoPage" fixture.
const test = base.test.extend({
  todoPage: async ({ page }, use) => {
    const todoPage = new TodoPage(page);
    await todoPage.goto();
    await todoPage.addToDo('item1');
    await todoPage.addToDo('item2');
    await use("todoPage");
    await todoPage.removeAll();
  },
}, { scope: 'test' });

test('should add an item', async ({ todoPage }) => {
  await todoPage.addToDo('my item');
  // ...
});

test('should remove an item', async ({ todoPage }) => {
  await todoPage.remove('item1');
  // ...
});