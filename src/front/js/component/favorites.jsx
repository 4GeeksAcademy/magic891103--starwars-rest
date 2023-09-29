import React, { useEffect, useContext } from 'react';
import { Context } from '../store/appContext';
import { Link } from 'react-router-dom';

const FavoriteItem = ({ item, onDelete }) => (
  <div className='dropdown-item d-flex justify-content-between align-items-center'>
    <Link to={`/${item.type}Page/${item.og_id}`}>
      <p className='my-1'>{item.name}</p>
    </Link>
    <button className="btn btn-danger ms-1" onClick={() => onDelete(item.fav_id)}>
      <i className="fa-solid fa-trash-can" aria-hidden="true"></i>
      <span className="visually-hidden">Delete</span>
    </button>
  </div>
);

const Favorites = () => {
  const { store, actions } = useContext(Context);

  useEffect(() => {
    actions.getUserFavorites();
  }, [actions]);  // Added actions as a dependency to suppress warning, assuming actions doesn't change often

  return (
    <div className="dropdown-center">
      <button 
        className="btn btn-primary dropdown-toggle" 
        type="button" 
        data-bs-toggle="dropdown" 
        aria-expanded="false"
        aria-label="Toggle favorites dropdown"
      >
        Favorites 
        {store.userFavorites.length > 0 && (
          <span className='bg-light ms-1 text-danger px-2 fw-semibold rounded-circle'>
            {store.userFavorites.length}
          </span>
        )}
      </button>
      <ul className="dropdown-menu dropdown-menu-end" aria-labelledby="favoritesDropdown">
        {store.userFavorites.map((item, idx) => (
          <FavoriteItem key={idx} item={item} onDelete={actions.deleteUserFavorite} />
        ))}
        <li><hr className='dropdown-divider' /></li>
        <button className='btn ms-2 btn-danger' onClick={actions.logout}>Logout</button>
      </ul>
    </div>
  );
};

export default React.memo(Favorites);