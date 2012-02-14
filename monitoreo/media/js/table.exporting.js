function exportarXLS(id){
	var foo = $('#'+id).html();
	var csrf_token =  $.cookie('csrftoken');

	var form = $('<form>').attr({
	    type: 'hidden',
	    method: 'POST',
	    action: '/xls/',
	    id: 'formxls'
	}).appendTo('body');

	$('<input>').attr({type: 'hidden', name: 'tabla',  value: foo}).appendTo(form);
	$('<input>').attr({type: 'hidden', name: 'csrfmiddlewaretoken',  value: csrf_token}).appendTo(form);

	$(form).submit();
}
