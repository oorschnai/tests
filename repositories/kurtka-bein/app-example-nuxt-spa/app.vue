<template>
  <div>
    <nav style="padding: 20px; background: #f0f0f0; margin-bottom: 20px;">
      <NuxtLink to="/" style="margin-right: 20px;">Главная</NuxtLink>
      <NuxtLink to="/about" style="margin-right: 20px;">О нас</NuxtLink>
      <NuxtLink to="/products" style="margin-right: 20px;">Товары</NuxtLink>
      <NuxtLink to="/products/123" style="margin-right: 20px;">Товар #123</NuxtLink>
      <NuxtLink to="/contact">Контакты</NuxtLink>
    </nav>
    <div style="padding: 20px;">
      <NuxtPage />
    </div>
  </div>
</template>
