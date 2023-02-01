var footer = document.getElementById('footer')
window.onscroll = function(){
    if(window.pageXOffset > 100){
        footer.style.position='fixed';
        footer.style.top = 100;
    }else{
        footer.style.position='relative';
        footer.style.top = 0;
    }
}