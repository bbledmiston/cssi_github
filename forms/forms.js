$("button").click(printEmail);

function printEmail(event) {
  event.preventDefault(); //Otherwise, page will refresh
  var email = $("#email");
  console.log(email.val());
}
