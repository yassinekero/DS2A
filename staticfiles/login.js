let form_login = document.querySelector(".login-side");
let form_singup = document.querySelector(".signup-side");
let signup_btn = document.querySelector(".signup_btn");
let login_btn = document.querySelector(".login_btn");


signup_btn.addEventListener("click", () =>
{

  form_login.style.display = "none";
  form_singup.style.display = "block";
  console.log(signup_btn.style.display);
});

login_btn.addEventListener("click", () =>
{
  form_singup.style.display = "none";
  form_login.style.display = "block";
  console.log(signup_btn.style.display);
});