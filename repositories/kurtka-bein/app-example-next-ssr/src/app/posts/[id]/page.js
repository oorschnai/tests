// Динамический роут с SSR

async function getPost(id) {
  try {
    const res = await fetch(`https://jsonplaceholder.typicode.com/posts/${id}`, {
      cache: 'no-store', // SSR при каждом запросе
      headers: { 'User-Agent': 'Next.js SSR Example' }
    });

    if (!res.ok) {
      return {
        id,
        title: `Пост #${id}`,
        body: 'Это демонстрационный пост для примера SSR в Next.js. Внешний API недоступен, но SSR работает корректно.',
        userId: 1,
        _isMock: true
      };
    }

    return res.json();
  } catch {
    return {
      id,
      title: `Пост #${id}`,
      body: 'Это демонстрационный пост для примера SSR в Next.js. Внешний API недоступен, но SSR работает корректно.',
      userId: 1,
      _isMock: true
    };
  }
}

// Генерация метаданных на сервере
export async function generateMetadata({ params }) {
  const post = await getPost(params.id);

  return {
    title: post.title,
    description: post.body.substring(0, 160),
  };
}

export default async function PostPage({ params }) {
  const post = await getPost(params.id);
  const renderTime = new Date().toLocaleString('ru-RU');

  return (
    <main style={{ padding: '2rem', maxWidth: '800px', margin: '0 auto' }}>
      <h1>Пост #{post.id}</h1>

      <div style={{ background: '#f0f0f0', padding: '1rem', borderRadius: '8px', marginBottom: '1rem' }}>
        <p><strong>Время рендера:</strong> {renderTime}</p>
      </div>

      {post._isMock && (
        <div style={{ background: '#fff3cd', border: '1px solid #ffc107', padding: '1rem', borderRadius: '8px', marginBottom: '1rem' }}>
          <p style={{ margin: 0, color: '#856404' }}>
            ⚠️ Используются демо-данные (внешний API недоступен)
          </p>
        </div>
      )}

      <article style={{ background: '#fff', border: '1px solid #ddd', padding: '1.5rem', borderRadius: '8px' }}>
        <h2 style={{ marginTop: 0 }}>{post.title}</h2>
        <p>{post.body}</p>
        <p style={{ color: '#666', fontSize: '0.9rem' }}>
          User ID: {post.userId}
        </p>
      </article>

      <div style={{ marginTop: '2rem' }}>
        <p>Попробуйте другие посты:</p>
        <div style={{ display: 'flex', gap: '0.5rem', flexWrap: 'wrap' }}>
          {[1, 2, 3, 4, 5].map(id => (
            <a
              key={id}
              href={`/posts/${id}`}
              style={{
                padding: '0.5rem 1rem',
                background: params.id === id.toString() ? '#0070f3' : '#eee',
                color: params.id === id.toString() ? 'white' : 'black',
                textDecoration: 'none',
                borderRadius: '4px'
              }}
            >
              Пост {id}
            </a>
          ))}
        </div>
      </div>

      <p style={{ marginTop: '2rem' }}>
        <a href="/" style={{ color: '#0070f3' }}>← Назад на главную</a>
      </p>
    </main>
  );
}
