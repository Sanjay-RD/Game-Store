const addToCartElement = document.getElementsByClassName("add-to-cart-btn");
const addToLocalStorageClicked = (e) => {
  const button = e.target;
  const shopItem =
    button.parentElement.parentElement.parentElement.parentElement.parentElement
      .parentElement;
  const title = shopItem.getElementsByClassName("game-title")[0].innerText;
  const price = parseFloat(
    shopItem.getElementsByClassName("price")[0].innerText.replace("Rs.", "")
  );
  const imageSrc = shopItem.getElementsByClassName("game-image")[0].src;

  console.log(title, price, imageSrc);
  addItemToCart(title, price, imageSrc);
};

let cartArr = [];

let getCartItems = JSON.parse(localStorage.getItem("cartItems"));
console.log(getCartItems);
if (getCartItems) {
  for (let i = 0; i < getCartItems.length; i++) {
    cartArr.push(getCartItems[i]);
  }
}

function addItemToCart(title, price, imageSrc) {
  let cartData = {
    title: title,
    price: price,
    imageSrc: imageSrc,
  };

  const exitItem = cartArr.find((item) => item.title === title);
  console.log(exitItem);

  if (exitItem) {
    if (exitItem.title === title) {
      alert(`${title} is already in your cart!`);
    }
  } else {
    // display message to ui
    const cartMessageContainer = document.createElement("div");
    const cartMessage = document.createElement("p");
    cartMessageContainer.className = "cart-message-container";
    cartMessage.className = "cart-message";
    const body = document.querySelector("body");
    cartMessage.innerText = "Added to cart";
    cartMessageContainer.appendChild(cartMessage);
    body.appendChild(cartMessageContainer);
    setTimeout(() => {
      cartMessageContainer.remove();
    }, 2000);
    // end
    cartArr.push(cartData);
    localStorage.setItem("cartItems", JSON.stringify(cartArr));
  }
}

for (let i = 0; i < addToCartElement.length; i++) {
  const button = addToCartElement[i];
  button.addEventListener("click", addToLocalStorageClicked);
}
