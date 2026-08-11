import type { Route } from './+types/home';

export function meta({}: Route.MetaArgs) {
  return [
    { title: 'Remix SSR Example' },
    { name: 'description', content: 'SSR Remix example for Node runtime' },
  ];
}

export default function Home() {
  return (
    <main style={{ maxWidth: 760, margin: '3rem auto', fontFamily: 'system-ui, sans-serif', lineHeight: 1.6 }}>
      <h1>Timeweb Cloud + Remix SSR = ❤️</h1>
      <p>Репозиторий: <strong>app-example-remix-ssr</strong></p>
      <p>Проект предназначен для ssr-проверки.</p>
      <ul>
        <li>Build output: <code>build/client</code> и <code>build/server</code></li>
        <li>Start command: <code>npm run start</code></li>
      </ul>
    </main>
  );
}
