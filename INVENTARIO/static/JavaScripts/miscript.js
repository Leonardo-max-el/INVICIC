document.querySelectorAll('.activo').forEach(function(activo) {
    activo.addEventListener('click', function() {
        // Quitar la clase seleccionado de todos los activos
        document.querySelectorAll('.activo').forEach(function(activo) {
            activo.classList.remove('seleccionado');
        });

        // Agregar la clase seleccionado al activo clicado
        this.classList.add('seleccionado');

        // Mostrar los detalles del activo seleccionado
        var detalles = this.getAttribute('data-detalles');
        document.querySelector('.detalles').innerHTML = detalles;
        document.querySelector('.detalles').style.display = 'block';
    });
});