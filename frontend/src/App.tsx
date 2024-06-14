import React from "react";
import {
  BrowserRouter as Router,
  Route,
  Routes,
  Navigate,
} from "react-router-dom";
import { AuthProvider, AuthContext } from "./contexts/AuthContext";
import Home from "./pages/Home";
import Login from "./pages/Login";
import Header from "./components/Header";

const App: React.FC = () => {
  return (
    <AuthProvider>
      <Router>
        <AuthContext.Consumer>
          {({ user }) => (
            <>
              {user && <Header />}
              <Routes>
                <Route
                  path="/login"
                  element={!user ? <Login /> : <Navigate to="/" />}
                />
                <Route
                  path="/"
                  element={user ? <Home /> : <Navigate to="/login" />}
                />
              </Routes>
            </>
          )}
        </AuthContext.Consumer>
      </Router>
    </AuthProvider>
  );
};

export default App;
