// Этот компонент рендерится на сервере при каждом запросе (SSR)

async function getData() {
  try {
    // Отключаем кеширование для SSR при каждом запросе
    const res = await fetch('https://api.github.com/repos/vercel/next.js', {
      cache: 'no-store', // SSR - рендерим при каждом запросе
      headers: {
        'User-Agent': 'Next.js SSR Example'
      }
    });

    if (!res.ok) {
      console.error('GitHub API error:', res.status, res.statusText);
      // Возвращаем моковые данные если API недоступен
      return {
        name: 'next.js',
        description: 'The React Framework',
        stargazers_count: 120000,
        forks_count: 25000,
        watchers_count: 120000,
        updated_at: new Date().toISOString(),
        _isMock: true
      };
    }

    return res.json();
  } catch (error) {
    console.error('Fetch error:', error);
    // Fallback данные
    return {
      name: 'next.js',
      description: 'The React Framework',
      stargazers_count: 120000,
      forks_count: 25000,
      watchers_count: 120000,
      updated_at: new Date().toISOString(),
      _isMock: true
    };
  }
}

export const metadata = {
  title: 'SSR Example',
  description: 'Server-side rendered page with dynamic data',
};

export default async function SSRExample() {
  const data = await getData();
  const currentTime = new Date().toLocaleString('ru-RU');

  return (
    <main style={{ padding: '2rem', maxWidth: '800px', margin: '0 auto' }}>
      <h1>Пример Server-Side Rendering (SSR)</h1>

      <div style={{ background: '#f0f0f0', padding: '1rem', borderRadius: '8px', marginBottom: '1rem' }}>
        <p><strong>Время рендера на сервере:</strong> {currentTime}</p>
        <p style={{ fontSize: '0.9rem', color: '#666' }}>
          Это время генерируется на сервере при каждом запросе
        </p>
      </div>

      {data._isMock && (
        <div style={{ background: '#fff3cd', border: '1px solid #ffc107', padding: '1rem', borderRadius: '8px', marginBottom: '1rem' }}>
          <p style={{ margin: 0, color: '#856404' }}>
            ⚠️ Используются демо-данные (GitHub API недоступен)
          </p>
        </div>
      )}

      <h2>Данные из GitHub API (Next.js репозиторий)</h2>
      <div style={{ background: '#fff', border: '1px solid #ddd', padding: '1rem', borderRadius: '8px' }}>
        <p><strong>Название:</strong> {data.name}</p>
        <p><strong>Описание:</strong> {data.description}</p>
        <p><strong>⭐ Stars:</strong> {data.stargazers_count.toLocaleString()}</p>
        <p><strong>🍴 Forks:</strong> {data.forks_count.toLocaleString()}</p>
        <p><strong>👁️ Watchers:</strong> {data.watchers_count.toLocaleString()}</p>
        <p><strong>Последнее обновление:</strong> {new Date(data.updated_at).toLocaleString('ru-RU')}</p>
      </div>

      <div style={{ marginTop: '2rem', padding: '1rem', background: '#e3f2fd', borderRadius: '8px' }}>
        <h3>Как это работает:</h3>
        <ul>
          <li>Компонент является async функцией</li>
          <li>Данные загружаются на сервере перед рендерингом</li>
          <li><code>cache: &apos;no-store&apos;</code> заставляет Next.js рендерить страницу при каждом запросе</li>
          <li>HTML генерируется на сервере с актуальными данными</li>
          <li>Обновите страницу - время изменится (SSR при каждом запросе)</li>
        </ul>
      </div>

      <p style={{ marginTop: '2rem' }}>
        <a href="/" style={{ color: '#0070f3' }}>← Назад на главную</a>
      </p>
    </main>
  );
}
