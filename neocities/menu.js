const menuToggle = document.querySelector('.menu-toggle');
const menuPrincipal = document.querySelector('#menu-principal');

function alternarMenu(aberto) {
    menuToggle.setAttribute('aria-expanded', aberto);
    menuToggle.setAttribute('aria-label', aberto ? 'Fechar menu' : 'Abrir menu');
    menuPrincipal.setAttribute('aria-hidden', !aberto);
    menuPrincipal.classList.toggle('aberto', aberto);
}

menuToggle.addEventListener('click', () => {
    alternarMenu(menuToggle.getAttribute('aria-expanded') !== 'true');
});

document.addEventListener('keydown', (evento) => {
    if (evento.key === 'Escape') alternarMenu(false);
});

document.addEventListener('click', (evento) => {
    if (!menuPrincipal.contains(evento.target) && !menuToggle.contains(evento.target)) {
        alternarMenu(false);
    }
});