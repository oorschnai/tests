import React from 'react';
import { Link } from 'react-router-dom';

function About() {
  return (
    <div className="page">
      <h1>О нас</h1>
      <p>Маршрут: /about</p>
      <nav className="nav-menu">
        <Link to="/">Главная</Link>
        <Link to="/catalog">Каталог</Link>
        <Link to="/catalog/18">Элемент 18</Link>
        <Link to="/about">О нас</Link>
      </nav>
      <div className="content">
        <p>Это тестовое приложение для проверки работы SPA роутинга на Caddy сервере.</p>
        <p>Проверяемые сценарии:</p>
        <ul>
          <li>Переход по ссылкам внутри приложения</li>
          <li>Прямое обращение к URL (например, /catalog/18)</li>
          <li>Обновление страницы (F5) на любом маршруте</li>
        </ul>
      </div>
    </div>
  );
}

export default About;
