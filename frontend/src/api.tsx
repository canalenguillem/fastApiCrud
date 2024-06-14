import axios from "axios";

const api = axios.create({
  baseURL: "http://localhost:8000", // Asegúrate de que esta URL sea la correcta para tu backend
});

export const getUsers = async () => {
  const response = await api.get("/users/");
  return response.data;
};
