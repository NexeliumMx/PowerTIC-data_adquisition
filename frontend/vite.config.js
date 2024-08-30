import { defineConfig } from 'vite'
import react from '@vitejs/plugin-react'

// https://vitejs.dev/config/
export default defineConfig({
  plugins: [react()],
  base: './', // This sets Vite to use relative paths
  build: {
    outDir: 'build' // Set output directory to 'build'
  }
})
