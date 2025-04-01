// import Image from 'next/image';
// import TT_Customs_Shop_Hero from '../../public/TT_Customs_Shop_Hero.jpg';
// import TT_Customs_Booking_Hero from '../../public/TT_Customs_Booking_Hero.jpg';

// const Hero = () => {
//   return (
//     <main className="grid grid-cols-1 md:grid-cols-2 min-h-screen">
//       {/* Left Hero Section */}
//       <div className="relative h-[500px] md:h-auto">
//         <Image
//           src={TT_Customs_Shop_Hero}
//           alt="Shop Hero"
//           fill
//           className="object-cover"
//           priority
//         />
//         <div className="absolute inset-0 flex flex-col justify-center items-center text-white p-8 z-10">
//           <h1 className="text-4xl font-bold mb-4 text-center">Welcome to the Shop</h1>
//           <p className="mb-6 text-center">Explore our exclusive collection and custom gear.</p>
//           <button className="bg-white text-black px-6 py-3 rounded-lg hover:bg-gray-300 transition">
//             Shop Now
//           </button>
//         </div>
//       </div>

//       {/* Right Hero Section */}
//       <div className="relative h-[500px] md:h-auto">
//         <Image
//           src={TT_Customs_Booking_Hero}
//           alt="Booking Hero"
//           fill
//           className="object-cover"
//           priority
//         />
//         <div className="absolute inset-0 flex flex-col justify-center items-center text-white p-8 z-10">
//           <h1 className="text-4xl font-bold mb-4 text-center">Book Your Appointment</h1>
//           <p className="mb-6 text-center">Reserve a spot for a custom fitting or consultation.</p>
//           <button className="bg-white text-black px-6 py-3 rounded-lg hover:bg-gray-300 transition">
//             Book Now
//           </button>
//         </div>
//       </div>
//     </main>
//   );
// };

// export default Hero;

// const Hero = () => {
//     return (
//       <main className="pt-24 grid grid-cols-1 md:grid-cols-2 min-h-screen">
//         {/* Left Hero Section with Parallax */}
//         <div
//           className="relative h-[500px] md:h-screen bg-fixed bg-center bg-cover flex items-center justify-center"
//           style={{ backgroundImage: `url('/TT_Customs_Shop_Hero.jpg')` }}
//         >
//           <div className="bg-zinc-900 opacity-90 p-8 text-center text-zinc-100 rounded-xl max-w-md mx-4 transition-all hover:opacity-100">
//             <h1 className="text-4xl font-bold mb-4">Welcome to the Shop</h1>
//             <p className="mb-6">Explore our exclusive collection and custom gear.</p>
//             <button className="bg-red-500 opacity-50 hover:opacity-100 hover:scale-110 text-white px-6 py-3 rounded-lg transition-all">
//               Shop Now
//             </button>
//           </div>
//         </div>
  
//         {/* Right Hero Section with Parallax */}
//         <div
//           className="relative h-[500px] md:h-screen bg-fixed bg-center bg-cover flex items-center justify-center"
//           style={{ backgroundImage: `url('/TT_Customs_Booking_Hero.jpg')` }}
//         >
//           <div className="bg-zinc-900 opacity-90 p-8 text-center text-zinc-100 rounded-xl max-w-md mx-4 transition-all hover:opacity-100">
//             <h1 className="text-4xl font-bold mb-4">Book Your Appointment</h1>
//             <p className="mb-6">Reserve a spot for a custom fitting or consultation.</p>
//             <button className="bg-red-500 opacity-50 hover:opacity-100 hover:scale-110 text-white px-6 py-3 rounded-lg transition-all">
//               Book Now
//             </button>
//           </div>
//         </div>
//       </main>
//     );
//   };

// export default Hero;

'use client'

import { Parallax } from 'react-scroll-parallax';
import { PiArrowCircleDown, PiLightbulb, PiShootingStar, PiProjectorScreenChart } from 'react-icons/pi'
import FeaturedStrip from '../featuredStrip/FeaturedStrip'

