# Руководство по SSR в Next.js

## Что добавлено

SSR (Server-Side Rendering) теперь полностью настроен и работает в этом проекте.

### Созданные примеры:

1. **`/ssr-example`** - Базовый пример SSR
   - Загрузка данных на сервере при каждом запросе
   - `cache: 'no-store'` для отключения кеширования
   - Время рендера обновляется при каждом обновлении страницы

2. **`/posts/[id]`** - Динамический роут с SSR
   - Параметризованный роут
   - Генерация метаданных на сервере (`generateMetadata`)
   - Загрузка данных на основе URL параметров

3. **`/rendering-strategies`** - Сравнение стратегий рендеринга
   - **SSR**: `cache: 'no-store'` - рендеринг при каждом запросе
   - **ISR**: `next: { revalidate: 60 }` - инкрементальная регенерация
   - **SSG**: `cache: 'force-cache'` - статическая генерация

## Ключевые изменения

### 1. next.config.mjs
```javascript
const nextConfig = {
    // Убрали 'output: export' для включения SSR
    // SSR работает по умолчанию в Next.js App Router
};
```

### 2. Стратегии fetch в App Router

```javascript
// SSR - при каждом запросе
fetch(url, { cache: 'no-store' })

// ISR - с ревалидацией
fetch(url, { next: { revalidate: 60 } })

// SSG - статическая генерация
fetch(url, { cache: 'force-cache' })
```

## Как использовать SSR

### Async Server Components

```javascript
// app/my-page/page.js
async function getData() {
  const res = await fetch('https://api.example.com/data', {
    cache: 'no-store' // SSR
  });
  return res.json();
}

export default async function Page() {
  const data = await getData();
  return <div>{data.title}</div>;
}
```

### Генерация метаданных

```javascript
export async function generateMetadata({ params }) {
  const data = await fetchData(params.id);

  return {
    title: data.title,
    description: data.description,
  };
}
```

### Динамические роуты

```javascript
// app/posts/[id]/page.js
export default async function Post({ params }) {
  const post = await getPost(params.id);
  return <article>{post.content}</article>;
}
```

## Запуск проекта

```bash
# Режим разработки (с HMR)
npm run dev

# Production сборка
npm run build
npm start
```

## Когда использовать каждую стратегию

| Стратегия | Использование | Примеры |
|-----------|---------------|---------|
| **SSR** | Персонализированный контент, часто меняющиеся данные | Дашборды, профили пользователей |
| **ISR** | Контент с периодическими обновлениями | Блог, новости, каталог продуктов |
| **SSG** | Статический контент | Лендинги, документация, about страницы |

## Производительность

- **SSR**: Каждый запрос обрабатывается сервером
- **ISR**: Первый запрос кеширован, фоновая ревалидация
- **SSG**: Максимальная производительность, генерация при сборке

## Проверка SSR

1. Откройте `/ssr-example`
2. Обновите страницу несколько раз
3. Время рендера будет меняться - это подтверждает SSR

## Дополнительные возможности

### Streaming SSR
```javascript
import { Suspense } from 'react';

export default function Page() {
  return (
    <Suspense fallback={<Loading />}>
      <AsyncComponent />
    </Suspense>
  );
}
```

### Server Actions (для форм)
```javascript
// app/actions.js
'use server'

export async function submitForm(formData) {
  // Обработка на сервере
}
```

## Документация Next.js

- [Data Fetching](https://nextjs.org/docs/app/building-your-application/data-fetching)
- [Rendering](https://nextjs.org/docs/app/building-your-application/rendering)
- [Caching](https://nextjs.org/docs/app/building-your-application/caching)
