function getAbout(){
    $.ajax({
        url: '/accounts/get_about',
        type: 'POST',
        data: data,
        cache: false,
        dataType: 'json',
        success: function(resp){
            alert('hello')
        }
    })
}