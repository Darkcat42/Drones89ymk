// мои функции для клиентской части
function to_url(url){
    /*
    функция перехода по ссылке  
    */
    console.log('переход по пути: '+url)
    document.location.href=url
}
document.addEventListener('contextmenu', function(event) {
    /*
    прослушиватель события контекстного меню по правой кнопке мыши
    */
    // event.preventDefault(); // Предотвращает появление стандартного контекстного меню
    console.log('Правая кнопка мыши нажата!');
});

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
    if(target.hasAttribute('data-action') == true){
            action = target.getAttribute('data-action')
            switch(action){
                case 'logout': to_url('/'+action)
                break;
            }
        }//2 
})//1 конец: addEventListener - click
