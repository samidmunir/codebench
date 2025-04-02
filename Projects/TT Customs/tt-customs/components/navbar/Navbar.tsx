// 'use client'

// import TT_Customs_Logo from '../../public/TT_Customs_Logo.jpg'
// import Image from 'next/image'
// import NavLink from './navlink/NavLink'
// import { PiHouseLine, PiShoppingCart, PiWrench, PiDotsNine, PiShoppingCartFill, PiSignIn } from 'react-icons/pi'
// import { usePathname } from 'next/navigation'
// import NavSearch from './navsearch/NavSearch'


// const links = [
//     {
//         id: 0,
//         title: 'Home',
//         href: '/',
//         icon: <PiHouseLine />,
//     },
//     {
//         id: 1,
//         title: 'Shop',
//         href: '/shop',
//         icon: <PiShoppingCart />,
//     },
//     {
//         id: 2,
//         title: 'Services',
//         href: '/services',
//         icon: <PiWrench />,
//     },
//     {
//         id: 3,
//         title: 'More',
//         href: '/more',
//         icon: <PiDotsNine />,
//     },
// ]

// const Navbar = () => {
//     const pathname = usePathname()

//     return (
//         <nav className='fixed top-0 left-0 w-full z-50 border-b-2 border-red-500 px-16 py-4 bg-zinc-900 flex align-middle justify-between'>
//             <div className='flex flex-row align-middle gap-4 my-auto'>
//                 <Image src={TT_Customs_Logo} alt='Logo' height={75} width={75} className='my-auto'/>
//                 <h1 className='text-4xl my-auto text-zinc-500 font-bold'>TT CUSTOMS</h1>
//             </div>
//             <div className='my-auto'>
//                 <ul className='flex gap-8'>
//                     {
//                         links.map(link => <NavLink key={link.id} title={link.title} href={link.href} icon={link.icon} path={pathname} />)
//                     }
//                     <li>
//                         <NavSearch />
//                     </li>
//                 </ul>
//             </div>
//             <div className='flex gap-4 my-auto align-middle'>
//                 <button className='flex gap-2 text-lg text-zinc-500 align-middle p-2 border-b-2 border-zinc-500 transition-all hover:text-red-500 hover:border-red-500'>Login <PiSignIn className='my-auto'/></button>
//                 <button className='flex gap-2 text-lg text-zinc-500 align-middle p-2 border-b-2 border-zinc-500 transition-all hover:text-red-500 hover:border-red-500'>My Cart<PiShoppingCartFill className='my-auto' /></button>
//             </div>
//         </nav>
//     )
// }

// export default Navbar;

'use client'

import { useState } from 'react'
import TT_Customs_Logo from '../../public/TT_Customs_Logo.jpg'
import Image from 'next/image'
import NavLink from './navlink/NavLink'
import {
  PiHouseLine,
  PiShoppingCart,
  PiWrench,
  PiDotsNine,
  PiShoppingCartFill,
  PiSignIn,
  PiListBold,
  PiXBold
} from 'react-icons/pi'
import { usePathname } from 'next/navigation'
import NavSearch from './navsearch/NavSearch'

const links = [
  { id: 0, title: 'Home', href: '/', icon: <PiHouseLine /> },
  { id: 1, title: 'Shop', href: '/shop', icon: <PiShoppingCart /> },
  { id: 2, title: 'Services', href: '/services', icon: <PiWrench /> },
  { id: 3, title: 'More', href: '/more', icon: <PiDotsNine /> },
]

const Navbar = () => {
  const pathname = usePathname()
  const [menuOpen, setMenuOpen] = useState(false)

  return (
    <nav className="fixed top-0 left-0 w-full z-50 bg-zinc-900 border-b-2 border-red-500 shadow-md">
      <div className="max-w-7xl mx-auto px-6 py-4 flex justify-between items-center">
        {/* Logo and Brand */}
        <div className="flex items-center gap-4">
          <Image src={TT_Customs_Logo} alt="Logo" height={60} width={60} className="rounded-full" />
          <h1 className="text-2xl font-bold text-zinc-500">TT CUSTOMS</h1>
        </div>

        {/* Desktop Menu */}
        <ul className="hidden md:flex gap-8 items-center">
          {links.map(link => (
            <NavLink key={link.id} title={link.title} href={link.href} icon={link.icon} path={pathname} />
          ))}
          <li><NavSearch /></li>
          <li>
            <button className="flex gap-2 text-lg text-zinc-500 border-b-2 border-zinc-500 p-2 transition-all hover:text-red-500 hover:border-red-500">
              Login <PiSignIn className="my-auto" />
            </button>
          </li>
          <li>
            <button className="flex gap-2 text-lg text-zinc-500 border-b-2 border-zinc-500 p-2 transition-all hover:text-red-500 hover:border-red-500">
              My Cart <PiShoppingCartFill className="my-auto" />
            </button>
          </li>
        </ul>

        {/* Hamburger Button for Mobile */}
        <button
          onClick={() => setMenuOpen(!menuOpen)}
          className="md:hidden text-3xl text-red-500"
        >
          {menuOpen ? <PiXBold /> : <PiListBold />}
        </button>
      </div>

      {/* Mobile Menu Dropdown */}
      {menuOpen && (
        <div className="md:hidden bg-zinc-800 border-t border-zinc-700 px-6 py-4">
          <ul className="flex flex-col gap-4">
            {links.map(link => (
              <NavLink key={link.id} title={link.title} href={link.href} icon={link.icon} path={pathname} />
            ))}
            <li><NavSearch /></li>
            <li>
              <button className="flex gap-2 text-lg text-zinc-500 border-b-2 border-zinc-500 p-2 transition-all hover:text-red-500 hover:border-red-500">
                Login <PiSignIn className="my-auto" />
              </button>
            </li>
            <li>
              <button className="flex gap-2 text-lg text-zinc-500 border-b-2 border-zinc-500 p-2 transition-all hover:text-red-500 hover:border-red-500">
                My Cart <PiShoppingCartFill className="my-auto" />
              </button>
            </li>
          </ul>
        </div>
      )}
    </nav>
  )
}

export default Navbar
