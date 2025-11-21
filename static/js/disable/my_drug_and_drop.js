let draggedItem = null; // переменная для временной записи объекта который мы тащим курсором
document.addEventListener('dragstart', (e) => {
    console.log(draggedItem)
    console.log(e.target)
    /*
    общий прослушиватель старта события drag_and_drop
    */
    if (e.target.getAttribute('draggable')){
        draggedItem = e.target;
        draggedItem.classList.add('dragstart');
        draggedItem.parentNode.classList.add('drug_select');
        }
         });
document.addEventListener('dragover', (e) => {
    /*
    общий прослушиватель события drag_and_drop - "над целью"
    */
    e.preventDefault();});
document.addEventListener('dragenter', (e) => {
    /*
    общий прослушиватель события drag_and_drop - "зашел в границы цели" 
    */
    e.preventDefault();});
document.addEventListener('dragleave', (e) => {
    /*
    общий прослушиватель старта события drag_and_drop "вышел из границ цели" 
    */
    e.preventDefault();});
document.addEventListener('drop', (e) => {
    /*
    общий прослушиватель старта события drag_and_drop 
    - "пользователь отпустил цель из лап мыши" 
    */
    e.preventDefault();
    e.target.classList.remove('dragover')
    let target_container = e.target.parentNode.parentNode; 
    let allItems = Array.from(target_container.children);
    let targetIndex = allItems.indexOf(e.target.parentNode); // индекс под
    let draggedIndex = allItems.indexOf(draggedItem); // индекс в руках
    // (targetIndex, draggedIndex) // цель тут это то что под курсором!
    console.log(target_container)
            console.log(draggedItem.parentNode)
    if(target_container == draggedItem.parentNode){

            if (draggedIndex < targetIndex) // тащим слева на право 0 < 1  
                target_container.insertBefore(draggedItem, e.target.parentNode.nextSibling);
            else if(draggedIndex > targetIndex){
                target_container.insertBefore(draggedItem, e.target.parentNode);}
                e.target.parentNode.classList.remove('drug_item_enter')
    }else{
        alert('неверная цель для перемещения')
    }
    });
document.addEventListener('dragend', (e) => {
    /*
    общий прослушиватель старта события drag_and_drop
    - конец события перетаскивания
    */
    if (e.target.getAttribute('draggable')){
        draggedItem = e.target;
        draggedItem.classList.remove('dragstart');
        draggedItem.parentNode.classList.remove('drug_select');}});