$.ajax({
  url: 'https://hellosalut.stefanbohacek.dev/?lang=fr',
  type: 'GET',
  dataType: 'json'
}
).done((data) => {
  $('DIV#hello').text(data.hello);
});
