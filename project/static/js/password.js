document.addEventListener('DOMContentLoaded', function () {
  const passwordField = document.getElementById('login_password')
  const togglePasswordButton = document.getElementById('togglePasswordButton')

  togglePasswordButton.addEventListener('click', function () {
    if (passwordField.type === 'password') {
      passwordField.type = 'text'
      togglePasswordButton.innerHTML =
        '<i class="fa-solid fa-eye-slash" style="color: #ffffff;"></i>'
    } else {
      passwordField.type = 'password'
      togglePasswordButton.innerHTML =
        '<i class="fa-solid fa-eye" style="color: #ffffff;"></i>'
    }
  })
})

