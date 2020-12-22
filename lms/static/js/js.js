function noempty() {
    var x = document.forms["forsearch"]["q"].value;
    if (x == "" || x == null) {
      alert("Please enter something to search");
      return false;
    }
  }