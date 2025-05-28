document.onscroll = () => {
    if(window.scrolly > 0 ) {
        docoument.querySelector('.header').classlist.add('active');
    } else {
        document.querySelector('.header').classlist.remove('active');
    }
};
document.onscroll = () => {
    document.querySelector('.menu').classlist.toggle('active');
    document.querySelector('.nav').classlist.toggle('active');
};