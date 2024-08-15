import { defineConfig } from "vite";
import react from "@vitejs/plugin-react";

// https://vitejs.dev/config/
export default defineConfig({
  plugins: [react()],
  server: {
    host: "0.0.0.0", // Listen on all addresses, necessary for Docker
    port: 5173, // Make sure this matches the port you expose in Docker
    strictPort: true, // Fail if the port is already in use
  },
});
