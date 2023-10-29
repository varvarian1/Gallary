document.addEventListener('DOMContentLoaded', function () {
  const imageContainers = document.querySelectorAll('.image-container')
  const fullscreenImage = document.querySelector('.fullscreen-image')
  const fullscreenImg = document.querySelector('#fullscreen-img')
  const fullscreenTitle = document.querySelector('.fullscreen-title')
  const fullscreenDescr = document.querySelector('.fullscreen-descr')
  const closeBtn = document.querySelector('#close-button')
  const fullscreenContent = document.querySelector('.fullscreen-image')

  imageContainers.forEach((container, index) => {
    const image = container.querySelector('.main-img')
    const decor = container.querySelector('.gallery-card__decor')
    const imageSrc = image.getAttribute('data-src')
    const title = decor.querySelector('.decor__title').textContent
    const subTitle = decor.querySelector('.decor__descr').textContent
    decor.addEventListener('click', (event) => {
      // Проверяем, что событие было вызвано именно на элементе .gallery-card__decor
      if (event.target === decor) {
        fullscreenImg.src = imageSrc
        fullscreenTitle.textContent = title
        fullscreenDescr.textContent = subTitle
        // Устанавливаем заголовок
        fullscreenImage.style.display = 'block'
      }
    })

    closeBtn.addEventListener('click', () => {
      fullscreenImage.style.display = 'none'
    })
    fullscreenContent.addEventListener('click', () => {
      fullscreenImage.style.display = 'none'
    })
  })
})

document.addEventListener('DOMContentLoaded', function () {
  const categoryCards = document.querySelectorAll('.category-card')
  const galleryCards = document.querySelectorAll('.gallery__card')

  categoryCards.forEach((categoryCard) => {
    categoryCard.addEventListener('click', function () {
      const selectedCategory = categoryCard.getAttribute('data-category')

      categoryCards.forEach((card) => card.classList.remove('active'))
      categoryCard.classList.add('active')

      galleryCards.forEach((galleryCard) => {
        const imageCategory = galleryCard
          .querySelector('.decor__category')
          .getAttribute('data-category')
        if (selectedCategory === 'All' || selectedCategory === imageCategory) {
          galleryCard.style.display = 'block'
        } else {
          galleryCard.style.display = 'none'
        }
      })
    })
  })
})
