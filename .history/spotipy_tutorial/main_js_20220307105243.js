src="http://ajax.googleapis.com/ajax/libs/jquery/1.11.1/jquery.min.js"


$.ajax({
    type: "POST",
    url: "./main.py",
    data: {

    }
  }).done(function( ) {
     console.log(data);
  });