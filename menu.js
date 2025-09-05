function setHeight(subMenu) {
  let total = 0;
  Array.from(subMenu.children).forEach((child) => {
    total += child.offsetHeight;
    const childSub = child.querySelector(".menu-item__sub");
    if (childSub && childSub.style.maxHeight) {
      total += parseInt(childSub.style.maxHeight);
    }
  });
  subMenu.style.maxHeight = total + "px";
}

function toggle(btn) {
  const subMenu = btn.nextElementSibling;
  if (!subMenu) return;

  if (subMenu.style.maxHeight) {
    subMenu.style.maxHeight = null;
    subMenu
      .querySelectorAll(".menu-item__sub")
      .forEach((child) => (child.style.maxHeight = null));
  } else {
    setHeight(subMenu);

    // Close sibling submenus
    const siblings = Array.from(
      btn.parentElement.parentElement.children
    ).filter((el) => el !== btn.parentElement);
    siblings.forEach((sib) => {
      const sibSub = sib.querySelector(".menu-item__sub");
      if (sibSub) {
        sibSub.style.maxHeight = null;
        sibSub
          .querySelectorAll(".menu-item__sub")
          .forEach((c) => (c.style.maxHeight = null));
      }
    });

    // Update all parent heights recursively
    let parent = btn.parentElement.parentElement.closest(".menu-item__sub");
    while (parent) {
      setHeight(parent);
      parent = parent.parentElement.closest(".menu-item__sub");
    }
  }
}

// Add event listeners
document.querySelectorAll(".toggle-btn").forEach((btn) => {
  btn.addEventListener("click", (e) => {
    e.preventDefault();
    toggle(btn);
  });
});
