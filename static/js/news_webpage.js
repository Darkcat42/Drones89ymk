async function createNews() {
    let news_file = document.getElementById('news_file')
    let image1 = news_file.files[0]
    let image2 = news_file.files[1]
    let news_title = document.getElementById('news_title')
    let title = news_title.value
    let news_text = document.getElementById('news_text')
    let text = news_text.textContent
    news_data = {
        'title' : title,
        'text' : text
    }
    let url = 'createNews'
    let formData = new FormData()
    formData.append('file1', image1)
    formData.append('file2', image2)
    formData.append('json', news_data)
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
        add_HTMLnews(news_id, title, text, image_src)
    })
}
function add_HTMLnews(idVal, titleVal, textVal, imageSrc){
    // тут будем динамически вставлять новую новость
    alert('затычка, доделать вставку новости после создания')
}