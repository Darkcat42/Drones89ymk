// получаем элементы со страницы
let btn_act_close = document.getElementById('modal_btn_close');
let modal_base = document.getElementById('modal_base');
let modal_message = document.getElementById('modal_message');
let modal_warning = document.getElementById('modal_warning');
let modal_header_title = document.getElementById('modal_header_title');
let modal_content = document.getElementById('modal_content');
document.addEventListener('submit', (evt) => {
    /*
    прослушиватель события тега form инпута с типом submit
    */
    evt.preventDefault(); 
    target = evt.target
    console.log(target.id)
    if(target.id != null){ // отлов кликабельных элементов
        switch(target.id){
            case 'login_form': check_login_form();
            console.log('asdasdasd')
                break;
        }
    }
});
function check_login_form(){
    let login_input = document.getElementById('login')
    let passwd_input = document.getElementById('login')
    if(login_input.value != ''){
        let form = document.getElementById('login_form')
        form.submit();
    } else {
         alert('заполните все поля')
    }
}
addEventListener('click', (evt) => {
    /*
    общий прослушиватель события click для отлова id элементов   
    по нажатию
    */
    target = evt.target
    if(target.id != null){ // отлов кликабельных элементов
        switch(target.id){
            case 'logout': open_warning('выйти из системы?', 'logout');
                break;
            case 'modal_btn_action': open_warning('выйти из системы?');
                break;
            case 'modal_btn_close':
                modal_base.classList.add('close_modal')
                break
        }
    }
    if(target.hasAttribute('data-modal') == true){
        switch(target.getAttribute('data-modal')){
            case 'login'    : open_modal('Авторизация', 'load_modal_form_login');
            break; // модальное окно авторизации
        }
    }//2
})//1 конец: addEventListener - click
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
            modal_content.innerHTML = html; 
        });
    modal_base.classList.remove('close_modal')
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

