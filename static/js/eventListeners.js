document.addEventListener('change', (evt) => {
    /*    общий прослушиватель события change для отлова элементов   */
    let target = evt.target
    if(target.id != null){ 
        switch(target.id){
            case 'news_file':
                newsPreview_load(target.files[0]);
            case 'galleryEvent_files':       
                galleryEventPreview_load(target.files);
        }}
})
document.addEventListener('click', (evt) => {
    /*
    общий прослушиватель события click для отлова элементов   
    по нажатию и атрибутам
    */
    target = evt.target
    if(target.hasAttribute('data-modal') == true){
        /*    действия для модальных окон   */
        switch(target.getAttribute('data-modal')){
            case 'login' : // модальное окно авторизации
                open_modal('Авторизация', '/loadModalBlock_anon/login');
                break; 
            case 'scheduleDay_add' : // модальное окно добавления нового дня в расписание 
                open_modal('Добавить день', '/loadModalBlock_user/schedule');
                break; 
            case 'news_add' : // модальное окно добавления новой новости
                open_modal('Добавить новость', '/loadModalBlock_user/news_modal');
                break; 
            case 'galleryEvent_add' :  // модальное окно добавления нового события в галерею
                open_modal('Добавить событие', '/loadModalBlock_user/galleryEvent_modal');
                break;
            case 'buildMoreInfo_btnShow' :  // модальное окно добавления нового события в галерею
                open_modal('Информация о сборке', '/loadModalBlock_user/build_modal_more_info');
                break;
            case 'modalHeader_btnClose' : // закрыть модальное окно
                modal_base.classList.add('db_none')
                break; 
        }//3
    }//2
    if(target.hasAttribute('data-action') == true){
        /*    функции сайта   */
        action = target.getAttribute('data-action')
        switch(action){
            case 'logout': // выход из системы
                document.location.href=action
                break;
            }//3
        }//2
    if(target.id != null){ 
        /*    действия по id элемента   */
        switch(target.id){
            case 'modalHeader_btnClose': // закрыть модальное окно
                modal_base.classList.add('db_none')
                break;
            /*    страница - расписание   */
            case 'scheduleDay_addBtn': // добавить день в расписание
                createDataScheduleDay();
                break;
            case 'scheduleDay_editBtn': // изменить день в расписании (выбор дня)
                showScheduleDay(target.parentNode.getAttribute('data-scheduleDay-id'));
                break;
            case 'scheduleDay_UpdateBtn': // изменить день в расписании (изменение дня)
                updateScheduleDay()
                break;
            case 'scheduleDay_delBtn': // удалить день в расписании
                deleteScheduleDay(target.parentNode.getAttribute('data-scheduleDay-id'));
                break;
            /*    страница - новости   */
            case 'news_addBtn': // добавить новость
                createNewNews()
                break;
            /*    страница - галерея   */
            case 'galleryEvent_addBtn': // добавить галерею событий
                createGalleryEvent()
                break;
            case 'galleryEventImg_deLInput': // удалить изображение из вставки при создании галереи
                galleryEventImg_deLInput(target)
                break;
        }
    }//2
})//1 конец: addEventListener - click
document.addEventListener('submit', (evt) => {
    /*  прослушиватель события тега form для input type="submit"    */
    evt.preventDefault(); 
    target = evt.target
    if(target.id != null){ // отлов кликабельных элементов
        switch(target.id){
            case 'login_form': check_login_form();
                break;
        }
    }
});




