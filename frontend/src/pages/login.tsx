import { FormEvent, useState } from 'react';

import Layout from '../components/Layout';
import { login } from '../services/auth';

export default function LoginPage() {
  const [email, setEmail] = useState('');
  const [token, setToken] = useState('');

  const submit = async (event: FormEvent) => {
    event.preventDefault();
    const data = await login(email);
    setToken(data.access_token);
  };

  return (
    <Layout>
      <form className="card" onSubmit={submit}>
        <h2>Login</h2>
        <input value={email} onChange={(e) => setEmail(e.target.value)} placeholder="email" />
        <button type="submit">Sign in</button>
        {token && <p>Token received (truncated): {token.slice(0, 24)}...</p>}
      </form>
    </Layout>
  );
}
