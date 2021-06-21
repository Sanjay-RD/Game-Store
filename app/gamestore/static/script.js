let menuItems = document.getElementById("menuItems")
let menuClick = document.getElementById("menuClick");

menuItems.style.maxHeight = "0px"

menuClick.addEventListener('click',()=>{
    if (menuItems.style.maxHeight == "0px") {
      menuItems.style.maxHeight = "200px";
    } else {
      menuItems.style.maxHeight = "0px";
    }
})


let productImg = document.getElementById("ProductImg");
let smallImg = document.getElementsByClassName("small-img");

// console.log(smallImg)

for(let i=0;i<smallImg.length;i++){
  smallImg[i].addEventListener('click',function(){
    productImg.src = smallImg[i].src
  })
}