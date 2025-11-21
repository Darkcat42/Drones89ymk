document.addEventListener('click', (evt) => {
    /*
    общий прослушиватель события click для отлова элементов   
    по нажатию и атрибутам
    */
    target = evt.target
    if(target.hasAttribute('data-modal') == true){
        switch(target.getAttribute('data-modal')){
            case 'login'    : open_modal('Авторизация', '/loadModalBlock_anon/login');
            break; // модальное окно авторизации
            case 'scheduleDay_add'    : open_modal('Добавить день', '/loadModalBlock_user/schedule');
            break; // модальное окно добавления нового дня в расписание
            case 'news_add'    : open_modal('Добавить новость', '/loadModalBlock_user/news');
            break; // модальное окно добавления нового дня в расписание
        }
    }//2
    if(target.hasAttribute('data-action') == true){
            action = target.getAttribute('data-action')
            switch(action){
                case 'logout': document.location.href=action
                break;
            }
        }//2
    if(target.id != null){ 
        switch(target.id){
            case 'modal_btn_close':
                modal_base.classList.add('close_modal')
                break;
            case 'scheduleDay_addBtn': createDataScheduleDay();
                break;
            case 'scheduleDay_editBtn': 
                showScheduleDay(target.parentNode.getAttribute('data-scheduleDay-id'));
                break;
            case 'scheduleDay_UpdateBtn':
                updateScheduleDay()
                break;
            case 'scheduleDay_delBtn':
                deleteScheduleDay(target.parentNode.getAttribute('data-scheduleDay-id'));
                break;
        }
    }//2
})//1 конец: addEventListener - click
document.addEventListener('submit', (evt) => {
    /*
    прослушиватель события тега form инпут с типом submit
    */
    evt.preventDefault(); 
    target = evt.target
    if(target.id != null){ // отлов кликабельных элементов
        console.log('отлов кликабельных элементов')
        switch(target.id){
            case 'login_form': check_login_form();
                break;
        }
    }
});




