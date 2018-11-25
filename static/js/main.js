function fetchLearningDetail(id){
    $.ajax({
        url: "{% url 'fetch_learing_detail id=" + id + " %}",
        type: 'GET',
        cache: false,
        dataType: 'json',
        success: function(){
            alert(id)
        }
    })
}