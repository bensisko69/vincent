var error = false;

$(document).on('click', '.openModalRegister', function()
{
	$('#modal-register').modal('show');
});	

$(document).on('click', '.submit-form', function()
{
	//$('#form_register').submit();
		console.log('click');
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