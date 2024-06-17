import axios from 'axios';

const api = axios.create({
  baseURL: 'http://localhost:8000',  // Cambia esta URL según sea necesario
});

export const login = async (username: string, password: string) => {
  const response = await api.post('/auth/token', {
    username,
    password,
  });
  return response.data;
};
