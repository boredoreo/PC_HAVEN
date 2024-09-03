document.addEventListener('DOMContentLoaded', function() {
     const menuBtn = document.querySelector('.menu-btn');
     const closeBtn = document.querySelector('.close-btn');
     const links = document.querySelector('.links');
 
     menuBtn.addEventListener('click', function() {
         links.classList.add('show-menu');
     });
 
     closeBtn.addEventListener('click', function() {
         links.classList.remove('show-menu');
     });
 });
 