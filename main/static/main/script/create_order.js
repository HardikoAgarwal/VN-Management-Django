

function removeItems() {
    console.log('1')
    const currentCount = Number(document.getElementById('item-count').value);
    console.log(currentCount)
    if (currentCount > 1) {
        const itemContainer = document.getElementById('item-container');
        const lastItem = document.getElementById(`product-box-${currentCount}`);
        lastItem.remove();
        document.getElementById('item-count').value = currentCount - 1;
    }
}

function addValue(customerId, customerText) {
    var inputField = document.getElementById("customer-name");
    var custID = document.getElementById('customer-id');
    custID.value = customerId;
    inputField.value = customerText;
    openList()
}

function openList() {
    const nameList = document.getElementById('customer-option');
    if (nameList.style.height === '0px' || nameList.style.height === '') {
        nameList.style.height = '146px';
        document.getElementById('customer-name-btn').style.transform = 'rotate(0deg)';
    }
    else {
        nameList.style.height = '0px';
        document.getElementById('customer-name-btn').style.transform = 'rotate(180deg)';
    }
}

function openProductList(count) {
    const nameList = document.getElementById('product-option-' + count);
    const button = document.getElementById('product-name-btn-' + count);
    if (nameList.style.height === '0px' || nameList.style.height === '') {
        const allOptions = document.querySelectorAll('.product-option');
        const allButtons = document.querySelectorAll('.product-name-btn');
        allOptions.forEach(option => {
            option.style.height = '0px';
            option.style.minHeight = '0px';
        });
        allButtons.forEach(button => {
            if (button.style.transform = 'rotate(0deg)') {
                button.style.transform = 'rotate(180deg)';
            }
        });
        nameList.style.height = '146px';
        button.style.transform = 'rotate(0deg)';
    }
    else {
        nameList.style.height = '0px';
        button.style.transform = 'rotate(180deg)';
    }
}

function addProduct(productName, productWeight, id, count) {
    var inputField = document.getElementById("product-" + count);
    inputField.value = productName + ' - ' + productWeight + 'gm';
    document.getElementById('product-id-' + count).value = id;
    openProductList(count)
}

function subQuantity(count) {
    console.log(count);
    const quantity = document.getElementById('quantity-' + count);
    if (Number(quantity.value) > 0) {
        quantity.value = Number(quantity.value) - 1;
    }
}

function addQuantity_1(count) {
    console.log(count);
    const quantity = document.getElementById('quantity-' + count);
    quantity.value = Number(quantity.value) + 1;
}

function addQuantity_5(count) {
    console.log(count);
    const quantity = document.getElementById('quantity-' + count);
    quantity.value = Number(quantity.value) + 5;
}

function CheckForm() {
    const form = document.getElementById('order-form');
    let valid = true;
    const errorBox = document.getElementById('error-box');
    const inputstext = form.querySelectorAll('input[type="text"]');
    console.log('Ye chala')
    inputstext.forEach(function(input) {
        if (input.value === '' || input.value === null) {
            
            valid = false;
            console.log('Ye bhi chala')
            return;
        }
    });
    const inputsnum = form.querySelectorAll('input[type="number"]');
    inputsnum.forEach(function(input) {
        if (input.value === '0' || input.value === null) {
            valid = false;
            console.log('Ye  bhi chal gya')
            return;
        }
    });
    if (valid) {
        form.submit();
    }
    else{
        errorBox.style.display = 'flex';
    }
    }