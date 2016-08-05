$("#addButton").click(onButtonClick);

function onButtonClick(event){
  event.preventDefault();
  var todoText = $("#item").val();
  var listItem = $("<li>" + todoText + "</li>");
  $("ul").append(listItem);
}
