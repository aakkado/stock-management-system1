const elementos = document.querySelectorAll('.navigation span');

document.addEventListener('DOMContentLoaded', function() {
    const elementoEstoque = document.querySelector('.navigation span:first-child');
    elementoEstoque.classList.add('cor-clicado');
  });
  

elementos.forEach(function(elemento) {
    elemento.addEventListener('click', function() {
      elementos.forEach(function(el) {
        el.classList.remove('cor-clicado');
      });
      this.classList.add('cor-clicado');
    });
  });