<script setup lang="ts">
// useFetch автоматически выполнит запрос на сервере (SSR) и на клиенте
const { data, pending, error } = await useFetch('/api/hello')

// Определяем, где происходит рендеринг
const renderLocation = process.server ? 'Сервер' : 'Клиент'
</script>

<template>
  <div style="font-family: Arial, sans-serif; max-width: 800px; margin: 50px auto; padding: 20px;">
    <h1>🚀 Nuxt 3 с поддержкой SSR</h1>

    <div style="background: #f0f9ff; border-left: 4px solid #0ea5e9; padding: 20px; margin: 20px 0;">
      <h2>✅ SSR включен</h2>
      <p>Этот компонент рендерится на: <strong>{{ renderLocation }}</strong></p>
    </div>

    <div style="background: #f0fdf4; border-left: 4px solid #10b981; padding: 20px; margin: 20px 0;">
      <h3>Данные от API (SSR):</h3>
      <div v-if="pending">
        Загрузка...
      </div>
      <div v-else-if="error">
        Ошибка: {{ error }}
      </div>
      <div v-else-if="data">
        <ul style="list-style: none; padding: 0;">
          <li><strong>Сообщение:</strong> {{ data.message }}</li>
          <li><strong>Время:</strong> {{ data.timestamp }}</li>
          <li><strong>Server Rendered:</strong> {{ data.serverRendered ? 'Да' : 'Нет' }}</li>
        </ul>
      </div>
    </div>

    <div style="background: #fef3c7; border-left: 4px solid #f59e0b; padding: 20px; margin: 20px 0;">
      <h3>Как это работает:</h3>
      <ul>
        <li><code>ssr: true</code> в nuxt.config.ts включает серверный рендеринг</li>
        <li><code>useFetch</code> автоматически выполняет запросы на сервере</li>
        <li>HTML генерируется на сервере и отправляется клиенту</li>
        <li>Улучшается SEO и производительность первой загрузки</li>
      </ul>
    </div>

    <div style="margin-top: 30px; padding: 20px; background: #f3f4f6; border-radius: 8px;">
      <h3>Команды для запуска:</h3>
      <pre style="background: #1f2937; color: #f9fafb; padding: 15px; border-radius: 5px; overflow-x: auto;">
# Разработка с SSR
npm run dev

# Сборка для продакшена с SSR
npm run build

# Запуск продакшн версии
npm run preview
      </pre>
    </div>
  </div>
</template>
