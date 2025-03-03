'use client'
import { useState, useEffect } from 'react'
import Loading from '@/app/loading'

const Home = () => {
  const [loading, setLoading] = useState<boolean>(true);

  useEffect(() => {
    const timer = setTimeout(() => setLoading(false), 1500);

    return () => clearTimeout(timer);
  }, []);

  return loading ? <Loading /> : (
    <main>
      <h1>HOME</h1>
    </main>
  );
}

export default Home;