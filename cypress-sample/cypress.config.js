const { defineConfig } = require("cypress");

module.exports = defineConfig({
  e2e: {
    // baseUrl:"http://localhost:3000",
    setupNodeEvents(on, config) {
      // implement node event listeners here
    },
  },
  // port: 9999,
  video: true,
  // projectId: "<input if you use cypress cloud>",
  //  -->  npx cypress run --record --key <UUID>
  experimentalWebKitSupport: true,
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
