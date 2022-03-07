import $ from "jquery";
document.write(12);
$.ajax(
   {
      type: "POST",
      url: "./main.py",
      data: 
      {
   
      }
   }
   ).done(function( ) 
   {
      console.log(data);
   });

// var script = document.createElement('script');
// script.src = 'https://code.jquery.com/jquery-3.4.1.min.js';
// script.type = 'text/javascript';
// document.getElementsByTagName('head')[0].appendChild(script);

