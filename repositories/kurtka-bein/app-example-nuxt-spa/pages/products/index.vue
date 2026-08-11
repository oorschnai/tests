<template>
  <div>
    <h1>Каталог товаров</h1>
    <p>Это страница со списком товаров.</p>
    <p>URL: <code>/products</code></p>
    <p>Текущий путь: <code>{{ $route.path }}</code></p>
    <ul>
      <li><NuxtLink to="/products/123">Товар #123</NuxtLink></li>
      <li><NuxtLink to="/products/456">Товар #456</NuxtLink></li>
      <li><NuxtLink to="/products/789">Товар #789</NuxtLink></li>
    </ul>
  </div>
</template>
