import React from 'react';
import { Link } from 'react-router-dom';

function Home() {
  return (
    <div className="page">
      <h1>Главная страница</h1>
      <p>Маршрут: /</p>
      <nav className="nav-menu">
        <Link to="/">Главная</Link>
        <Link to="/catalog">Каталог</Link>
        <Link to="/catalog/18">Элемент 18</Link>
        <Link to="/about">О нас</Link>
      </nav>
      <div className="content">
        <p>Добро пожаловать в тестовое SPA приложение для проверки роутинга Caddy!</p>
      </div>
    </div>
  );
}

export default Home;
