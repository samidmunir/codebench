// components/footer/Footer.tsx

const Footer = () => {
    return (
      <footer className="bg-zinc-900 text-zinc-400 py-8 px-4 mt-0 border-t border-red-500">
        <div className="max-w-7xl mx-auto flex flex-col md:flex-row justify-between items-center gap-4 text-sm">
          <p>&copy; {new Date().getFullYear()} TT CUSTOMS. All rights reserved.</p>
          <div className="flex gap-6">
            <a href="/privacy" className="hover:text-zinc-200 transition">Privacy Policy</a>
            <a href="/terms" className="hover:text-zinc-200 transition">Terms of Service</a>
            <a href="/contact" className="hover:text-zinc-200 transition">Contact Us</a>
          </div>
        </div>
      </footer>
    );
  };
  
  export default Footer;  