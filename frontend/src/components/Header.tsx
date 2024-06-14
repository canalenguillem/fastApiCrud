import React, { useContext } from "react";
import { Link } from "react-router-dom";
import { AuthContext } from "../contexts/AuthContext";
import "./Header.css";

const Header: React.FC = () => {
  const { user, logout } = useContext(AuthContext);

  return (
    <header className="header">
      <Link to="/" className="logo-link">
        <img src="/logo.png" alt="Enguillem App Logo" className="logo" />
      </Link>
      <nav className="menu">
        {/* Aquí puedes agregar más enlaces de navegación */}
      </nav>
      <div className="user-info">
        <span>{user?.name}</span>
        <button onClick={logout}>Logout</button>
      </div>
    </header>
  );
};

export default Header;
