// // components/ui/LoadingSpinner.tsx

// const LoadingSpinner = () => {
//     return (
//       <div className="fixed top-0 left-0 w-full h-1.5 z-[9999]">
//         <div className="h-full bg-red-500 animate-pulse w-full transition-all duration-300" />
//       </div>
//     );
//   };
  
//   export default LoadingSpinner;
  

// components/ui/LoadingSpinner.tsx

// LoadingSpinner.tsx

import { PiSpinnerGap } from 'react-icons/pi'

const LoadingSpinner = () => {
  return (
    <div className="fixed inset-0 bg-black bg-opacity-60 flex items-center justify-center z-[9999] transition-opacity duration-500">
      <PiSpinnerGap className="animate-spin text-red-500 text-7xl" />
    </div>
  )
}

export default LoadingSpinner