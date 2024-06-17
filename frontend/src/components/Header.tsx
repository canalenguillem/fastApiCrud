import React from "react";
import { Link } from "react-router-dom";
import { useAuth } from "../contexts/AuthContext"; // Asegúrate de importar useAuth
import "./Header.css";

const Header = () => {
  const { logout } = useAuth();

  return (
    <header className="header">
      <div className="logo">
        <Link to="/">Logo</Link>
      </div>
      <nav className="menu">
        <Link to="/">Home</Link>
        <Link to="/profile">Profile</Link>
      </nav>
      <div className="profile">
        <button onClick={logout}>Logout</button>
      </div>
    </header>
  );
};

export default Header;
