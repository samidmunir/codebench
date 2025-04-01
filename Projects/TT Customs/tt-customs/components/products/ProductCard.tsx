// components/products/ProductCard.tsx

interface ProductCardProps {
    name: string
    price: number
    brand: string
    image: string
    fits: string[]
  }
  
  const ProductCard = ({ name, price, brand, image, fits }: ProductCardProps) => {
    return (
      <div className="bg-zinc-800 rounded-xl overflow-hidden border border-zinc-700 shadow-lg hover:shadow-red-500/20 transition">
        <img src={image} alt={name} className="w-full h-48 object-cover" />
        <div className="p-4 text-zinc-200">
          <h3 className="text-xl font-semibold mb-1 truncate">{name}</h3>
          <p className="text-sm text-zinc-400 mb-2">Brand: {brand}</p>
          <p className="text-sm text-zinc-500 mb-4">Fits: {fits.join(', ')}</p>
          <div className="flex justify-between items-center">
            <span className="text-red-500 font-bold">${price.toFixed(2)}</span>
            <button className="bg-red-500 hover:bg-red-600 text-white text-sm px-4 py-2 rounded-md transition">
              Add to Cart
            </button>
          </div>
        </div>
      </div>
    )
  }
  
  export default ProductCard
  