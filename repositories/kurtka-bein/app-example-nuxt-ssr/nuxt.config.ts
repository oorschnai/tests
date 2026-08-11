// https://nuxt.com/docs/api/configuration/nuxt-config
export default defineNuxtConfig({
  devtools: { enabled: true },

  // Явная настройка SSR
  ssr: true,

  // Настройки рендеринга
  nitro: {
    preset: 'node-server'
  }
})
