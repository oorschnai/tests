export default defineEventHandler((event) => {
  return {
    message: 'Привет из SSR API!',
    timestamp: new Date().toISOString(),
    serverRendered: true
  }
})
