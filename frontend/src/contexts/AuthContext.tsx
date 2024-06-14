import React, { createContext, useState, useEffect } from "react";
import axios from "axios";

interface AuthContextType {
  user: any;
  login: (email: string, password: string) => Promise<void>;
  logout: () => void;
}

export const AuthContext = createContext<AuthContextType | undefined>(
  undefined
);

export const AuthProvider: React.FC = ({ children }) => {
  const [user, setUser] = useState(null);

  useEffect(() => {
    // Check if the user is logged in on initial load
    const token = localStorage.getItem("token");
    if (token) {
      axios.defaults.headers.common["Authorization"] = `Bearer ${token}`;
      axios
        .get("/api/auth/me")
        .then((response) => {
          setUser(response.data);
        })
        .catch(() => {
          logout();
        });
    }
  }, []);

  const login = async (email: string, password: string) => {
    const response = await axios.post("/api/auth/login", { email, password });
    const { token, user } = response.data;
    localStorage.setItem("token", token);
    axios.defaults.headers.common["Authorization"] = `Bearer ${token}`;
    setUser(user);
  };

  const logout = () => {
    localStorage.removeItem("token");
    delete axios.defaults.headers.common["Authorization"];
    setUser(null);
  };

  return (
    <AuthContext.Provider value={{ user, login, logout }}>
      {children}
    </AuthContext.Provider>
  );
};
