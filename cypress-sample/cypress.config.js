const { defineConfig } = require("cypress");

module.exports = defineConfig({
  e2e: {
    // baseUrl:"http://localhost:3000",
    setupNodeEvents(on, config) {
      // implement node event listeners here
    },
  },

  component: {
    devServer: {
      framework: "react",
      bundler: "vite",
    },
  },

  reporter: "mochawesome",
  reporterOptions: {
    reportDir: 'cypress/reports',
    overwrite: false,
    html: false,
    json: true
  }
});
