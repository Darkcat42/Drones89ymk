// async function createNewNews() {
//     let news_file = document.getElementById('news_file')
//     let image = news_file.files[0]
//     let news_title = document.getElementById('news_title')
//     let title = news_title.value
//     let news_text = document.getElementById('news_text')
//     let text = news_text.value
//     let url = 'createNews'
//     let formData = new FormData()
//     formData.append('file', image)
//     formData.append('title', title)
//     formData.append('text', text)
//     responce = await fetch(url, { // отправляем запрос
//         method: 'POST',
//         body: formData
//     })
//     window.location.reload()
// }

// function del_news(id){
//     url = '/deleteScheduleDay/'+id
//     let response = fetch(url)
//     .then(response => response.text())
//     .then(html => {
//         elem = document.querySelector('[data-scheduleDay-id="'+html+'"]')
//         elem.remove()
//     })
//  } 
