let products = [
  {id: 1,name: "Laptop", price:50000},
  {id: 2,name: "Phone", price:20000},
  {id: 3,name: "Headphones", price:2000},
];
let cart = JSON.parse(localStorage.getItem("cart"))||[];

if(document.getElementById("product-list")){
  let container = document.getElementById("product-list");

  products.forEach(product=>{
    let div = document.createElement("div");
    div.className = "card";
  
  div.innerHTML = `
  <h3>${product.name}</h3>
  <p>₹${product.price}</p>
  <button onclick="addToCart(${product.id}">Add to Cart</button>`;

  container.appendChild(div);
});
}
