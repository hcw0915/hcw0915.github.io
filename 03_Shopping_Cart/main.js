

let shopItemsData = [{
  id:"1",
  name:"asd",
  price: 45,
  desc:"Lorem ipsum dolor sit amet consectetur adipisicing elit.",
  img:"https://picsum.photos/200/200"
},{
  id:"2",
  name:"wer",
  price: 100,
  desc:"Lorem ipsum dolor sit amet consectetur adipisicing elit.",
  img:"https://picsum.photos/200/200"
},{
  id:"3",
  name:"sdf",
  price: 130,
  desc:"Lorem ipsum dolor sit amet consectetur adipisicing elit.",
  img:"https://picsum.photos/200/200"
},{
  id:"4",
  name:"xcv",
  price: 70,
  desc:"Lorem ipsum dolor sit amet consectetur adipisicing elit.",
  img:"https://picsum.photos/200/200"
}]


let shop = document.getElementById('shop')
let generateShop = () => {
  return (shop.innerHTML = shopItemsData.map( (x) => {
    let {id,name,price,desc,img} = x
    return `  
    <div id="product-id-${id}" class="item">
      <img width="220" src=${img} alt="">
      <div class="details">
        <h3>${name}</h3>
        <p>${desc}</p>
        <div class="price-quantity">
          <h2>$ ${price}</h2>
          <div class="buttons">
            <i id="decrement" onclick="decrement(${id})" class="bi bi-dash-lg bi-b"></i>
            <div id="${id}" class="quantity">0</div>
            <i id="increment" onclick="increment(${id})" class="bi bi-plus-lg bi-b"></i>
          </div>
        </div>
      </div>
    </div>`
  }).join(''))
}

generateShop()



const updateElement = document.getElementById('update')


let basket = []
let increment = (id) => {
  let search = basket.find((x)=> x.id === id)
  if (search === undefined) {
    basket.push({
      id:id,
      item:1
    })
  }else{
    search.item += 1
  }
  localStorage.getItem("data",JSON.stringify (basket))
  // console.log(basket);
  update(id)
}

const decrement = (id) => {
  let search = basket.find((x)=> x.id === id)
  if (search.item === 0) { return
  }else{
    search.item -= 1
  }
  localStorage.getItem("data",JSON.stringify (basket))
  // console.log(basket);
  update(id)
}

const update = (id) => {
  let search = basket.find((x)=> x.id === id )
  document.getElementById(id).innerHTML = search.item
  cartNumber()
}

const cartNumber = () => {
  let num = document.getElementById('cartAmount')  
  let data = basket.map((x)=> x.item).reduce( (a,b)=> a+b )
  num.innerHTML = data
}
