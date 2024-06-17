import {
  BrowserRouter as Router,
  Route,
  Routes,
  Navigate,
} from "react-router-dom";
import Home from "./pages/Home";
import Login from "./pages/Login";
import { AuthProvider, useAuth } from "./contexts/AuthContext";

const PrivateRoute = ({ element: Element }: { element: JSX.Element }) => {
  const { isAuthenticated } = useAuth();
  return isAuthenticated ? Element : <Navigate to="/login" />;
};

const App = () => {
  return (
    <Router>
      <AuthProvider>
        <Routes>
          <Route path="/login" element={<Login />} />
          <Route path="/" element={<PrivateRoute element={<Home />} />} />
        </Routes>
      </AuthProvider>
    </Router>
  );
};

export default App;
