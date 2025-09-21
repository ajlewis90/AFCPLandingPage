$(document).ready(function() {
	$("#business-signup-form").submit(function(e) {
		// prevent from normal form behaviour
		e.preventDefault();
		// serialize the form data
		var serializedData = $(this).serialize();
		$.ajax({
			type : 'POST',
			url : "/add-business-contact/",
			data : serializedData,
			success : function(response) {
				console.log(response.message);
				$('.signup-success-response').html(response.message);
				setTimeout(function() {
					$('.signup-success-response').fadeOut().empty();
				}, 7000);
				// reset the form after successful submit
				$("#business-signup-form")[0].reset();
				if (response.redirect_url) {
					window.location = response.redirect_url;
				}
			},
			error : function(response) {
				console.log(response.message);
				$('.signup-error-response').html(response.message);
				setTimeout(function() {
					$('.signup-error-response').fadeOut().empty();
				}, 700);
			}
		});
	});
});