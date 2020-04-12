//Перезагрузка страницы при изменение размера окна
var s_win_w = $(window).width();
$(window).resize(function () {
    win_w = $(window).width();
    if (win_w >= s_win_w * 1.3 || win_w <= s_win_w * 0.7) {
        location.reload();
    }
});

//Уменьшение шапки пи скроле вниз
$(window).scroll(function () {
    if ($(this).scrollTop() > 1 && $(window).width() > 769) {
        $('header').addClass("header-resize");
    } else {
        $('header').removeClass("header-resize");
    }
});

//Когда документ загружен
$(document).ready(function () {

    //анимация кнопки поиска
    $('.header-search-button').mouseenter(function () {
        $(this).css("transform", "rotate(180deg)");
    })
    $('.header-search-button').mouseleave(function () {
        $(this).css("transform", "rotate(360deg)");
    })

    //Двежение кнопки открывающей меню
    $('.menu-active').click(function () {
        if ($(window).width() < 500) {
            $('body').toggleClass('lock');
        }
        $(this).toggleClass('active');
        $('.main-menu').toggleClass('check');
        $('.content').toggleClass('resize');
        $('.header-buttons').toggleClass('buttons-active');
        $('.active-for-mobile').toggleClass('display-icons');
    })

    //Логика спойлеров 
    if ($(window).width() <= '769') {
        $('.spoilers').addClass('mobil');
    } else {
        $('.spoilers').removeClass('mobil');
    }

    $('.spoiler-active').click(function () {
        if ($('.spoilers').hasClass('mobil')) {
            $('.spoiler-active').not($(this)).removeClass('arrow-active');
            $('.spoiler-content').not($(this).next()).slideUp(300);
        }
        $(this).toggleClass('arrow-active').next().slideToggle(300);
    })

    //Переключение сетки товаров
    $('.grid').click(function () {
        $(this).toggleClass('active-grid');
        $('.main-product').toggleClass('change-grid');
    })


    //Слайдеры
    //Главный слайдер
    $('.slider').slick({
        dots: true, // активация точек
        speed: 1000, // время анимации
        autoplay: true, //автоматическое пролистывание
        autoplaySpeed: 2500, //скорость автоматического пролистывания
        pauseOnFocus: true, //Пауза при фокусе слайдера(нажатию куда либо)
        pauseOnHover: true, //Пауза при наведение на слайдер
        pauseOnDotsHover: true, //Пауза при наведение на точки
        responsive: [
            {
                breakpoint: 500,
                settings: {
                    dots: false
                }
            }
        ]
        //arrows:true, отображение стрелок
        //slidesToShow: 3, количество отображаемых слаййдов
        //slidesToScroll: 1, количество пролистываемых слайдов
        //easing: 'linear' тип анимации
        //infinite: false, бесконечное пролистывание
        //initialSlide: 2, начальный слайд
        //draggable: true,  //Свайп для ПК
        //swipe:true,  Свайп для телефонов
        //waitForAnimate:false,Ускоренноя прокрутка слайдов стрелками
        //rows: 1, //количество рядов
    });

    //Сладйер на странице товара
    $('.slider-min').slick({
        arrows: false, //отображение стрелок
        dots: false, // активация точек
        speed: 1000, // время анимации
        fade: true,
        autoplay: false, //автоматическое пролистывание
        autoplaySpeed: 2500, //скорость автоматического пролистывания
        pauseOnFocus: true, //Пауза при фокусе слайдера(нажатию куда либо)
        pauseOnHover: true, //Пауза при наведение на слайдер
        pauseOnDotsHover: true, //Пауза при наведение на точки
        asNavFor: ".sub-slider-min"
    });

    //Сладйер на странице товара вспомогательный
    $('.sub-slider-min').slick({
        arrows: true, //отображение стрелок
        dots: false, // активация точек
        //centerMode: true,
        slidesToShow: 3,
        speed: 1000, // время анимации
        autoplay: false, //автоматическое пролистывание
        autoplaySpeed: 2500, //скорость автоматического пролистывания
        pauseOnFocus: true, //Пауза при фокусе слайдера(нажатию куда либо)
        pauseOnHover: true, //Пауза при наведение на слайдер
        pauseOnDotsHover: true, //Пауза при наведение на точки
        infinite: true, //бесконечное пролистывание
        asNavFor: ".slider-min",
        focusOnSelect: true,
    });

});

