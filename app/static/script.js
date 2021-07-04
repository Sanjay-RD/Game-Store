let menuItems = document.getElementById("menuItems");
let menuClick = document.getElementById("menuClick");

menuItems.style.maxHeight = "0px";

menuClick.addEventListener("click", () => {
  if (menuItems.style.maxHeight == "0px") {
    menuItems.style.maxHeight = "200px";
  } else {
    menuItems.style.maxHeight = "0px";
  }
});

let productImg = document.getElementById("ProductImg");
let smallImg = document.getElementsByClassName("small-img");

// console.log(smallImg)

for (let i = 0; i < smallImg.length; i++) {
  smallImg[i].addEventListener("click", function () {
    productImg.src = smallImg[i].src;
  });
}

let LoginForm = document.getElementById("LoginForm");
let RegForm = document.getElementById("RegForm");
let Indicator = document.getElementById("Indicator");
let login = document.getElementById("login");
let register = document.getElementById("register");
login.addEventListener("click", () => {
  RegForm.style.transform = "translateX(300px)";
  LoginForm.style.transform = "translateX(300px)";
  Indicator.style.transform = "translateX(0px)";
});

register.addEventListener("click", () => {
  RegForm.style.transform = "translateX(0px)";
  LoginForm.style.transform = "translateX(0px)";
  Indicator.style.transform = "translateX(100px)";
});

setTimeout(() => {
  $("#message").fadeOut("slow");
}, 3000);
