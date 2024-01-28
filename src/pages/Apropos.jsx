import React from 'react';
import lawyer from '../assets/searchlawyer1.png'; // Import the lawyer image file
import Navbar from '../component/Navbar';
import Footer from '../component/Footer';

function Apropos() {
  return (
      <div>
          <Navbar/>
          <div className="flex">
     
      <div className="w-1/2 h-96 flex items-center justify-center bg-black">
        <div >
          <h1 className="text-4xl font-bold text-white ">Prenez un rendez-vous avec un avocat</h1>
        </div>
      </div>

      <div className="w-1/2 h-96">
        <div className="bg-cover bg-center h-full" style={{ backgroundImage: `url(${lawyer})` }}>
        </div>
      </div>
          </div>
        <div className="mx-16 flex items-center justify-center">
  <div className="mt-4 gap-10">
    <div className='flex my-4 text-4xl font-medium'>
      Trouvez l'avocat idéal pour vous 
    </div>
    <div className='flex items-center justify-center my-8 mt-12 mb-10 max-w-5xl'>
        <div className='border-r-2 border-dotted border-gray-400 mr-28 pr-20'>
            <ul className="list-disc grid gap-3 text-2xl">
            <li>Facile</li>
            <li>Rapide</li>
            <li>Accessible</li>
            </ul>
        </div>
        <div className="">
            Ce service de prise de rendez-vous en ligne vous permet de convenir d'une consultation en cabinet avec un avocat près de chez vous et compétent sur votre dossier. À cette occasion, vous pourrez poser toutes les questions souhaitées à votre avocat afin qu'il vous conseille avec précision sur votre situation et qu'il vous apporte des éléments de réponses clairs. De plus, vous maîtrisez votre budget en réglant votre consultation en avance à un prix fixe.
        </div>
        
    </div>
    <button
      className="bg-[#D04946] w-full mb-10 text-white font-semibold py-2 px-4 rounded focus:outline-none focus:shadow-outline mr-3"
      type="submit"
    >
      Faire une recherche
    </button>
        </div>
        
</div>

                    
        <Footer/>
                </div>
                
                
           
    
  );
}

export default Apropos;
