import React from "react";
import Header from "../components/Header";
import Footer from "../components/Footer";
import "./Home.css"; // Crear o actualizar el archivo Home.css para los estilos

const Home = () => {
  return (
    <>
      <Header />
      <div className="content">
        <h1>Welcome to the Dashboard</h1>
      </div>
      <Footer />
    </>
  );
};

export default Home;
