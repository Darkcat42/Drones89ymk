// alert('test')
function get_real_children(parent){
    return Array.from(parent.children)
}
function set_editor(elems_id){
    massive_elems_id = elems_id.split(', ')
    console.log(massive_elems_id)
    massive_elems_id.forEach((elem, i) => {
        // console.log(elem)
        element = document.getElementById(elem)
        element.classList.add('editor_hover')

});

}
function open_modal(){
    modal_menu.classList.remove('close_modal')
    modal_menu.classList.add('open_modal')
    document.body.style.overflow='hidden' // отключаем скролл для сайта
    
}
// window.addEventListener("load", function() {
//   set_editor(); // Ваша функция здесь
// });
addEventListener('click', (evt) => {
    target = evt.target
    console.log(target.id)
    modal_menu = document.getElementById('modal_menu')
    modal_header_title = document.getElementById('modal_header_title')
    modal_content_div = document.getElementById('modal_content_div')
    // любое модальное окно
    if(target.id == 'modal_btn_act_close'){
        modal_menu.classList.remove('open_modal')
        modal_menu.classList.add('close_modal')
        document.body.style.overflow='auto'
        modal_content_div.innerHTML = ''
    }//2
    if(target.hasAttribute('data-modal') == true){
        // модальное окно авторизации
        if(target.getAttribute('data-modal') == 'login'){
            open_modal()
            modal_header_title.textContent = 'Авторизация'
            fetch('/load_modal_form_login') // Делаем AJAX-запрос к серверу
            .then(response => response.text())
            .then(html => {
                modal_content_div.innerHTML = html; // Вставляем полученный HTML в контейнер
            });}//3
        // модальное окно редактирования меню
        if(target.getAttribute('data-modal') == 'edit_menu'){
            open_modal()
            modal_header_title.textContent = 'Редактирование меню'
            fetch('/load_modal_menu_edit') // Делаем AJAX-запрос к серверу
            .then(response => response.text())
            .then(html => {
                modal_content_div.innerHTML = html; // Вставляем полученный HTML в контейнер
            });}//3
    }//2
    if(target.name == 'select_type'){

            if(target.options[1].getAttribute('name') == 'edit_menu_type'){
            }
        }
 
})//1

addEventListener('dragstart', (evt) => {
    target=evt.target
    target.classList.add(`selected`);
})
addEventListener('dragend', (evt) => {
    target=evt.target
    target.classList.remove(`selected`);
})




