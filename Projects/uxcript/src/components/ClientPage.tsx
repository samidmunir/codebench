import { ReactNode } from 'react'

const ClientPage = ({children}: {children: ReactNode}) => {
    return (
        <main className='bg-stone-500 px-8 py-4 h-[580px]'>
            {children}
        </main>
    );
}

export default ClientPage;