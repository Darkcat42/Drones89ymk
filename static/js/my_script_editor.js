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
//    if(target.id == 'modal_link_act_open'){
//        modal_menu.classList.remove('close_modal')
//        modal_menu.classList.add('open_modal')
//        document.body.style.overflow='hidden'
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
        // модальное окно авторизации
        if(target.getAttribute('data-modal') == 'edit_menu'){
            open_modal()
            modal_header_title.textContent = 'Авторизация'
            fetch('/load_modal_menu_edit') // Делаем AJAX-запрос к серверу
            .then(response => response.text())
            .then(html => {
                modal_content_div.innerHTML = html; // Вставляем полученный HTML в контейнер
            });}//3
    }//2


})//1

// <!-- Кнопка для загрузки формы -->
// <button id="loadFormBtn">Показать форму подписки</button>

// <!-- Контейнер, куда будет вставлена форма -->
// <div id="formContainer"></div>

// <script>
// document.getElementById('loadFormBtn').addEventListener('click', function() {
//     
//     fetch('/load-subscribe-form')
//         .then(response => response.text())
//         .then(html => {
//             // Вставляем полученный HTML в контейнер
//             document.getElementById('formContainer').innerHTML = html;
//         });
// });
// </script>

// function edit_link_webpage(index){
//     // link = document.getElementById('link_webpage'+index)
//     // link_href = link.getAttribute('href')
//     // popap_menu.classList.remove('close_popap')
//     // popap_menu.classList.add('open_popap')
//     // popap_url_input = document.getElementById('popap_url')
//     // popap_title_h2 = document.getElementById('popap_title_h2')
//     // popap_select = document.getElementById('popap_select')
//     // popap_submit = document.getElementById('popap_submit')
//     // popap_form = document.getElementById('popap_form')
//     // popap_submit.value = 'Изменить'
//     // popap_select.style.display = 'none';
//     // popap_title_h2.textContent = 'редактирование маршрута'
//     // popap_url_input.value = link_href
//     // popap_name_input = document.getElementById('popap_name')
//     // popap_name_input.value = link.textContent
//     // data = '('+link_href+', '+link.textContent+')'
//     // let url = `${'/popap_edit_web_page'}?query=${encodeURIComponent(data)}`;
//     // popap_form.action = url
// }

