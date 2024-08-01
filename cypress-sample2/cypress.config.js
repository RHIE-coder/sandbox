const { defineConfig } = require("cypress");

module.exports = defineConfig({
  e2e: {
    slowTestThreshold: 1000,
    setupNodeEvents(on, config) {
      // implement node event listeners here
    },
  },
});
