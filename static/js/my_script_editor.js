// получаем элементы со страницы
let btn_act_close = document.getElementById('modal_btn_close');
let modal_section = document.getElementById('modal_section');
let modal_message = document.getElementById('modal_message');
let modal_warning = document.getElementById('modal_warning');
// const parag = document.getElementById('message_paragraf');
let modal_header_title = document.getElementById('modal_header_title');
let modal_content_div = document.getElementById('modal_content_div');
addEventListener('click', (evt) => {
    /*
    общий прослушиватель события click для отлова id элементов   
    по нажатию
    */
    target = evt.target
    if(target.id != null){ // отлов кликабельных элементов
        switch(target.id){
            case 'logout': open_warning('выйти из системы?', 'logout');
            RemoveCol() // чужая функция
            break;
            case 'modal_btn_action': open_warning('выйти из системы?');
            RemoveCol() // чужая функция
            break;
            case 'modal_btn_close':
                modal_section.classList.add('close_modal')
                modal_message.classList.add('close_modal')
                modal_warning.classList.add('close_modal')
                break
        }
    }
    if(target.hasAttribute('data-modal') == true){
        switch(target.getAttribute('data-modal')){
            case 'login'    : open_modal('Авторизация', 'load_modal_form_login');
            break; // модальное окно авторизации
            case 'edit_menu': open_modal('Редактирование меню', '/load_modal_menu_edit');
            break; // модальное окно редактирования меню
        }
    }//2
    if(target.hasAttribute('data-action') == true){
        action = target.getAttribute('data-action')
        switch(action){
            case 'logout': to_url('/'+action)
            break;
        }
    }//2 
    if(target.id == 'delete_item_btn'){// запрос на удаление ссылки меню
        delete_id = target.getAttribute('data-delete_id')
        if(target.getAttribute('href') != '/main'){
            open_message('ссылка удалена')
//            fetch('/delete_menu_link/'+delete_id) // AJAX-запрос
//                .then(response => {
//                    if(response.status == 200){
//                        open_message('ссылка удалена')
//                    }}, // условие если запрос неудачный
//                    () => {alert(console.log('ошибка!'))})
                    }
        else{
            open_warning('удалить ссылку на главную?', '/delete_menu_link/'+delete_id)
        }
                }//2 конец: if - delete_item_btn
})//1 конец: addEventListener - click
let draggedItem = null; // переменная для временной записи объекта который мы тащим курсором
document.addEventListener('dragstart', (e) => {
    console.log(draggedItem)
    console.log(e.target)
    /*
    общий прослушиватель старта события drag_and_drop
    */
    if (e.target.getAttribute('draggable')){
        draggedItem = e.target;
        draggedItem.classList.add('dragstart');
        draggedItem.parentNode.classList.add('drug_select');
        }
         });
document.addEventListener('dragover', (e) => {
    /*
    общий прослушиватель события drag_and_drop - "над целью"
    */
    e.preventDefault();});
document.addEventListener('dragenter', (e) => {
    /*
    общий прослушиватель события drag_and_drop - "зашел в границы цели" 
    */
    e.preventDefault();});
document.addEventListener('dragleave', (e) => {
    /*
    общий прослушиватель старта события drag_and_drop "вышел из границ цели" 
    */
    e.preventDefault();});
document.addEventListener('drop', (e) => {
    /*
    общий прослушиватель старта события drag_and_drop 
    - "пользователь отпустил цель из лап мыши" 
    */
    e.preventDefault();
    e.target.classList.remove('dragover')
    let target_container = e.target.parentNode.parentNode; 
    let allItems = Array.from(target_container.children);
    let targetIndex = allItems.indexOf(e.target.parentNode); // индекс под
    let draggedIndex = allItems.indexOf(draggedItem); // индекс в руках
    // (targetIndex, draggedIndex) // цель тут это то что под курсором!
    console.log(target_container)
            console.log(draggedItem.parentNode)
    if(target_container == draggedItem.parentNode){

            if (draggedIndex < targetIndex) // тащим слева на право 0 < 1  
                target_container.insertBefore(draggedItem, e.target.parentNode.nextSibling);
            else if(draggedIndex > targetIndex){
                target_container.insertBefore(draggedItem, e.target.parentNode);}
                e.target.parentNode.classList.remove('drug_item_enter')
    }else{
        alert('неверная цель для перемещения')
    }
    });
document.addEventListener('dragend', (e) => {
    /*
    общий прослушиватель старта события drag_and_drop
    - конец события перетаскивания
    */
    if (e.target.getAttribute('draggable')){
        draggedItem = e.target;
        draggedItem.classList.remove('dragstart');
        draggedItem.parentNode.classList.remove('drug_select');}});
// мои функции для клиентской части
function to_url(url){
    /*
    функция перехода по ссылке  
    */
    console.log('переход по пути: '+url)
    document.location.href=url
}
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
    massive_elems_id.forEach((elem) => {
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
    modal_section.classList.remove('close_modal')
    document.body.style.overflow='hidden' 
}
function open_message(text){
    /*
    функция отвечает за показ каждого модального сообщения ползователю,
    принимает текст сообщения  
    */
    let parag = document.getElementById('parag')
    parag.textContent = text
    modal_message.classList.remove('close_modal')
    document.body.style.overflow = 'hidden' 
}
function open_warning(text, action){
    /*
    функция отвечает за показ модального окна предупреждения ползователю,
    принимает текст сообщения  
    */
    let warning_paragraf = document.getElementById('warning_paragraf')
    let modal_warning_btn_action = document.getElementById('modal_warning_btn_action')
    modal_warning_btn_action.setAttribute('data-action', action)
    warning_paragraf.textContent = text
    modal_warning.classList.remove('close_modal')
    document.body.style.overflow='hidden'


}


// функции чужие предоставленные с изначальным проектом на изучение и переработку
function RemoveCol() { // Навигация для мобильной версии
    if(/iPhone|iPad|iPod|Android/i.test(navigator.userAgent)){
        let el = document.getElementById('navbarNavAltMarkup');
        el.classList.remove('show');
        HeaderFull()
    }   
}