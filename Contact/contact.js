const inputs = document.querySelectorAll(".input");

function focusFunc() {
  let parent = this.parentNode;
  parent.classList.add("focus");
}

function blurFunc() {
  let parent = this.parentNode;
  if (this.value == "") {
    parent.classList.remove("focus");
  }
}

inputs.forEach((input) => {
  input.addEventListener("focus", focusFunc);
  input.addEventListener("blur", blurFunc);
});

const toggle = document.querySelector(".navbar__toggle");
const menu = document.querySelector(".off-screen");
const overlay = document.querySelector(".overlay");

toggle.addEventListener("click", () => {
  toggle.classList.toggle("active");
  menu.classList.toggle("active");
  overlay.classList.toggle("active");
});

overlay.addEventListener("click", () => {
  toggle.classList.remove("active");
  menu.classList.remove("active");
  overlay.classList.remove("active");
});
