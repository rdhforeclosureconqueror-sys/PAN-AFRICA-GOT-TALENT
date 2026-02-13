import Link from 'next/link';
import { ReactNode } from 'react';

export default function Layout({ children }: { children: ReactNode }) {
  return (
    <main>
      <h1>📦 PAN-AFRICAN GOT TALENT</h1>
      <nav style={{ display: 'flex', gap: 12, marginBottom: 16 }}>
        <Link href="/">Home</Link>
        <Link href="/dashboard">Dashboard</Link>
        <Link href="/pagt/leaderboard">Leaderboard</Link>
        <Link href="/profile">Profile</Link>
      </nav>
      {children}
    </main>
  );
}
