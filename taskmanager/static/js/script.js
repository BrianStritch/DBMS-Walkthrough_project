 /**
  * 
 the first eventlistener is for the sidenav functionality
 **/
 
 document.addEventListener('DOMContentLoaded', function() {
     // sidenav initialisation
    let sidenav = document.querySelectorAll('.sidenav');
    M.Sidenav.init(sidenav);
    // this is added in from function below to initialize datepicker
    let datepicker = document.querySelectorAll('.datepicker');
    M.Datepicker.init(datepicker, {
      format: "dd mmmm, yyyy", // this format gives eg: 1 febuary, 2024   - taken from materialize website
      i18n:{done: "Select"}    
      }); 
    
    // this is added in from function below to initialize dropdown
    let selects = document.querySelectorAll('select');
    M.FormSelect.init(selects);

    // this is added from function below to initialize the collapsible in tasks.html
    let collapsibles = document.querySelectorAll('.collapsible');
    M.Collapsible.init(collapsibles);

  });

  // Or with jQuery

//   $(document).ready(function(){
//     $('.sidenav').sidenav();
//   });


// this is from stage 8 initializing the datepicker in tasks form

// document.addEventListener('DOMContentLoaded', function() {
//   var elems = document.querySelectorAll('.datepicker');
//   var instances = M.Datepicker.init(elems, options);
// });

  // Or with jQuery

  // $(document).ready(function(){
  //   $('.datepicker').datepicker();
  // });


 // this is from stage 8 initializing the dropdown menu in tasks form  
  // document.addEventListener('DOMContentLoaded', function() {
  //   var elems = document.querySelectorAll('select');
  //   var instances = M.FormSelect.init(elems, options);
  // });

  // // Or with jQuery

  // $(document).ready(function(){
  //   $('select').formSelect();
  // });

// // this is the code block to initialize the collapsible
//   document.addEventListener('DOMContentLoaded', function() {
//     var elems = document.querySelectorAll('.collapsible');
//     var instances = M.Collapsible.init(elems, options);
//   });

//   // Or with jQuery

//   $(document).ready(function(){
//     $('.collapsible').collapsible();
//   });