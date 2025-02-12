'use client'
import { BsFillXDiamondFill, BsDisplayFill, BsDiagram3Fill, BsCurrencyExchange , BsChatLeftDotsFill  } from 'react-icons/bs'
import Link from 'next/link'
import { usePathname } from 'next/navigation'

const links = [
    {
        id: 0,
        icon: <BsDisplayFill />,
        href: '/',
        label: 'Overview',
    },
    {
        id: 1,
        icon: <BsDiagram3Fill />,
        href: '/components',
        label: 'Components',
    },
    {
        id: 2,
        icon: <BsCurrencyExchange />,
        href: '/pricing',
        label: 'Pricing',
    },
    {
        id: 3,
        icon: <BsChatLeftDotsFill />,
        href: '/testimonials',
        label: 'Testimonials',
    },
];

interface NavLinkProps {
    key: number;
    icon: React.ReactNode;
    href: string;
    label: string;
}

const NavLink = (props: NavLinkProps) => {
    const pathname = usePathname();
    return (
        <Link href={props.href} className={`${pathname === props.href ? 'text-indigo-500 border-indigo-500' : 'text-zinc-300 border-zinc-900'} flex text-xl items-center border-t-2  hover:text-indigo-500 hover:border-indigo-500 transition-all cursor-default`}>
            <span>{props.icon}</span>
            <p className='ml-2'>{props.label}</p>
        </Link>
    );
}

const Navbar = () => {
    return (
        <nav className='bg-zinc-900 flex justify-between px-8 py-2'>
            <div className='text-zinc-300 flex text-3xl items-center'>
                <BsFillXDiamondFill />
                <h1 className='ml-1'>UXcript</h1>
            </div>
            <div className='flex gap-8'>
                {
                    links.map((link) => (
                        <NavLink key={link.id} icon={link.icon} href={link.href} label={link.label} />
                    ))
                }
            </div>
            <div className='flex'>
                <input
                    type='email'
                    placeholder='Your email'
                    className='bg-zinc-800 opacity-75 text-indigo-500 px-2 placeholder:text-indigo-500 placeholder:text-xl hover:opacity-100 focus:outline-none transition-all cursor-default' 
                />
                <button className='outline-none border-2 border-indigo-500 text-indigo-500 opacity-75 text-xl py-1 px-2 hover:bg-indigo-500 hover:text-zinc-300 hover:scale-110 hover:opacity-100 transition-all cursor-default'>Subscribe</button>
            </div>
        </nav>
    );
}

export default Navbar;