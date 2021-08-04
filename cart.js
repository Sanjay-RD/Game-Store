const removeCartItem = (e) => {
  console.log("delete");

  // delete from local storage
  const cartRow = e.target.parentElement.parentElement;
  const titleElement = cartRow.querySelectorAll("th")[1].innerText;
  const cartValue = JSON.parse(localStorage.getItem("cartItems"));
  const result = cartValue.filter((item) => item.title !== titleElement);
  // console.log(result);
  localStorage.setItem("cartItems", JSON.stringify(result));
  // end
  // delete from ui
  let buttonClick = e.target;
  buttonClick.parentElement.parentElement.remove();
  // delete from ui end
  updateCartTotal();
};

// const quantityChange = (e) => {
// console.log("object" + typeof e.target.value);
// console.log(e.target.parentElement.parentElement);
// const cartRow = e.target.parentElement.parentElement;
// const titleElement =
//   cartRow.getElementsByClassName("col-md-3-cart")[0].innerText;
// console.log(titleElement);
// const cartValue = JSON.parse(localStorage.getItem("cartItems"));
// cartValue.forEach(function (item) {
//   if (item.title === titleElement) {
//     item.qty = parseInt(e.target.value);
//   }
// });
// localStorage.setItem("cartItems", JSON.stringify(cartValue));
// updateCartTotal();
// };

const eventHandler = () => {
  // for item change
  // let quantityInput = document.getElementsByClassName("cart-select");
  // console.log(quantityInput);
  // console.log(quantityInput.length);
  // for (let i = 0; i < quantityInput.length; i++) {
  //   const input = quantityInput[i];
  //   input.addEventListener("change", quantityChange);
  // }
  // item change end

  // delete btn
  const deleteBtn = document.querySelectorAll("#delete-btn");
  deleteBtn.forEach(function (btn) {
    btn.addEventListener("click", removeCartItem);
  });
  // delete btn end
};

window.onload = () => {
  const cartValue = JSON.parse(localStorage.getItem("cartItems"));
  const shoppingCartContent = document.getElementsByClassName(
    "shopping-cart-content"
  )[0];
  const checkOutBtn = document.getElementsByClassName("checkout-btn")[0];
  // display message if cart is empty
  if (cartValue.length === 0) {
    const cartEmpty = document.createElement("div");
    cartEmpty.className = "cart-empty";
    cartEmpty.innerText = "Your cart is empty";
    shoppingCartContent.appendChild(cartEmpty);
    checkOutBtn.setAttribute("disabled", true);
  }
  // end
  cartValue.forEach(function (item) {
    tableRow = document.createElement("tr");
    tableRow.className = "tr";
    cartTable = document.getElementById("cartTable");
    let cartRowContent = `
      <th>
        <img src="${item.imageSrc}" alt="" />
      </th>
      <th id="cart-title">
        <a href="">${item.title}</a>
      </th>
      <th>
        <span class="price">Rs. ${item.price}</span>
      </th>
      <th>
        <input
          type="text"
          class="cartItemForm"
          placeholder="1"
          disabled
        />
      </th>
      <th>
        <i class="fas fa-trash" id="delete-btn"></i>
      </th>
    `;
    tableRow.innerHTML = cartRowContent;
    cartTable.appendChild(tableRow);
  });

  updateCartTotal();
  eventHandler();
};

const updateCartTotal = () => {
  const cartRows = document.getElementsByClassName("tr");
  let total = 0;
  for (let i = 0; i <= cartRows.length - 1; i++) {
    const cartRow = cartRows[i];
    let priceElement = cartRow.getElementsByClassName("price")[0];
    // let quantityElement = cartRow.getElementsByClassName("cart-select")[0];
    let price = parseFloat(priceElement.innerText.replace("Rs.", ""));
    // let quantity = quantityElement.value;
    total = total + price * 1;
  }
  total = Math.round(total * 100) / 100;
  document.getElementsByClassName("totalPrice")[0].innerText = `Rs. ${total}`;
  const subtotal = document.getElementById("subtotal");
  subtotal.innerText = cartRows.length;
  // const cartValue = JSON.parse(localStorage.getItem("cartItems"));
  // let total = cartValue.reduce(function (a, b) {
  //   return a + b.price;
  // }, 0);
  // const totalPrice = document.getElementById("totalPrice");
  // totalPrice.innerText = `Rs. ${total}`;
};
