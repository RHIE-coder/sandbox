import path from "path"
import tailwindcss from "@tailwindcss/vite"
import react from "@vitejs/plugin-react"
import { defineConfig } from "vite"

import dotenv from 'dotenv';
dotenv.config();
 
// https://vite.dev/config/
export default defineConfig({
  plugins: [react(), tailwindcss()],
  resolve: {
    alias: {
      "@": path.resolve(__dirname, "./src"),
    },
  },
  server: {
    allowedHosts: [process.env.OWN_DOMAIN!], 
    host: true, // 👈 이게 핵심!
    // port: 3000, // 원하는 포트 (기본값: 5173)
  },
})