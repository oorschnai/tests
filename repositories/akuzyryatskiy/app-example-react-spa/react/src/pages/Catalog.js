import React from 'react';
import { Link } from 'react-router-dom';

function Catalog() {
  const items = [1, 5, 18, 42, 99];

  return (
    <div className="page">
      <h1>Страница каталога</h1>
      <p>Маршрут: /catalog</p>
      <nav className="nav-menu">
        <Link to="/">Главная</Link>
        <Link to="/catalog">Каталог</Link>
        <Link to="/catalog/18">Элемент 18</Link>
        <Link to="/about">О нас</Link>
      </nav>
      <div className="content">
        <h2>Список элементов каталога:</h2>
        <ul>
          {items.map(id => (
            <li key={id}>
              <Link to={`/catalog/${id}`}>Элемент {id}</Link>
            </li>
          ))}
        </ul>
      </div>
    </div>
  );
}

export default Catalog;
