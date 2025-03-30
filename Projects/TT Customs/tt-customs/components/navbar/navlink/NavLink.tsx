'use client'

import Link from 'next/link'

interface NavLinkProps {
    title: string
    href: string
    icon: React.ReactElement
    path: string
}

const NavLink = (props: NavLinkProps) => {
    return (
        <li className={props.path === props.href ? 'text-red-500 border-t-2 border-red-500' : 'text-slate-500 border-t-2 border-zinc-900 transition-all hover:border-t-2 hover:border-zinc-500'}>
            <Link href={props.href} className='flex align-middle gap-2 text-xl cursor-default'>
                <p className='my-auto'>{props.icon}</p>
                <p className='my-auto'>{props.title}</p>
            </Link>
        </li>
    )
}

export default NavLink;