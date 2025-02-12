import type { Metadata } from 'next'
import './globals.css'
import Navbar from '@/components/Navbar'
import ClientPage from '@/components/ClientPage'
import Footer from '@/components/Footer'

export const metadata: Metadata = {
  title: 'UXcript',
  description: 'A fusion of UX and Typescript',
}

export default function RootLayout({
  children,
}: Readonly<{
  children: React.ReactNode;
}>) {
  return (
    <html lang='en'>
      <body>
        <Navbar />
        <ClientPage>{children}</ClientPage>
        <Footer />
      </body>
    </html>
  );
}