// app/services/layout.tsx

import Navbar from '@/components/navbar/Navbar'
import Footer from '@/components/footer/Footer'

export default function ServicesLayout({ children }: { children: React.ReactNode }) {
  return (
    <>
      <Navbar />
      <main className="pt-24">{children}</main>
    </>
  )
}