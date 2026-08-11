<template>
  <div>
    <h1>Товар #{{ $route.params.id }}</h1>
    <p>Это динамическая страница товара с параметром ID.</p>
    <p>URL: <code>/products/{{ $route.params.id }}</code></p>
    <p>Текущий путь: <code>{{ $route.path }}</code></p>
    <p>ID товара: <strong>{{ $route.params.id }}</strong></p>
    <br>
    <p>
      <NuxtLink to="/products">← Вернуться к каталогу</NuxtLink>
    </p>
  </div>
</template>
