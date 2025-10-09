function get_real_children(parent){
    /*
    функция принимает родительский элемент и возвращает
    настоящий массив его элементов  
    */
    return Array.from(parent.children)
}
function set_editor(elems_id){
    /*
    функция запускается из base.html при onload, 
    если current_user.is_authenticated == True, то
    функция принимает id элементов через запятую, накладывает на 
    элементы стили, которые обозначают возможность редактирония
    */
    massive_elems_id = elems_id.split(', ')
    massive_elems_id.forEach((elem, i) => {
        element = document.getElementById(elem)
        element.classList.add('editor_hover')});}
function open_modal(text, url){
    /*
    функция отвечает за показ каждого модального окна,
    html контент прилетает по AJAX с сервера в 
    контент-область модального окна
    */
    modal_header_title.textContent = text
        fetch(url)
        .then(response => response.text())
        .then(html => {
            modal_content_div.innerHTML = html; 
        });
    modal_menu.classList.remove('close_modal')
    modal_menu.classList.add('open_modal')
    document.body.style.overflow='hidden' 
}
function open_message(text){
    /*
    функция отвечает за показ каждого модального сообщения ползователю,
    принимает текст сообщения  
    */
    modal_message.classList.remove('close_modal')
    modal_message.classList.add('modal_message')
    message_paragraf.textContent=text
    document.body.style.overflow='hidden' 
}
function open_warning(text){
    /*
    функция отвечает за показ каждого модального сообщения ползователю,
    принимает текст сообщения  
    */
    modal_message.classList.remove('close_modal')
    modal_message.classList.add('modal_message')
    message_paragraf.textContent=text
    document.body.style.overflow='hidden' 
}
let modal_menu = document.getElementById('modal_menu')
let modal_message = document.getElementById('modal_message')
let message_paragraf = document.getElementById('message_paragraf')
let modal_header_title = document.getElementById('modal_header_title')
let modal_content_div = document.getElementById('modal_content_div')

addEventListener('click', (evt) => {
    target = evt.target
    // любое модальное окно
    if(target.id == 'logout'){
        open_warning()
    }
    if(target.id == 'modal_btn_act_close'){
        let modal_type = target.getAttribute('data-modal_type')
        if(modal_type == 'message'){
            modal_message.classList.remove('open_modal')
            modal_message.classList.add('close_modal')
            document.body.style.overflow='auto'
            modal_content_div.innerHTML = ''
        }
        else if(modal_type == 'modal_menu_block'){
            modal_menu.classList.remove('open_modal')
            modal_menu.classList.add('close_modal')
            document.body.style.overflow='auto'
            modal_content_div.innerHTML = ''
        }
        
    }//2
    if(target.hasAttribute('data-modal') == true){
        // модальное окно авторизации
        if(target.getAttribute('data-modal') == 'login'){
            open_modal('Авторизация', 'load_modal_form_login')
        }//3
        // модальное окно редактирования меню
        if(target.getAttribute('data-modal') == 'edit_menu'){
            open_modal('Редактирование меню', '/load_modal_menu_edit')
        }//3
    }//2
    if(target.id == 'delete_item_btn'){// запрос на удаление ссылки меню
    delete_id = target.getAttribute('data-delete_id')
    if(target.getAttribute('href') != '/main'){
        fetch('/delete_menu_link/'+delete_id) // AJAX-запрос
            .then(response => {
                if(response.status == 200){
                    open_message('ссылка удалена')    
                }}, // условие если запрос неудачный
            () => {alert(console.log('ошибка!'))})}}//2 конец: if - delete_item_btn
})//1 конец: addEventListener - click
let draggedItem = null; // переменная для временной записи объекта который мы тащим курсором
document.addEventListener('dragstart', (e) => {
  if (e.target.getAttribute('draggable')){
    draggedItem = e.target;
    draggedItem.classList.add('dragstart');
    draggedItem.parentNode.classList.add('drug_select');}});
document.addEventListener('dragover', (e) => {
  e.preventDefault();});
document.addEventListener('dragenter', (e) => {
    e.preventDefault();});
document.addEventListener('dragleave', (e) => {
    e.preventDefault();});
document.addEventListener('drop', (e) => {
  e.preventDefault();
  e.target.classList.remove('dragover')
    let container = e.target.parentNode.parentNode; 
    let allItems = Array.from(container.children);
    let targetIndex = allItems.indexOf(e.target.parentNode); // индекс под
    let draggedIndex = allItems.indexOf(draggedItem); // индекс в руках
    // console.log(targetIndex, draggedIndex) // цель тут это то что под курсором!
    container_id = container.id 
    draggedItem_p_id = draggedItem.parentNode.id  
    if(container_id == draggedItem_p_id){
        if (draggedIndex < targetIndex) // тащим слева на право 0 < 1  
        container.insertBefore(draggedItem, e.target.parentNode.nextSibling);
        else if(draggedIndex > targetIndex){
        container.insertBefore(draggedItem, e.target.parentNode);}
        e.target.parentNode.classList.remove('drug_item_enter')}});
document.addEventListener('dragend', (e) => {
  if (e.target.getAttribute('draggable')){
    draggedItem = e.target;
    draggedItem.classList.remove('dragstart');
    draggedItem.parentNode.classList.remove('drug_select');}});





