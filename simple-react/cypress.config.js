import { defineConfig } from "cypress";

export default defineConfig({
  e2e: {
    // baseUrl: "http://localhost:8080",
    setupNodeEvents(on, config) {},
  },
  port: 9999,
  video: true,
  // projectId: "<input if you use cypress cloud>",
  // CLI: npx cypress run --record --key <UUID>
});
