var error = false;

var csrftoken = getCookie('csrftoken');

function getCookie(name) 
{
    var cookieValue = null;
    if (document.cookie && document.cookie != '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = jQuery.trim(cookies[i]);
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) == (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

$.ajaxSetup({   headers: {  "X-CSRFToken": csrftoken  }  });

$(document).on('click', '.openModalRegister', function()
{
	$('#modal-register').modal('show');
});	

$(document).on('click', '.submit-form', function()
{
	$.ajax({
	   type: "POST",
	   url: "account",
	   dataType: "json",
	   traditional: true,
	   data: {'firstname': $('#id_firstname')},
	   success: function(success) 
	   {

	   }
	});
});

if (error == 'True')
{
	$('#modal-register').modal('show');
};