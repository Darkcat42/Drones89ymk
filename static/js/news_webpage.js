async function createNews() {
    let news_file = document.getElementById('news_file')
    let image = news_file.files[0]
    let news_title = document.getElementById('news_title')
    let title = news_title.value
    let news_text = document.getElementById('news_text')
    let text = news_text.value
    let url = 'createNews'
    let formData = new FormData()
    formData.append('file', image)
    formData.append('title', title)
    formData.append('text', text)
    responce = await fetch(url, { // отправляем запрос
        method: 'POST',
        body: formData
    })
    .then(response => response.json()) // получаем ответ
    .then(data => {
        let news_id = data['id']
        let title = data['title']
        let text = data['text']
        let image_src = data['image_src']
        news_insert_html(news_id, title, text, image_src)
    })
}
function news_insert_html(idVal, titleVal, textVal, imageSrc){
    // тут будем динамически вставлять новую новость
    alert('затычка, доделать вставку новости после создания')
}