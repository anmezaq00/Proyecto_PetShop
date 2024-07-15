function formatCurrency(value) {
    return new Intl.NumberFormat('es-CL', {
        style: 'currency',
        currency: 'CLP'
    }).format(value);
}

function loadCart() {
    let cart = JSON.parse(localStorage.getItem('cart')) || [];
    let cartItemsContainer = document.getElementById('cartItems');
    let cartTotal = document.getElementById('cartTotal');
    let total = 0;

    cartItemsContainer.innerHTML = '';

    cart.forEach((item, index) => {
        const itemTotal = parseFloat(item.price);
        total += itemTotal;

        const cartItem = document.createElement('div');
        cartItem.classList.add('carrito-item');
        cartItem.innerHTML = `
            <img src="${item.image}" alt="${item.name}">
            <div class="carrito-item-details">
                <h5>${item.name}</h5>
                <p>${item.weight}</p>
            </div>
            <div class="carrito-item-price">${formatCurrency(item.price)}</div>
            <button class="remove-btn" data-index="${index}">Eliminar</button>
        `;
        cartItemsContainer.appendChild(cartItem);
    });

    cartTotal.textContent = `Total: ${formatCurrency(total)}`;

    document.querySelectorAll('.remove-btn').forEach(button => {
        button.addEventListener('click', removeItem);
    });
}

function removeItem(event) {
    const index = event.target.getAttribute('data-index');
    let cart = JSON.parse(localStorage.getItem('cart')) || [];
    cart.splice(index, 1);
    localStorage.setItem('cart', JSON.stringify(cart));
    loadCart();
}

document.addEventListener('DOMContentLoaded', loadCart);
