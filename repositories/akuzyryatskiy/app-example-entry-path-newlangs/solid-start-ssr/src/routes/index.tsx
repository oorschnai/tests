import "../app.css";

export default function Home() {
  return (
    <main style={{ "max-width": "720px", margin: "3rem auto", "font-family": "system-ui, sans-serif", "line-height": 1.6 }}>
      <h1>Timeweb Cloud + SolidStart SSR = ❤️</h1>
      <p>
        Репозиторий: <strong>app-example-solid-start-ssr</strong>
      </p>
      <p>Пример SolidStart-проекта для ssr-режима.</p>
      <ul>
        <li>Фреймворк: SolidStart</li>
        <li>Сборка: <code>npm run build</code></li>
        <li>Серверный запуск: <code>node .output/server/index.mjs</code></li>
      </ul>
    </main>
  );
}
