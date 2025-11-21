// мои функции для клиентской части
// получаем элементы со страницы
let btn_act_close = document.getElementById('modal_btn_close');
let modal_base = document.getElementById('modal_base');
let modal_message = document.getElementById('modal_message');
let modal_warning = document.getElementById('modal_warning');
let modal_header_title = document.getElementById('modal_header_title');
let modal_content = document.getElementById('modal_content');
function check_login_form(){
    /*
    функция отвечает за проверку правильности ввода на стороне клиента (доделать)
    */
    let login_input = document.getElementById('login')
    let passwd_input = document.getElementById('password')
    if(login_input.value != ''){
        let form = document.getElementById('login_form')
        form.submit();
    } else {
         alert('заполните все поля')
    }
}
async function open_modal(text, url){
    /*
    функция отвечает за показ каждого модального окна,
    html контент прилетает по AJAX с сервера в 
    контент-область модального окна
    */
    modal_header_title.textContent = text
    await fetch(url)
    .then(response => response.text())
    .then(html => {
            modal_content.innerHTML = html; 
        });
    modal_base.classList.remove('close_modal')
    return true
}
// function open_message(text){
//     /*
//     функция отвечает за показ каждого модального сообщения ползователю,
//     принимает текст сообщения  
//     */
//     let parag = document.getElementById('parag')
//     parag.textContent = text
//     modal_message.classList.remove('close_modal')
// //    document.body.style.overflow = 'hidden'
// }
// function open_warning(text, action){
//     /*
//     функция отвечает за показ модального окна предупреждения ползователю,
//     принимает текст сообщения  
//     */
//     let warning_paragraf = document.getElementById('warning_paragraf')
//     let modal_warning_btn_action = document.getElementById('modal_warning_btn_action')
//     modal_warning_btn_action.setAttribute('data-action', action)
//     warning_paragraf.textContent = text
//     modal_warning.classList.remove('close_modal')
//     document.body.style.overflow='hidden'
// }

