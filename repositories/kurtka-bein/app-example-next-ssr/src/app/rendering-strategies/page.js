// Страница с примерами разных стратегий рендеринга

// SSR - рендеринг при каждом запросе
async function getSSRData() {
  try {
    const res = await fetch('https://api.github.com/repos/facebook/react', {
      cache: 'no-store', // Force SSR
      headers: { 'User-Agent': 'Next.js SSR Example' }
    });
    if (!res.ok) return { name: 'react', stargazers_count: 220000, updated_at: new Date().toISOString(), _isMock: true };
    return res.json();
  } catch {
    return { name: 'react', stargazers_count: 220000, updated_at: new Date().toISOString(), _isMock: true };
  }
}

// SSG/ISR - рендеринг с кешированием и ревалидацией каждые 60 секунд
async function getISRData() {
  try {
    const res = await fetch('https://api.github.com/repos/nodejs/node', {
      next: { revalidate: 60 }, // ISR - ревалидация каждые 60 секунд
      headers: { 'User-Agent': 'Next.js SSR Example' }
    });
    if (!res.ok) return { name: 'node', stargazers_count: 100000, updated_at: new Date().toISOString(), _isMock: true };
    return res.json();
  } catch {
    return { name: 'node', stargazers_count: 100000, updated_at: new Date().toISOString(), _isMock: true };
  }
}

// SSG - статическая генерация с кешированием
async function getSSGData() {
  try {
    const res = await fetch('https://api.github.com/repos/microsoft/typescript', {
      cache: 'force-cache', // Static generation
      headers: { 'User-Agent': 'Next.js SSR Example' }
    });
    if (!res.ok) return { name: 'typescript', stargazers_count: 95000, updated_at: new Date().toISOString(), _isMock: true };
    return res.json();
  } catch {
    return { name: 'typescript', stargazers_count: 95000, updated_at: new Date().toISOString(), _isMock: true };
  }
}

export const metadata = {
  title: 'Стратегии рендеринга Next.js',
  description: 'Примеры SSR, SSG и ISR',
};

