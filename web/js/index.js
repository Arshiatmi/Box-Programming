$(document).ready(function () {
  // _. {Start} display the inspector after clicking on the arrow-inspector button ._
  $(".box-inspector").hide();
  $(".arrow-inspector").click(function () {
    $(".inspector").toggleClass("active-inspector");
    $(".box-inspector").animate({
      width: "toggle",
    });
  });
  // _. {End} display the inspector after clicking on the arrow-inspector button ._
});