const featuredProducts = [
    {
        id: 0,
        icon: <PiLightbulb />,
        title: 'Ambient Lighting Kits',
        price: 459.99,
        buttonText: 'Shop Now'
    },
    {
        id: 1,
        icon: <PiShootingStar />,
        title: 'Starlight Kits',
        price: 349.99,
        buttonText: 'Shop Now'
    },
    {
        id: 2,
        icon: <PiProjectorScreenChart />,
        title: 'BMW Virtual Dashboard Upgrade',
        price: 699.99,
        buttonText: 'Shop Now'
    },
]

const featuredServices = [
    {
        id: 0,
        icon: <PiLightbulb />,
        title: 'Ambient Lighting Installation/Upgrade',
        price: 375.00,
        buttonText: 'Schedule Service'
    },
    {
        id: 1,
        icon: <PiShootingStar />,
        title: 'Starlight Installation',
        price: 250.00,
        buttonText: 'Schedule Service'
    },
    {
        id: 2,
        icon: <PiProjectorScreenChart />,
        title: 'BMW Virtual Dashboard Installation',
        price: 400.00,
        buttonText: 'Schedule Service'
    },
]

const Hero = () => {
  return (
    <main className="grid grid-cols-1 md:grid-cols-2 min-h-screen pt-24">
      {/* Left Hero Section */}
      <Parallax speed={-10}>
        <div
          className="relative h-[500px] md:h-screen bg-fixed bg-center bg-cover flex items-center justify-center"
          style={{ backgroundImage: `url('/TT_Customs_Shop_Hero.jpg')` }}
        >
          <div className="bg-zinc-900 bg-opacity-80 p-8 text-center text-zinc-100 rounded-xl max-w-md mx-4">
            <h1 className="text-4xl font-bold mb-4">Welcome to the Shop</h1>
            <p className="mb-6">Explore our exclusive collection and custom gear.</p>
            <button className="bg-red-500 hover:bg-red-600 text-white px-6 py-3 rounded-lg transition">
              Shop Now
            </button>
            <p className='mt-4'>Scroll for more <PiArrowCircleDown className='inline' /></p>
          </div>
        </div>
        <div className='p-8 bg-zinc-900'>
            <h1 className='text-red-500 text-4xl text-center'>Top Tier Customs Shop</h1>
            <h2 className='text-center text-3xl text-zinc-300'>Featured Products</h2>
            <div className='bg-zinc-800 w-[600] mx-auto mt-4 rounded-lg'>
                {featuredProducts.map(featuredProduct => <FeaturedStrip key={featuredProduct.id} icon={featuredProduct.icon} title={featuredProduct.title} price={featuredProduct.price} buttonText={featuredProduct.buttonText} />)}
            </div>
        </div>
      </Parallax>

      {/* Right Hero Section */}
      <Parallax speed={5}>
        <div
          className="relative h-[500px] md:h-screen bg-fixed bg-center bg-cover flex items-center justify-center"
          style={{ backgroundImage: `url('/TT_Customs_Booking_Hero.jpg')` }}
        >
          <div className="bg-zinc-900 bg-opacity-80 p-8 text-center text-zinc-100 rounded-xl max-w-md mx-4">
            <h1 className="text-4xl font-bold mb-4">Book Your Appointment</h1>
            <p className="mb-6">Reserve a spot for a custom fitting or consultation.</p>
            <button className="bg-red-500 hover:bg-red-600 text-white px-6 py-3 rounded-lg transition">
              Book Now
            </button>
            <p className='mt-4'>Scroll for more <PiArrowCircleDown className='inline' /></p>
          </div>
        </div>
        <div className='p-8 bg-zinc-900'>
            <h1 className='text-red-500 text-4xl text-center'>Top Tier Customs Services</h1>
            <h2 className='text-center text-3xl text-zinc-300'>Featured Products</h2>
            <div className='w-[600] mx-auto mt-4 rounded-lg'>
                {featuredServices.map(featuredService => <FeaturedStrip key={featuredService.id} icon={featuredService.icon} title={featuredService.title} price={featuredService.price} buttonText={featuredService.buttonText} />)}
            </div>
        </div>
      </Parallax>
    </main>
  );
};

export default Hero;