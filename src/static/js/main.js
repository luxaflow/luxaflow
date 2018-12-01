$(document).ready(function () {
    $('.carousel').carousel({
        indicators: true,
        fullWidth: true,
        startingTop: '0%'
    });

    $('.modal').modal({
        prevenScrolling: false,
        dismissible: false,
        inDuration: 500
    });
    
});

function getPostContent(id) {
    $.ajax({
        url: '/posts/detail/' + id,
        dataType: 'json',
        success: function (result) {
            post = JSON.parse(result);
            $('#post-content-title').html(post[0].fields.name);
            $('#post-content-body').html(post[0].fields.body);
        }
    })
}

function getPostModalContent(id) {
    $.ajax({
        url: '/posts/detail/' + id,
        dataType: 'json',
        success: function (result) {
            post = JSON.parse(result);
            $('#post-modal-title').html(post[0].fields.name);
            $('#post-modal-body').html(post[0].fields.body);
        }
    })
}

function getProjectContent(id) {
    $.ajax({
        url: '/projects/detail/' + id,
        dataType: 'json',
        success: function (result) {
            project = JSON.parse(result);
            $('#project-content-title').html(project[0].fields.name);
            $('#project-content-body').html(project[0].fields.description);
        }
    })
}

function getContent(dataType, id) {
    $.ajax({
        url: '/about/'+ dataType +'/detail/' + id,
        dataType: 'json',
        success: function (result) {
            content = JSON.parse(result);
            $('#about-content-title').html(content[0].fields.name);
            $('#about-content-body').html(content[0].fields.description);
        }
    })
}

function getModalContent(dataType, id) {
    $.ajax({
        url: '/about/' + dataType + '/detail/' + id,
        dataType: 'json',
        success: function (result) {
            content = JSON.parse(result);
            $('#about-modal-title').html(content[0].fields.name);
            $('#about-modal-body').html(content[0].fields.description);
        }
    })
}
