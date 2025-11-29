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
            case 'add_news' : // модальное окно добавления новой новости
                open_modal('Добавить новость', '/loadModalBlock_user/news_modal');
                break; 
            case 'add_news' : // модальное окно редактирования новой новости
                open_modal('Изменить новость', '/loadModalBlock_user/news_modal');
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
        switch(target.getAttribute('data-action')){
            /*    системное   */
            case 'logout': // выход из системы
                document.location.href='logout'
                break;
            /*    страница - расписание   */
            case 'edit_scheduleDay': // начать редактировать день в расписании
                startEdit_scheduleDay(target.parentNode.getAttribute('data-scheduleDay-id'));
                break;
            /*    страница - новости   */
            // case 'news_addBtn': // добавить новость
            //     createNewNews()
            //     break;
            // }//3
        }//2
    // if(target.id != null){ 
    //     /*    действия по id элемента   */
    //     switch(target.id){
           
    //         
    //         /*    страница - галерея   */
    //         // case 'galleryEvent_addBtn': // добавить галерею событий
    //         //     createGalleryEvent()
    //         //     break;
    //         // case 'galleryEventImg_deLInput': // удалить изображение из вставки при создании галереи
    //         //     galleryEventImg_deLInput(target)
    //         //     break;
    //     }
    }//2
})//1 конец: addEventListener - click
// мои функции для клиентской части
// получаем элементы со страницы
let btn_act_close = document.getElementById('modalHeader_btnClose');
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
    modal_base.classList.remove('db_none')
    return true
}
/*    главная страница - расписание   */
async function startEdit_scheduleDay(id){ 
    /*
    функция для загрузки модального окна вместо отдельной страницы 
    */
    await open_modal('Редактировать день', '/loadModalBlock_user/schedule');
    let url =  '/showScheduleDay/'+id
    fetch(url)
    .then(response => response.json())
    .then(data => {
        document.getElementById('scheduleDay_submit').value = 'Изменить день'
        let scheduleDay_form = document.getElementById('scheduleDay_form')
        scheduleDay_form.setAttribute('action', 'updateScheduleDay/'+id)

        document.getElementById('day_id').value = data['id']
        document.getElementById('day').value = data['day']
        document.getElementById('start').value = data['start']
        document.getElementById('end').value = data['end']
        document.getElementById('location').value = data['location']   
    })
}
/*    страница - новости   */
async function startEdit_news(id){
    await open_modal('Изменить новость', '/loadModalBlock_user/news_modal');
    let url =  '/show_news/'+id
    fetch(url)
    .then(response => response.json())
    .then(data => {
        document.getElementById('news_addBtn').value = 'Изменить'
        let scheduleDay_form = document.getElementById('scheduleDay_form')
        scheduleDay_form.setAttribute('action', 'updateScheduleDay/'+id)

        document.getElementById('news_id').value = data['id']
        document.getElementById('news_title').textContent = data['title']
        document.getElementById('news_text').value = data['news_desc']
        document.getElementById('news_placeholder').src = data['image_src']   
        
    })
}
function newsPreview_load(new_image){
    let images_preview = document.getElementById('images_preview')
    images_preview.innerHTML = ''
    let new_img = document.createElement('img');
    let reader = new FileReader();
    reader.onload = (evt) => {
        new_img.src = evt.target.result;
        new_img.width = 300;
        new_img.classList.add('col')
        images_preview.appendChild(new_img)
    }
    reader.readAsDataURL(new_image);
}
