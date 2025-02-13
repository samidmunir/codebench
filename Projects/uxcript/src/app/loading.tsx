import { BsFillXDiamondFill } from 'react-icons/bs'

const Loading = () => {
    return (
        <div className='flex items-center justify-center h-screen'>
            <BsFillXDiamondFill className='text-8xl text-indigo-500 animate-spin' />
        </div>
    );
}

export default Loading;