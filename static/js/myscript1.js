// Перемещает значок телеграмма вниз
let f = document.getElementById('form');
let c = document.getElementById('content');
function poll() {
    f.style.display = 'block';
    c.style.display = 'none';
    if (window.width() < 950) {
        f.style.marginBottom = '30px'
    }
}
// Перемещает значок телеграмма вниз


// start__Фиксируется шапка при скролле
window.addEventListener('scroll', function () {
    let head = document.getElementById('header');
    if (window.scrollY > 0) {
        head.style.boxShadow = '0 5px 20px -5px rgba(255,255,255,0.5)';
        head.style.position = 'sticky';
        head.style.top = '0';
        head.style.backgroundColor = '#31123C'
        head.style.zIndex = '4000'
    } else {
        head.style.boxShadow = 'none';
        head.style.position = 'static';
        head.style.top = '0';
    }
});
// end__Фиксируется шапка при скролле



// Раскрываем фото с тенью позади при нажатии
function LinkFull(link) {
    let ref = link;
    let elModal = document.getElementById('linkJsImg')
    elModal.innerHTML = '<img src="' + ref + '" class="img-fluid img_diplom js_img_ful" >'
}
// Раскрываем фото с тенью позади при нажатии



// Кнопка наверх
let mybutton = document.getElementById("btn-back-to-top");

window.onscroll = function () {
    scrollFunction();
};

function scrollFunction() {
    if (
        document.body.scrollTop > 20 ||
        document.documentElement.scrollTop > 20
    ) {
        mybutton.style.display = "block";
    } else {
        mybutton.style.display = "none";
    }
}

mybutton.addEventListener("click", backToTop);
// Кнопка наверх


// Навигация для мобильной версии
function backToTop() {
    document.body.scrollTop = 0;
    document.documentElement.scrollTop = 0;
}

function HeaderFull() {
    if(/iPhone|iPad|iPod|Android/i.test(navigator.userAgent)){
        let head = document.getElementById('header');
        let close = document.getElementById('img_close');
        let closeB = document.getElementById('bg_close')
        if (head.style.height == '100vh') {
            head.style.height = 'auto';
            close.style.display = 'none';
            closeB.style.display = 'block';
        } else {
            head.style.height = '100vh';
            close.style.display = 'block';
            closeB.style.display = 'none';
        }
    }
}

// function RemoveCol() {
//     if(/iPhone|iPad|iPod|Android/i.test(navigator.userAgent)){
//         let el = document.getElementById('navbarNavAltMarkup');
//         el.classList.remove('show');
//         HeaderFull()
//     }   
// }
// Навигация для мобильной версии



// Подгружаем картинки быстрее
document.addEventListener("DOMContentLoaded", function() {
    var lazyloadImages = document.querySelectorAll("img.lazy");    
    var lazyloadThrottleTimeout;
    
    function lazyload () {
      if(lazyloadThrottleTimeout) {
        clearTimeout(lazyloadThrottleTimeout);
      }    
      
      lazyloadThrottleTimeout = setTimeout(function() {
          var scrollTop = window.pageYOffset;
          lazyloadImages.forEach(function(img) {
              if(img.offsetTop < (window.innerHeight + scrollTop)) {
                img.src = img.dataset.src;
                img.classList.remove('lazy');
              }
          });
          if(lazyloadImages.length == 0) { 
            document.removeEventListener("scroll", lazyload);
            window.removeEventListener("resize", lazyload);
            window.removeEventListener("orientationChange", lazyload);
          }
      }, 20);
    }
    
    document.addEventListener("scroll", lazyload);
    window.addEventListener("resize", lazyload);
    window.addEventListener("orientationChange", lazyload);
  });
  // Подгружаем картинки быстрее



const formElement = document.getElementById('formsol'); // извлекаем элемент формы
formElement.addEventListener('submit', (e) => {
    const Arr = ["rap1", "rap2", "rap3", "rap4"];
    for (let i = 0; i <= 3; ++i) {
        const kick = document.getElementById(Arr[i])
        kick.style.display = 'none'
    }

  e.preventDefault();
  let formData = new FormData(formElement); // создаём объект FormData, передаём в него элемент формы
  let formWeight = formData.get('weight'); // получаем вес
  let formArea = formData.get('area'); // получаем область применения
  if (formWeight >= 30000) {
     let photoRz = document.getElementsByClassName('photo_rz_cards');
    console.log(photoRz)
     photoRz[0].innerHTML = "<p>К сожалению мы пока не умеем расчитывать правовое регулирование на БПЛА свыше 30кг </p>"
  }
  if ((formWeight <= 150) && (formArea == 'Вне населенного пункта' || formArea == 'В населенном пункте' || formArea == 'Вблизи аэродрома')) {
    let el = document.getElementById('rap1')
    el.style.display = 'block'
  }
  if (formWeight > 150 && formWeight <= 30000 && formArea == 'Вне населенного пункта') {
    let el = document.getElementById('rap2')
    el.style.display = 'block'
  }
  if (formWeight > 150 && formWeight <= 30000 && formArea == 'В населенном пункте') {
    let el = document.getElementById('rap3')
    el.style.display = 'block'
  }
  if (formWeight > 150 && formWeight <= 30000 && formArea == 'Вблизи аэродрома') {
    let el = document.getElementById('rap4')
    el.style.display = 'block'
  }
  
});