//Добавление товаров в корзину
$(document).ready(function () {
    var form = $('#buyProduct');
    console.log(form);

    function basketUpdating(product_id, quantity_nbr, is_delete) {
        var data = {};
        data.product_id = product_id;
        data.quantity_nbr = quantity_nbr;
        var csrf_token = $('#buyProduct [name="csrfmiddlewaretoken"]').val();
        data["csrfmiddlewaretoken"] = csrf_token;

        if (is_delete) {
            data["is_delete"] = true;
        }

        var url = form.attr('action');
        $.ajax({
            url: url,
            type: 'POST',
            data: data,
            cache: true,
            success: function (data) {
                console.log('OK')
                if (data.product_total_quantity_nbr || data.product_total_quantity_nbr == 0) {
                    $('.shopping .counter').text(data.product_total_quantity_nbr);
                    
                    $('.shopping-list-container').html(" ");
                    $.each(data.products, function (k, v) {
                        
                        $('.shopping-list-container').
                        append('<tr class="shopping-item"><td>' + v.product_title + '</td><td>' + v.quantity_nbr + 'шт.</td><td>' + v.product_price + '</td><td class="shopping-list-delete" data-product_id="' + v.id + '" title="Удалить товар"></td></tr>');
                    })
                }
            },
            error: function () {
                console.log('error')
            }
        })
    }

    form.on('submit', function (e) {
        //Запретить добавить товар в корзину если товара нет на складе
        if ($('.warehouse').text() == 0) {
            e.preventDefault();
            $('.alert-title').text('Товаров нет на складе');
            $('.alert').css('display', 'block');
            console.log('Товаров нет на складе');
        }
        //Запретить добавить товар в корзину если указан 0 или больше чем есть в наличии
        else if ($('.detail-quantity input').val() == 0 || $('.detail-quantity input').val() >= $('.warehouse').text() )  {
            e.preventDefault();
            $('.alert-title').text('Указано не правильное количество');
            $('.alert').css('display', 'block');
            console.log('Указано не правильное количество');
        } else {
            e.preventDefault(); //Отменить стандартное поведение
            var quantity_nbr = $('#quantity_nbr').val(); //Получить количество товара которого хотят купить
            var addBasket = $('#addBasket'); //Получение кнопки отправки формы для считывания с неё data атрибутов
            var product_id = addBasket.data('product-id'); //Получение id продукта в бд
            var product_title = addBasket.data('product-title'); //Получение названия продукта
            var product_price = addBasket.data('product-price'); //Получение цены продукта

            basketUpdating(product_id, quantity_nbr, is_delete = false);
        }
    })

    //Удаление товаров из коризы
    $(document).on('click', '.shopping-list-delete', function (e) {
        e.preventDefault();
        product_id = $(this).data("product_id");
        quantity_nbr = 0;
        basketUpdating(product_id, quantity_nbr, is_delete = true);
    })









    //Уведомление о том что товаров в корзине нет
    $('.add-order').click(function () {
        if ($('.shopping-list-container tr').hasClass('shopping-item')) {
            console.log('Товар в коризне');
        } else {
            console.log('Товар в коризне нет');
            $('.alert-title').text('Товаров в корзине нет');
            $('.alert').css('display', 'block');
        }
    })
    $('.alert-button').click(function () {
        $('.alert').css('display', 'none');
        $('.alert-title').text(' Всплыващие окно ');
    })



    //просмотр картинки товара в полном экране
    $('.slider item').click(function () {
        $(this).nect($()).clone() // сделаем копию картинки на которую было нажато
            .addClass("active-slider-img") // добавим этой копии класс активации
            .appendTo(".product-big"); // вставим измененный элемент в элемент для просмотра
        $("body").addClass("lock");
        $(".product-big").addClass("active-product-big");
    })
    $('.product-big-close').click(function () {
        $(".product-big").closest('.slider-img').remove();
        $("body").removeClass("lock");
        $(".product-big").removeClass("active-product-big");
    })
});

//Геренация случайного цвета подсветки
var colors = ['#FF283F',
              'rgba(233, 33, 243, 1)',
              'rgba(25, 212, 247, 1)'];
randomColor = colors[Math.random() * colors.length ^ 0];
document.documentElement.style.setProperty('--red', randomColor);