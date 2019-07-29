var likes = 0
var currentUser = "Jack"

var usersLiked = []

let button = document.querySelector("#like_button");
let likesLabel = document.querySelector("#numLikesLabel");

button.addEventListener("click", () => {
  for (i = 0; i < usersLiked.length; i++) {
    if (usersLiked[i] === currentUser){
      likes--;
      button.innerHTML = "Like";
      delete usersLiked[i];
      likesLabel.innerHTML = "0 Likes";
      button.style.background = "#4050dd";
      button.style.border = "1px solid #4050dd";
      return;
    }
  }

  likes++;
  usersLiked.push(currentUser);
  button.innerHTML = "Unlike"
  likesLabel.innerHTML = likes + " like";
  button.style.background = "#ff0000";
  button.style.border = "1px solid #ff0000";
});

const changeHeaderColor = () => {
  likesLabel.style.color = "#ff0000"
}

likesLabel.addEventListener("click", changeHeaderColor)
