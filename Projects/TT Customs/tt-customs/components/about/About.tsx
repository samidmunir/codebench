// components/about/About.tsx

'use client'

import { PiLightningBold, PiGear, PiPaintBrushBroad } from 'react-icons/pi'

const About = () => {
  return (
    <section className="bg-zinc-900 px-6 py-16 text-zinc-200 lg:mt-8 sm:mt-4 md:mt-8">
      <div className="max-w-5xl mx-auto text-center">
        <h2 className="text-4xl font-bold text-red-500 mb-4">About TT Customs</h2>
        <p className="text-zinc-400 mb-12">
          TT Customs is your go-to destination for elite automotive customization. From cutting-edge lighting kits to virtual dashboard upgrades and premium installations, we transform your vehicle into a masterpiece. Backed by top-tier service, expert craftsmanship, and a passion for performance, we redefine what it means to drive in style.
        </p>

        {/* Floating Feature Cards */}
        <div className="grid grid-cols-1 sm:grid-cols-3 gap-6">
          {/* Card 1 */}
          <div className="bg-zinc-800 border border-zinc-700 p-6 rounded-xl shadow-lg hover:shadow-red-500/20 transition transform hover:-translate-y-2">
            <PiLightningBold className="text-4xl text-red-500 mx-auto mb-4" />
            <h3 className="text-xl font-semibold mb-2">Performance Lighting</h3>
            <p className="text-sm text-zinc-400">
              Starlight headliners and ambient lighting kits that elevate your interior game.
            </p>
          </div>

          {/* Card 2 */}
          <div className="bg-zinc-800 border border-zinc-700 p-6 rounded-xl shadow-lg hover:shadow-red-500/20 transition transform hover:-translate-y-2">
            <PiGear className="text-4xl text-red-500 mx-auto mb-4" />
            <h3 className="text-xl font-semibold mb-2">Custom Installations</h3>
            <p className="text-sm text-zinc-400">
              Seamless integration of modern tech — virtual dashboards, retrofits, and more.
            </p>
          </div>

          {/* Card 3 */}
          <div className="bg-zinc-800 border border-zinc-700 p-6 rounded-xl shadow-lg hover:shadow-red-500/20 transition transform hover:-translate-y-2">
            <PiPaintBrushBroad className="text-4xl text-red-500 mx-auto mb-4" />
            <h3 className="text-xl font-semibold mb-2">Bespoke Styling</h3>
            <p className="text-sm text-zinc-400">
              Every detail tailored to your taste — because your ride should be as bold as you are.
            </p>
          </div>
        </div>
      </div>
    </section>
  );
};

export default About;
