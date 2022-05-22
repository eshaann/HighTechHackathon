
function submit(event) {
  temp = document.getElementById("firstForm")
  window.location.replace("./resultsViewer.html?Hashtag_Choice=" + temp.value);
  event.preventDefault();
}
