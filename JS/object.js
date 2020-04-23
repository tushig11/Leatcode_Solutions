const getItems = customer => (...orders) => {
  console.log(orders);
  return orders
    .filter(order => order.customerId === customer.id)
    .map(order => order.items)
    .reduce((acc, cur) => [...acc, ...cur], []);
};

let customer = {
  name: "Fiddy",
  id: 5
};

const order1 = { id: 1, customerId: 1, items: ["belt"] };
const order2 = { id: 2, customerId: 5, items: ["chain", "deo"] };
const order3 = { id: 3, customerId: 5, items: ["grills"] };
const order4 = { id: 4, customerId: 2, items: ["pants"] };

const w = getItems(customer)(order1, order2, order3, order4);
const x = getItems(customer)([order1, order2, order3, order4]);
const y = getItems(customer, order1, order2, order3, order4);
const z = getItems(customer)(order1, order2, order4);

console.log(w, x, y, z);
