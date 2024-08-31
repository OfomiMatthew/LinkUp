const modalSearch = document.getElementById('exampleModal3')
const searchButton = document.getElementById('search');
const closeModalSearchButton = modal.querySelector('.del');
const modalSearchBackground = modal.querySelector('.md-bg');
 
  searchButton.addEventListener('click',()=>{
modalSearch.classList.add('.is-active');
  })

  closeModalSearchButton.addEventListener('click',()=>{
    modalSearch.classList.remove('is-active');
  })

  modalSearchBackground.addEventListener('click',()=>{
    modalSearch.classList.remove('is-active');
  })