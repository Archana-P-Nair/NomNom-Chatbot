document.addEventListener('DOMContentLoaded', function() {
    
    let cart = [];
    let total = 0;
    const cartItemsList = document.querySelector('.cart-items');
    const orderTotal = document.querySelector('.order-total strong');
    
  
    const addToCartButtons = document.querySelectorAll('.add-to-cart');
    addToCartButtons.forEach(button => {
        button.addEventListener('click', function() {
            const menuItem = this.closest('.menu-item');
            const itemName = menuItem.querySelector('h4').textContent;
            const itemPrice = parseFloat(menuItem.querySelector('.price').textContent.replace('$', ''));
            
            
            const existingItem = cart.find(item => item.name === itemName);
            
            if (existingItem) {
                existingItem.quantity += 1;
            } else {
                cart.push({
                    name: itemName,
                    price: itemPrice,
                    quantity: 1
                });
            }
            
            total += itemPrice;
            updateCartDisplay();
        });
    });
    
    
    function updateCartDisplay() {
        cartItemsList.innerHTML = '';
        
        if (cart.length === 0) {
            cartItemsList.innerHTML = '<li>Your cart is empty</li>';
            orderTotal.textContent = 'Total: $0.00';
            return;
        }
        
        cart.forEach(item => {
            const li = document.createElement('li');
            li.innerHTML = `
                <span>${item.name} x${item.quantity}</span>
                <span>$${(item.price * item.quantity).toFixed(2)}</span>
            `;
            cartItemsList.appendChild(li);
        });
        
        orderTotal.textContent = `Total: $${total.toFixed(2)}`;
    }
    
    
    const orderForm = document.querySelector('.order-form');
    orderForm.addEventListener('submit', function(e) {
        e.preventDefault();
        
        if (cart.length === 0) {
            alert('Please add items to your cart before placing an order.');
            return;
        }
        
        
        const formData = new FormData(orderForm);
        const orderData = {
            customer: {
                name: formData.get('name'),
                address: formData.get('address'),
                phone: formData.get('phone'),
                instructions: formData.get('instructions')
            },
            items: cart,
            total: total
        };
        
        console.log('Order submitted:', orderData);
        alert('Thank you for your order! Your delicious food will be prepared soon.');
        
        
        orderForm.reset();
        cart = [];
        total = 0;
        updateCartDisplay();
    });
});
