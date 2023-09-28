import React, { useState, useEffect } from 'react';
import axios from 'axios';

const ProductList = () => {
  const [products, setProducts] = useState([]);
  const [selectedProducts, setSelectedProducts] = useState([]);
  const [totalPrice, setTotalPrice] = useState(0);

  useEffect(() => {
    axios.get('/products') // Replace with your backend URL
      .then(response => {
        setProducts(response.data);
      })
      .catch(error => {
        console.error('Error fetching products:', error);
      });
  }, []);

  const handleProductSelect = (product) => {
    const updatedSelectedProducts = [...selectedProducts, product];
    setSelectedProducts(updatedSelectedProducts);
    updateTotalPrice(updatedSelectedProducts);
  };

  const updateTotalPrice = (selectedProducts) => {
    const totalPrice = selectedProducts.reduce((total, product) => {
      return total + (product.price * product.quantity);
    }, 0);
    setTotalPrice(totalPrice);
  };

  const handlePurchase = () => {
    const productsToSend = selectedProducts.map(product => ({
      id: product.id,
      quantity: product.quantity
    }));

    axios.post('/purchase', { products: productsToSend }) // Replace with your backend URL
      .then(response => {
        console.log('Purchase success! Total price:', response.data.total_price);
      })
      .catch(error => {
        console.error('Error making purchase:', error);
      });
  };

  return (
    <div>
      <h2>Product List</h2>
      <ul>
        {products.map(product => (
          <li key={product.id}>
            {product.name} - ${product.price}
            <button onClick={() => handleProductSelect(product)}>Add to Cart</button>
          </li>
        ))}
      </ul>
      <h3>Selected Products:</h3>
      <ul>
        {selectedProducts.map(product => (
          <li key={product.id}>
            {product.name} - ${product.price} x {product.quantity}
          </li>
        ))}
      </ul>
      <p>Total Price: ${totalPrice}</p>
      <button onClick={handlePurchase}>Purchase</button>
    </div>
  );
};

export default ProductList;
