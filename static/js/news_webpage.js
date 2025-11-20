// // получаем элементы со страницы
// let btn_act_close = document.getElementById('modal_btn_close');
// let modal_base = document.getElementById('modal_base');
// // let modal_message = document.getElementById('modal_message');
// // let modal_warning = document.getElementById('modal_warning');
// let modal_header_title = document.getElementById('modal_header_title');
// let modal_content = document.getElementById('modal_content');
document.addEventListener('click', (evt) => {
    /*
    общий прослушиватель события click для отлова id элементов   
    по нажатию
    */
    target = evt.target
    if(target.id != null){ // отлов кликабельных элементов
        switch(target.id){
            case 'modal_btn_close':
                modal_base.classList.add('close_modal')
                break
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
    }
    if(target.hasAttribute('data-modal') == true){
        switch(target.getAttribute('data-modal')){
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
function deleteScheduleDay(id){
    url = '/deleteScheduleDay/'+id
    let response = fetch(url)
    .then(response => response.text())
    .then(html => {
        elem = document.querySelector('[data-scheduleDay-id="'+html+'"]')
        elem.remove()
    })
}
function editModal_ScheduleDay(idVal, dayVal, startVal, endVal, locationVal){
    let idObj = document.getElementById('day_id')
    idObj.value = idVal
    let dayObj = document.getElementById('day')
    let startObj = document.getElementById('start')
    let endObj = document.getElementById('end')
    let locationObj = document.getElementById('location')
    document.getElementById('scheduleDay_addBtn').value = 'Изменить день'
    document.getElementById('scheduleDay_addBtn').id = 'scheduleDay_UpdateBtn'
    let attrStr = '[data-scheduleDay-id="'+idVal+'"]'
    target = document.querySelector(attrStr)
    let all_td_ScheduleDay = target.children
        Array.from(all_td_ScheduleDay).forEach(elem => {
            if(elem.id == 'scheduleDayName'){
                dayObj.value = dayVal
            }
            if(elem.id == 'scheduleStart'){
                startObj.value = startVal
            }
            if(elem.id == 'scheduleEnd'){
                endObj.value = endVal
            }
            if(elem.id == 'scheduleLocation'){
                locationObj.value = locationVal
            }
        });  
}
async function showScheduleDay(id){
    await open_modal('Редактировать день', '/loadModalBlock_user/schedule');
    let url =  '/showScheduleDay/'+id
    console.log(url)
    fetch(url)
    .then(response => response.json())
    .then(data => {
        let day_id = data['id']
        let day = data['day']
        let start = data['start']
        let end = data['end']
        let location = data['location']   
        editModal_ScheduleDay(day_id, day, start, end, location)
    })
}
async function updateScheduleDay(){
    let day_id = document.getElementById('day_id')
    let location = document.getElementById('location')
    let day = document.getElementById('day')
    let start = document.getElementById('start')
    let end = document.getElementById('end')
    let scheduleDay = {
        'location' : location.value,  
        'day' : day.value,  
        'start' : start.value,  
        'end' : end.value
    }
    let url =  '/updateScheduleDay/'+day_id.value

    await fetch(url, { // отправляем запрос
        method: 'POST',
        headers: {
            'Content-Type': 'application/json;charset=utf-8'
        },
        body: JSON.stringify(scheduleDay)
    })
    .then(response => response.json()) // получаем ответ
    .then(data => {
        let id = data['id']
        let day = data['day']
        let start = data['start']
        let end = data['end']
        let location = data['location']  
        edit_scheduleDay(id, day, start, end, location) 
    })
}
function edit_scheduleDay(idVal, dayVal, startVal, endVal, locationVal){
    let attrStr = '[data-scheduleDay-id="'+idVal+'"]'
    target = document.querySelector(attrStr)
    let all_td_ScheduleDay = target.children
        Array.from(all_td_ScheduleDay).forEach(elem => {
            if(elem.id == 'scheduleDayName'){
                elem.innerHTML = dayVal
            }
            if(elem.id == 'scheduleStart'){
                elem.innerHTML = startVal
            }
            if(elem.id == 'scheduleEnd'){
                elem.innerHTML = endVal
            }
            if(elem.id == 'scheduleLocation'){
                elem.innerHTML = locationVal
            }
        });
        modal_base.classList.add('close_modal')
}
function createHTMLScheduleDay(idVal, dayVal, startVal, endVal, locationVal){
    let last_tr_ScheduleDay
    let all_tr_ScheduleDays = document.querySelectorAll('[data-scheduleDay-id]')
    if(all_tr_ScheduleDays.length === 0){
        empty_tr_ScheduleDays = document.getElementById('empty_schedule')
        last_tr_ScheduleDay = empty_tr_ScheduleDays
        clone_tr = empty_tr_ScheduleDays.cloneNode(true)
        clone_tr.removeAttribute('id')
        clone_tr.removeAttribute('class')
    }
    else{
        last_tr_ScheduleDay = Array.from(all_tr_ScheduleDays).at(-1)
        clone_tr = last_tr_ScheduleDay.cloneNode(true)
    }
    clone_tr.setAttribute('data-scheduleDay-id', idVal)
    let all_td_ScheduleDay = clone_tr.children
    Array.from(all_td_ScheduleDay).forEach(elem => {
        if(elem.id == 'scheduleDayName'){
            elem.textContent = dayVal
        }
        if(elem.id == 'scheduleStart'){
            elem.textContent = startVal
        }
        if(elem.id == 'scheduleEnd'){
            elem.textContent = endVal
        }
        if(elem.id == 'scheduleLocation'){
            elem.textContent = locationVal
        }
    });
    last_tr_ScheduleDay.insertAdjacentElement('afterend', clone_tr);
    modal_base.classList.add('close_modal')
}
async function createDataScheduleDay(){
    /*
    запрос на создание нового дня
    */
    let location = document.getElementById('location')
    let day = document.getElementById('day')
    let start = document.getElementById('start')
    let end = document.getElementById('end')
    let scheduleDay = {
        'location' : location.value,  
        'day' : day.value,  
        'start' : start.value,  
        'end' : end.value
    }
    await fetch('/createScheduleDay', { // отправляем новый день и получаем его в json
        method: 'POST',
        headers: {
            'Content-Type': 'application/json;charset=utf-8'
        },
        body: JSON.stringify(scheduleDay)
    })
    .then(response => response.json())
    .then(data => {
        let id = data['id']
        let day = data['day']
        let start = data['start']
        let end = data['end']
        let location = data['location']  
        createHTMLScheduleDay(id, day, start, end, location)
    }); 
}


