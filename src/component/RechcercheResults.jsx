import React from 'react';
import lawyersData from '../db/data.json';

// Mapping between language abbreviations and full names
const languageMap = {
  fr: 'Français',
  an: 'Anglais',
  ar: 'Arabe',
  es: 'Espagnol',
  kb: 'Kabyle'
};

function LawyerList() {
  return (
    <div>
      <h1 className='text-7xl'>List of Lawyers</h1>
      {lawyersData.lawyers.map(lawyer => (
        <div key={lawyer.id}>
          <h2 className='text-3xl border-t-2 border-black mt-10'>{lawyer.name}</h2>
          <p>{lawyer.description}</p>
          <p>Activity: {lawyer.activity}</p>
          <p>
                  Languages:
                
                        {lawyer.language.map(lang => (
                            <img key={lang} src="https://flagsapi.com/DZ/flat/64.png" alt={lang} style={{ width: '30px', height: 'auto' }} />
                        ))}
                  
                
         
          </p>
        </div>
      ))}
    </div>
  );
}

export default LawyerList;
