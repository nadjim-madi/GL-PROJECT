import React from 'react'

function Navbar() {
  return (
      <div>
          <br />
          <br />
          <div className='border-b-2  border-b-[#ECECEC] '>
              <a href="/registration">
          <button className='rounded-full text-2xl bg-[#D04946] pb-2 px-2 top-1 right-2 absolute text-white'>
            connexion
          </button>
        </a>
            <div>
                  <div className='flex gap-12 ml-3 top-2 absolute text-[#25233B] text-2xl'>
                      <div>LOGO</div>
                      <a href="#">HOME</a>
                      <a href="/Apropos">PRENDRE UN RENDEZ-VOUS</a>
                      <a href="#">A PROPOS</a>
                  </div>      
              </div>  
              
          </div>
          
    </div>
  )
}

export default Navbar