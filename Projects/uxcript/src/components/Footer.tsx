import { BsFillXDiamondFill, BsFillCpuFill  } from 'react-icons/bs'

const Footer = () => {
    return (
        <footer className='bg-zinc-900 px-8 py-2'>
            <section className='flex justify-center gap-64'>
                <div>
                    <div className='flex items-center'>
                        <BsFillXDiamondFill className='text-3xl text-indigo-500' />
                        <h1 className='text-3xl text-indigo-500 ml-1'>UXcript</h1>
                    </div>
                    <p className='text-indigo-500 opacity-80'>A fusion of UX and TypeScript</p>
                    <div className='text-zinc-300 opacity-80 flex items-center text-md'>
                        <p>Munir Code Forge 2025</p>
                        <BsFillCpuFill className='ml-1' />
                    </div>
                </div>
                <div>
                    <h1 className='text-xl text-indigo-500'>Services</h1>
                    <p className='text-sm text-zinc-300 hover:text-indigo-500 transition-all cursor-default'>Branding</p>
                    <p className='text-sm text-zinc-300 hover:text-indigo-500 transition-all cursor-default'>Design</p>
                    <p className='text-sm text-zinc-300 hover:text-indigo-500 transition-all cursor-default'>Marketing</p>
                    <p className='text-sm text-zinc-300 hover:text-indigo-500 transition-all cursor-default'>Advertisement</p>
                </div>
                <div>
                    <h1 className='text-xl text-indigo-500'>Company</h1>
                    <p className='text-sm text-zinc-300 hover:text-indigo-500 transition-all cursor-default'>About</p>
                    <p className='text-sm text-zinc-300 hover:text-indigo-500 transition-all cursor-default'>Contact</p>
                    <p className='text-sm text-zinc-300 hover:text-indigo-500 transition-all cursor-default'>Jobs</p>
                    <p className='text-sm text-zinc-300 hover:text-indigo-500 transition-all cursor-default'>Press kit</p>
                </div>
                <div>
                    <h1 className='text-xl text-indigo-500'>Legal</h1>
                    <p className='text-sm text-zinc-300 hover:text-indigo-500 transition-all cursor-default'>Terms of use</p>
                    <p className='text-sm text-zinc-300 hover:text-indigo-500 transition-all cursor-default'>Privacy policy</p>
                    <p className='text-sm text-zinc-300 hover:text-indigo-500 transition-all cursor-default'>Cookie policy</p>
                </div>
            </section>
        </footer>
    );
}

export default Footer;