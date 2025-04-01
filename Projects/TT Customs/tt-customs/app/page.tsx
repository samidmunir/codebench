// page.tsx
'use client'

import { ParallaxProvider } from 'react-scroll-parallax'
import Hero from '@/components/hero/Hero'

export default function Home() {
  return (
    <ParallaxProvider>
      <Hero />
    </ParallaxProvider>
  )
}
