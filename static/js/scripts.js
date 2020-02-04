// function on() {
//     document.getElementById("overlay").style.display = "block";
//   }
  
//   function off() {
//     document.getElementById("overlay").style.display = "none";
//   }
function myFunction() {
  alert("Test scripts");
}


  $(document).ready(function(){
      $("#overlay").mouseenter(function(){
          $("#text").show("slow");
      })
      .mouseleave(function(){
          $("#text").hide("slow");
      });
  })