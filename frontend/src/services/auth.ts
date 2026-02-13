import { api } from './api';

export async function login(email: string, role = 'paid_member') {
  const { data } = await api.post('/auth/login', { email, role });
  return data;
}
