(function () {
const btnEliminar = document.querySelectorAll('.btnEliminar');

btnEliminar.forEach(btn=> {
btn.addEventListener('click', (e)=> {
    const confimacion = confirm('Estás seguro de eliminar');
    if (!confimacion){
        e.preventDefault();
        }
    });
});
})();