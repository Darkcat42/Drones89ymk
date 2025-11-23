let counter = 1
let input_files_obj = {}
let input_files_list = []
async function createGalleryEvent(){
    // let galleryEvent_files = document.getElementById('galleryEvent_files')
    // let images = galleryEvent_files.files
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
}

function galleryEventPreview_load(new_input_images){
    let images_modal_preview = document.getElementById('images_modal_preview')
    let img_container = document.getElementById('img_container')
    Array.from(new_input_images).forEach(input_img => {
        input_files_obj[input_img['name']] = input_img
        input_files_list.push(input_img)
        let new_img = img_container.cloneNode(true)
        new_img.querySelectorAll('p')[0].innerHTML = input_img['name']
        console.log(new_img.querySelectorAll('p'))
        new_img.removeAttribute('id')
        new_img.classList.remove('db_none')
        images_modal_preview.appendChild(new_img)
    });
}    
