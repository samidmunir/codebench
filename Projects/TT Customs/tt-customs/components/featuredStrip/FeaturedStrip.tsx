interface FeaturedStripProps {
    icon: React.ReactElement
    title: string
    price: number
    buttonText: string
}

const FeaturedStrip = (props: FeaturedStripProps) => {
    return (
        <div className='border border-red-500 flex items-center justify-between p-4 bg-zinc-800 text-zinc-100 rounded-md mb-2 mt-4'>
            <div className="w-12 flex justify-center text-xl">{props.icon}</div>
            <div className="flex-1 pl-4 truncate">{props.title}</div>
            <div className="w-24 text-right">${props.price.toFixed(2)}</div>
            <div className="ml-4">
                <button className="bg-red-500 hover:bg-red-600 text-white px-4 py-2 rounded-md text-sm">
                {props.buttonText}
                </button>
            </div> 
        </div>
    )
}

export default FeaturedStrip;