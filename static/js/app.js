


$(document).on('click', '.add-to-cart', function() {
    const title = $(this).closest('.prod-container').find('.prod-title').text();
    const price = $(this).closest('.prod-container').find('.prod-price').text();
    const img = $(this).closest('.prod-container').find('.prod-img').attr('src');
    let allAddedProdsToCart = [];
    let addedProdsToCart = {
      prodTitle: title,
      prodPrice: price,
      prodImg: img
    }
    allAddedProdsToCart.push(addedProdsToCart);
    localStorage.setItem('cartProducts', JSON.stringify(allAddedProdsToCart));
    console.log('Title ', title);
    console.log('Price ', price);
    console.log('img ', img);
});
