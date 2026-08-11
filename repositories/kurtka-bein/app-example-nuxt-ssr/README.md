![Nuxt Logo](https://st.timeweb.com/cloud-static/apps-logo/nuxt.svg)

# Nuxt с SSR

Пример приложения [Nuxt 3](https://nuxt.com/) с поддержкой **Server-Side Rendering (SSR)**, которое можно развернуть в **Timeweb Cloud Apps** без настройки.

:tada: [Демо](https://timeweb-cloud-app-example-nuxt-79e2.twc1.net)

:rocket: [Создать свой Apps](https://timeweb.cloud/my/apps/create)

:books: [Документация Timeweb Cloud Apps](https://timeweb.cloud/docs/apps)

## 🚀 Особенности

- ✅ **SSR включен** - серверный рендеринг для улучшения SEO и производительности
- 🔄 **API Routes** - встроенные серверные API эндпоинты
- ⚡ **Nitro Server** - современный серверный движок
- 📦 **TypeScript** - полная поддержка типов

## <a name="dev"></a>Локальный запуск проекта

```bash
# установка зависимостей
npm install

# запуск в дев режиме с SSR
npm run dev

# сборка для продакшена с SSR
npm run build

# запуск продакшн версии
npm run preview
```

## 📝 Конфигурация SSR

SSR настроен в `nuxt.config.ts`:

```typescript
export default defineNuxtConfig({
  ssr: true,  // Включен серверный рендеринг
  nitro: {
    preset: 'node-server'  // Preset для Node.js сервера
  }
})
```

## 🛠️ Структура проекта

```
├── app.vue              # Главный компонент с примером SSR
├── server/
│   └── api/
│       └── hello.ts    # API эндпоинт для демонстрации SSR
├── nuxt.config.ts      # Конфигурация SSR
└── package.json        # Скрипты для сборки с SSR
```
