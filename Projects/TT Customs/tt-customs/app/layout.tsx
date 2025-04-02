import type { Metadata } from "next";
import "./globals.css";

import Navbar from "@/components/navbar/Navbar";
import RouteChangeIndicator from "@/components/RouteChangeIndicator";
import About from "@/components/about/About";
import Testimonials from "@/components/common/Testimonials";
import Subscribe from "@/components/subscribe/Subscribe";
import Footer from "@/components/footer/Footer";

export const metadata: Metadata = {
  title: "TT Customs",
  description: "Top Tier Customs",
};

export default function RootLayout({
  children,
}: Readonly<{
  children: React.ReactNode;
}>) {
  return (
    <html lang="en">
      <body className='bg-zinc-900'>
        <Navbar />
        <RouteChangeIndicator />
        {children}
        <About />
        <Testimonials />
        <Subscribe />
        <Footer />
      </body>
    </html>
  );
}