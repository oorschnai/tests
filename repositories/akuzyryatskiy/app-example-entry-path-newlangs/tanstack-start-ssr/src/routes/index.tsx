import { createFileRoute } from '@tanstack/react-router'

export const Route = createFileRoute('/')({ component: App })

function App() {
  return (
    <main style={{ maxWidth: 760, margin: '3rem auto', fontFamily: 'system-ui, sans-serif', lineHeight: 1.6 }}>
      <h1>Timeweb Cloud + TanStack Start SSR = ❤️</h1>
      <p>Репозиторий: <strong>app-example-tanstack-start-ssr</strong></p>
      <p>Минимальный пример для проверки сборки и запуска.</p>
      <ul>
        <li>Framework: TanStack Start (React)</li>
        <li>Build output: <code>.output</code></li>
        <li>Start command: <code>node .output/server/index.mjs</code></li>
      </ul>
    </main>
  )
}
