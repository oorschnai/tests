import React from 'react';
import { Link, useParams } from 'react-router-dom';

function CatalogItem() {
  const { id } = useParams();

  return (
    <div className="page">
      <h1>Элемент каталога</h1>
      <p>Маршрут: /catalog/{id}</p>
      <nav className="nav-menu">
        <Link to="/">Главная</Link>
        <Link to="/catalog">Каталог</Link>
        <Link to="/catalog/18">Элемент 18</Link>
        <Link to="/about">О нас</Link>
      </nav>
      <div className="content">
        <div className="item-card">
          <h2>ID элемента: {id}</h2>
          <p>Это детальная страница элемента каталога с ID = {id}</p>
          <p>Попробуйте обновить страницу (F5) или открыть этот URL напрямую в браузере.</p>
        </div>
        <Link to="/catalog" className="back-link">← Вернуться к каталогу</Link>
      </div>
    </div>
  );
}

export default CatalogItem;
