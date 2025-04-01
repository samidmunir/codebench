// app/products/page.tsx or components/products/ProductsPage.tsx

'use client'

import { useState } from 'react'
import ProductCard from '@/components/products/ProductCard'

const products = [
  {
    name: 'Ambient Lighting Kit',
    price: 459.99,
    brand: 'TT Customs',
    image: '/images/ambient-light.jpg',
    fits: ['BMW', 'Mercedes', 'Audi']
  },
  {
    name: 'BMW Virtual Dash Upgrade',
    price: 699.99,
    brand: 'TT Customs',
    image: '/images/virtual-dash.jpg',
    fits: ['BMW']
  },
  {
    name: 'Starlight Roof Kit',
    price: 349.99,
    brand: 'TT Customs',
    image: '/images/starlight.jpg',
    fits: ['Universal']
  }
]

const ProductsPage = () => {
  const [query, setQuery] = useState('')
  const [filterBrand, setFilterBrand] = useState('')
  const [filterFit, setFilterFit] = useState('')

  const filteredProducts = products.filter(p =>
    p.name.toLowerCase().includes(query.toLowerCase()) &&
    (!filterBrand || p.brand === filterBrand) &&
    (!filterFit || p.fits.includes(filterFit))
  )

  return (
    <div className="px-6 py-16 bg-zinc-900 text-white min-h-screen">
      <h1 className="text-4xl font-bold text-red-500 mb-8 text-center">Browse Products</h1>

      {/* Filters */}
      <div className="flex flex-col md:flex-row gap-4 mb-8 justify-center">
        <input
          type="text"
          placeholder="Search products..."
          value={query}
          onChange={e => setQuery(e.target.value)}
          className="px-4 py-2 rounded-md bg-zinc-800 border border-zinc-700 text-white w-full md:w-1/3"
        />
        <select
          value={filterBrand}
          onChange={e => setFilterBrand(e.target.value)}
          className="px-4 py-2 rounded-md bg-zinc-800 border border-zinc-700 text-white"
        >
          <option value="">All Brands</option>
          <option value="TT Customs">TT Customs</option>
        </select>
        <select
          value={filterFit}
          onChange={e => setFilterFit(e.target.value)}
          className="px-4 py-2 rounded-md bg-zinc-800 border border-zinc-700 text-white"
        >
          <option value="">All Fits</option>
          <option value="BMW">BMW</option>
          <option value="Mercedes">Mercedes</option>
          <option value="Audi">Audi</option>
          <option value="Universal">Universal</option>
        </select>
      </div>

      {/* Products Grid */}
      <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-8">
        {filteredProducts.map((product, idx) => (
          <ProductCard key={idx} {...product} />
        ))}
      </div>
    </div>
  )
}

export default ProductsPage
