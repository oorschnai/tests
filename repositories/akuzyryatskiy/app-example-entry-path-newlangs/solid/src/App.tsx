import type { Component } from 'solid-js';

const App: Component = () => {
  return (
    <main style={{ 'max-width': '720px', margin: '3rem auto', 'font-family': 'system-ui, sans-serif', 'line-height': 1.6 }}>
      <h1>Timeweb Cloud + Solid = ❤️</h1>
      <p>Репозиторий: <strong>app-example-solid</strong></p>
      <p>Минимальный Solid SPA для проверки frontend-режима.</p>
      <ul>
        <li>Фреймворк: Solid</li>
        <li>Сборка: <code>npm run build</code></li>
        <li>Выходная папка: <code>dist</code></li>
      </ul>
    </main>
  );
};

export default App;
