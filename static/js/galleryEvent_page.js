//let counter = 0
let input_files_obj = {}
let input_files_list = []
async function createGalleryEvent(){
    let images = input_files_list
    let galleryEvent_title = document.getElementById('galleryEvent_title')
    let galleryEvent_date = document.getElementById('galleryEvent_date')
    let formData = new FormData()
    for(let image_file of images){
        formData.append('files', image_file)
    }
    formData.append('title', galleryEvent_title.value)
    formData.append('date', galleryEvent_date.value)
    let url = 'addGalleryEvent'
    await fetch(url, {
        method: 'POST',
        body: formData
    })
    // .then(response => response.json()) // получаем ответ
    // .then(data => {
    //     let title = data['title']
    //     let date = data['date']
    //     let images = data['images']
    // })
    window.location.reload()
}
function MakeCounter(){
    var count = 0
    return () => {
        return count = count + 1}
}
let counter = MakeCounter()
function galleryEventPreview_load(new_input_images){
    let images_modal_preview = document.getElementById('images_modal_preview')
    let img_container = document.getElementById('img_container')
    Array.from(new_input_images).forEach(input_img => {
        input_files_obj[input_img['name']] = input_img
        input_files_list.push(input_img)
        let new_img = img_container.cloneNode(true)
        new_img.querySelectorAll('p')[0].innerHTML = input_img['name']
        new_img.querySelectorAll('p')[0].id = 'img_filename'+counter()
        new_img.removeAttribute('id')
        new_img.classList.remove('db_none')
        images_modal_preview.appendChild(new_img)
    });
}
function galleryEventImg_deLInput(target){
    target.parentNode.classList.add('db_none')
    let index = input_files_list.indexOf(input_files_obj[target.parentNode.querySelector('p').textContent])
    input_files_list.splice(index, 1)

}
// function createHTMLgalleryEvent(titleVal, dateVal, imagesList){
//     let last_tr_ScheduleDay
//     let all_tr_ScheduleDays = document.querySelectorAll('[data-scheduleDay-id]')
//     if(all_tr_ScheduleDays.length === 0){
//         empty_tr_ScheduleDays = document.getElementById('empty_schedule')
//         last_tr_ScheduleDay = empty_tr_ScheduleDays
//         clone_tr = empty_tr_ScheduleDays.cloneNode(true)
//         clone_tr.removeAttribute('id')
//         clone_tr.removeAttribute('class')
//     }
//     else{
//         last_tr_ScheduleDay = Array.from(all_tr_ScheduleDays).at(-1)
//         clone_tr = last_tr_ScheduleDay.cloneNode(true)
//     }
//     clone_tr.setAttribute('data-scheduleDay-id', idVal)
//     let all_td_ScheduleDay = clone_tr.children
//     Array.from(all_td_ScheduleDay).forEach(elem => {
//         if(elem.id == 'scheduleDayName'){
//             elem.textContent = dayVal
//         }
//         if(elem.id == 'scheduleStart'){
//             elem.textContent = startVal
//         }
//         if(elem.id == 'scheduleEnd'){
//             elem.textContent = endVal
//         }
//         if(elem.id == 'scheduleLocation'){
//             elem.textContent = locationVal
//         }
//     });
//     last_tr_ScheduleDay.insertAdjacentElement('afterend', clone_tr);
//     modal_base.classList.add('close_modal')
// }

// function edit_scheduleDay(idVal, dayVal, startVal, endVal, locationVal){
//     let attrStr = '[data-scheduleDay-id="'+idVal+'"]'
//     target = document.querySelector(attrStr)
//     let all_td_ScheduleDay = target.children
//         Array.from(all_td_ScheduleDay).forEach(elem => {
//             if(elem.id == 'scheduleDayName'){
//                 elem.innerHTML = dayVal
//             }
//             if(elem.id == 'scheduleStart'){
//                 elem.innerHTML = startVal
//             }
//             if(elem.id == 'scheduleEnd'){
//                 elem.innerHTML = endVal
//             }
//             if(elem.id == 'scheduleLocation'){
//                 elem.innerHTML = locationVal
//             }
//         });
//         modal_base.classList.add('close_modal')
// }