export default async function RenderingStrategies() {
  const [ssrData, isrData, ssgData] = await Promise.all([
    getSSRData(),
    getISRData(),
    getSSGData(),
  ]);

  const renderTime = new Date().toLocaleString('ru-RU');

  return (
    <main style={{ padding: '2rem', maxWidth: '1000px', margin: '0 auto' }}>
      <h1>Стратегии рендеринга в Next.js</h1>

      <div style={{ background: '#f0f0f0', padding: '1rem', borderRadius: '8px', marginBottom: '2rem' }}>
        <p><strong>Время рендера страницы:</strong> {renderTime}</p>
        <p style={{ fontSize: '0.9rem', color: '#666', margin: '0.5rem 0 0 0' }}>
          Обновите страницу несколько раз и обратите внимание на разницу в данных
        </p>
      </div>

      {(ssrData._isMock || isrData._isMock || ssgData._isMock) && (
        <div style={{ background: '#fff3cd', border: '1px solid #ffc107', padding: '1rem', borderRadius: '8px', marginBottom: '2rem' }}>
          <p style={{ margin: 0, color: '#856404' }}>
            ⚠️ Используются демо-данные (GitHub API недоступен)
          </p>
        </div>
      )}

      <div style={{ display: 'grid', gap: '1.5rem', marginBottom: '2rem' }}>
        {/* SSR Example */}
        <div style={{ background: '#fff3cd', border: '2px solid #ffc107', padding: '1.5rem', borderRadius: '8px' }}>
          <h2 style={{ marginTop: 0, color: '#856404' }}>
            1. SSR (Server-Side Rendering)
          </h2>
          <p><strong>Репозиторий:</strong> {ssrData.name}</p>
          <p><strong>⭐ Stars:</strong> {ssrData.stargazers_count.toLocaleString()}</p>
          <p><strong>Обновлен:</strong> {new Date(ssrData.updated_at).toLocaleString('ru-RU')}</p>

          <div style={{ background: 'white', padding: '1rem', borderRadius: '4px', marginTop: '1rem' }}>
            <strong>Как работает:</strong>
            <ul style={{ margin: '0.5rem 0 0 0', paddingLeft: '1.5rem' }}>
              <li><code>cache: &apos;no-store&apos;</code></li>
              <li>Рендеринг при каждом запросе</li>
              <li>Всегда актуальные данные</li>
              <li>Больше нагрузка на сервер</li>
            </ul>
          </div>
        </div>

        {/* ISR Example */}
        <div style={{ background: '#d1ecf1', border: '2px solid #17a2b8', padding: '1.5rem', borderRadius: '8px' }}>
          <h2 style={{ marginTop: 0, color: '#0c5460' }}>
            2. ISR (Incremental Static Regeneration)
          </h2>
          <p><strong>Репозиторий:</strong> {isrData.name}</p>
          <p><strong>⭐ Stars:</strong> {isrData.stargazers_count.toLocaleString()}</p>
          <p><strong>Обновлен:</strong> {new Date(isrData.updated_at).toLocaleString('ru-RU')}</p>

          <div style={{ background: 'white', padding: '1rem', borderRadius: '4px', marginTop: '1rem' }}>
            <strong>Как работает:</strong>
            <ul style={{ margin: '0.5rem 0 0 0', paddingLeft: '1.5rem' }}>
              <li><code>next: &#123; revalidate: 60 &#125;</code></li>
              <li>Кеширование на 60 секунд</li>
              <li>Ревалидация в фоне после истечения времени</li>
              <li>Баланс между скоростью и актуальностью</li>
            </ul>
          </div>
        </div>

        {/* SSG Example */}
        <div style={{ background: '#d4edda', border: '2px solid #28a745', padding: '1.5rem', borderRadius: '8px' }}>
          <h2 style={{ marginTop: 0, color: '#155724' }}>
            3. SSG (Static Site Generation)
          </h2>
          <p><strong>Репозиторий:</strong> {ssgData.name}</p>
          <p><strong>⭐ Stars:</strong> {ssgData.stargazers_count.toLocaleString()}</p>
          <p><strong>Обновлен:</strong> {new Date(ssgData.updated_at).toLocaleString('ru-RU')}</p>

          <div style={{ background: 'white', padding: '1rem', borderRadius: '4px', marginTop: '1rem' }}>
            <strong>Как работает:</strong>
            <ul style={{ margin: '0.5rem 0 0 0', paddingLeft: '1.5rem' }}>
              <li><code>cache: &apos;force-cache&apos;</code></li>
              <li>Кеширование при билде</li>
              <li>Максимальная производительность</li>
              <li>Требует пересборки для обновления</li>
            </ul>
          </div>
        </div>
      </div>

      <div style={{ background: '#e7f3ff', padding: '1.5rem', borderRadius: '8px' }}>
        <h3>Сравнение стратегий:</h3>
        <table style={{ width: '100%', borderCollapse: 'collapse' }}>
          <thead>
            <tr style={{ background: '#0070f3', color: 'white' }}>
              <th style={{ padding: '0.75rem', textAlign: 'left' }}>Стратегия</th>
              <th style={{ padding: '0.75rem', textAlign: 'left' }}>Когда использовать</th>
              <th style={{ padding: '0.75rem', textAlign: 'left' }}>Производительность</th>
            </tr>
          </thead>
          <tbody>
            <tr style={{ background: 'white' }}>
              <td style={{ padding: '0.75rem', borderBottom: '1px solid #ddd' }}><strong>SSR</strong></td>
              <td style={{ padding: '0.75rem', borderBottom: '1px solid #ddd' }}>Персонализация, аутентификация</td>
              <td style={{ padding: '0.75rem', borderBottom: '1px solid #ddd' }}>Средняя</td>
            </tr>
            <tr style={{ background: '#f8f9fa' }}>
              <td style={{ padding: '0.75rem', borderBottom: '1px solid #ddd' }}><strong>ISR</strong></td>
              <td style={{ padding: '0.75rem', borderBottom: '1px solid #ddd' }}>Контент с периодическими обновлениями</td>
              <td style={{ padding: '0.75rem', borderBottom: '1px solid #ddd' }}>Высокая</td>
            </tr>
            <tr style={{ background: 'white' }}>
              <td style={{ padding: '0.75rem' }}><strong>SSG</strong></td>
              <td style={{ padding: '0.75rem' }}>Статический контент, маркетинговые страницы</td>
              <td style={{ padding: '0.75rem' }}>Максимальная</td>
            </tr>
          </tbody>
        </table>
      </div>

      <p style={{ marginTop: '2rem' }}>
        <a href="/" style={{ color: '#0070f3' }}>← Назад на главную</a>
      </p>
    </main>
  );
}
