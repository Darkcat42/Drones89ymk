// alert('test')
function get_real_children(parent){
    return Array.from(parent.children)
}
function set_editor(elems_id){
    massive_elems_id = elems_id.split(', ')
    // console.log(massive_elems_id)
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
    // console.log(target.id)
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
 
    if(target.id == 'move_item_bnt'){
        
    }



})//1 конец: addEventListener - click

let draggedItem = null;
document.addEventListener('dragstart', (e) => {
  if (e.target.getAttribute('draggable')){
    draggedItem = e.target;
    draggedItem.classList.add('dragstart');
    draggedItem.parentNode.classList.add('drug_select');

  }
});
document.addEventListener('dragover', (e) => {
  e.preventDefault();
//   drug_select_node_list = e.target.parentNode.querySelectorAll('.drug_select')
//   drug_select_real_array = Array.from(drug_select_node_list)
//    console.log(drug_select_real_array)
//   if(drug_select_real_array[0].parentNode == e.target.parentNode){
//     console.log('sdfsdfds')
//     drug_select_real_array[0].classList.remove('My_D_none')
//     drug_select_real_array[1].classList.remove('My_D_none')
//   }
  
  
});
document.addEventListener('dragenter', (e) => {
    if(e.target.parentNode === draggedItem.parentNode){
e.preventDefault();
  e.target.classList.add('dragover')
    }
});
document.addEventListener('dragleave', (e) => {
    if(e.target.parentNode === draggedItem.parentNode){
e.preventDefault();
  e.target.classList.remove('dragover')
    }
});
document.addEventListener('drop', (e) => {
  e.preventDefault();
  e.target.classList.remove('dragover')
    let container = e.target.parentNode.parentNode; 
    let allItems = Array.from(container.children);
    let targetIndex = allItems.indexOf(e.target.parentNode); // индекс под
    let draggedIndex = allItems.indexOf(draggedItem); // индекс в руках
    console.log(targetIndex, draggedIndex) // цель тут это то что под курсором!
    container_id = container.id 
    draggedItem_p_id = draggedItem.parentNode.id  
    if(container_id == draggedItem_p_id){
        if (draggedIndex < targetIndex) // тащим слева на право 0 < 1  
        container.insertBefore(draggedItem, e.target.parentNode.nextSibling);
        else if(draggedIndex > targetIndex){
        container.insertBefore(draggedItem, e.target.parentNode);  
        }
    }
});
document.addEventListener('dragend', (e) => {
  if (e.target.getAttribute('draggable')){
    draggedItem = e.target;
    draggedItem.classList.remove('dragstart');
    draggedItem.parentNode.classList.remove('drug_select');
  }
});





