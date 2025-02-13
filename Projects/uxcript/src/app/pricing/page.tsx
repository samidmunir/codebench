'use client'
import { useState, useEffect } from 'react'
import Loading from '@/app/loading'
import { BsPatchCheckFill } from 'react-icons/bs'


const pricingPlans = [
  {
    title: 'Free',
    subtitle: 'Get started with the essentials',
    price: 0.00,
    features: [
      'Basic UI Components (Buttons, Inputs, Cards)',
      'Open Source License',
      'Community Support',
      'Regular Updates',
      'Basic Theming Options',
    ],
  },
  {
    title: 'Personal',
    subtitle: 'For developers and freelancers',
    price: 50.00,
    features: [
      'Access to All Core UI Components',
      'Advanced Theming & Customization',
      'Responsive Design Support',
      'Email Support',
      'Component Documentation & Examples',
    ],
  },
  {
    title: 'Business',
    subtitle: 'For teams and businesses',
    price: 100.00,
    features: [
      'Access to Pro & Enterprise Components',
      'Figma & Design System Integration',
      'Priority Support & Feature Requests',
      'Custom Branding & White Labeling',
      'API Access & Custom Plugins',
    ],
  },
];

interface PricingCardProps {
  title: string;
  subtitle: string;
  price: number;
  features: string[];
}

const PricingCard = (props: PricingCardProps) => {
  const { title, subtitle, price, features } = props;
  return (
    <main className='bg-zinc-900 rounded-lg px-8 py-4 shadow-xl blur-sm opacity-80 hover:blur-none hover:opacity-100 hover:scale-110 transition-all cursor-default'>
      <div className='text-center'>
        <h2 className='text-zinc-300 text-3xl'>{title}</h2>
        <p className='text-zinc-300 text-lg'>{subtitle}</p>
      </div>
      <div>
        <p className='text-indigo-500 font-bold text-4xl text-center mt-8'>${price.toFixed(2)} / mo</p>
      </div>
      <div className='text-zinc-300 mt-8'>
        <p className='text-xs italic'>What's included:</p>
        <>
          {
            features.map((feature, index) => (
              <PlanFeature key={index} feature={feature} />
            ))
          }
        </>
      </div>
      <div className='flex justify-center gap-4 mt-4'>
        <button className='text-lg text-zinc-300 py-1 px-2 outline-none border-2 border-indigo-500 hover:bg-indigo-500 hover:text-zinc-300 hover:scale-110 transition-all cursor-default'>Explore</button>
        <button className='text-lg text-zinc-300 py-1 px-2 outline-none border-2 border-teal-500 hover:bg-teal-500 hover:text-zinc-300 hover:scale-110 transition-all cursor-default'>Subscribe</button>
      </div>
    </main>
  );
}

interface PlanFeatureProps {
  feature: string;
}

const PlanFeature = (props: PlanFeatureProps) => {
  return (
    <div className='flex items-center text-zinc-300'>
      <BsPatchCheckFill />
      <p className='ml-1'>{props.feature}</p>
    </div>
  );
}

const Pricing = () => {
  const [loading, setLoading] = useState<boolean>(true);

  useEffect(() => {
    const timer = setTimeout(() => setLoading(false), 1500);

    return () => clearTimeout(timer);
  }, []);

  return loading ? <Loading /> : (
    <main className='bg-stone-300 py-4 px-8 rounded-lg h-[540px]'>
      <h1 className='text-4xl text-center leading-tight'>Pricing Plans</h1>
      <p className='text-xl text-center italic leading-tight'>Choose the right subscription for you!</p>
      <section className='flex justify-between mt-4'>
        {pricingPlans.map((plan, index) => (
          <PricingCard key={index} {...plan} />
        ))}
      </section>
    </main>
  );
}

export default Pricing;