fetch("../json/therdex_products.json")
  .then((res) => res.json())
  .then((data) => {
    const grid = document.getElementById("carpetGrid");
    const modal = document.getElementById("carpetModal");
    const modalImg = document.getElementById("modalImage");
    const modalName = document.getElementById("modalName");
    const modalInfo = document.getElementById("modalInfo");
    const modalClose = document.getElementById("modalClose");
    const prevBtn = document.getElementById("prevPage");
    const nextBtn = document.getElementById("nextPage");
    const pageIndicator = document.getElementById("pageIndicator");

    const itemsPerPage = 9;
    let currentPage = 1;
    const totalPages = Math.ceil(data.length / itemsPerPage);

    function renderPage(page) {
      grid.innerHTML = ""; // Clear old items

      const start = (page - 1) * itemsPerPage;
      const end = start + itemsPerPage;
      const items = data.slice(start, end);

      items.forEach((product) => {
        const card = document.createElement("div");
        card.className = "card" + (product.hover_image ? " has-hover" : "");
        card.innerHTML = `
          <div class="image-container">
            <img src="${product.main_image}" alt="${
          product.title
        }" class="main-img">
            ${
              product.hover_image
                ? `<img src="${product.hover_image}" alt="${product.title} hover" class="hover-img">`
                : ""
            }
          </div>
          <div class="card-name">${product.title}</div>
        `;

        card.addEventListener("click", () => {
          modal.style.display = "block";
          modalImg.src = product.main_image;
          modalName.textContent = product.title;
          if (product.info) {
            const infoItems = product.info.split("||");
            modalInfo.innerHTML =
              "<ul>" +
              infoItems.map((item) => `<li>${item}</li>`).join("") +
              "</ul>";
          } else {
            modalInfo.innerHTML = "";
          }
        });

        grid.appendChild(card);
      });

      // Update pagination UI
      pageIndicator.textContent = `Page ${currentPage} of ${totalPages}`;
      prevBtn.disabled = currentPage === 1;
      nextBtn.disabled = currentPage === totalPages;
    }

    // Pagination controls
    prevBtn.addEventListener("click", () => {
      if (currentPage > 1) {
        currentPage--;
        renderPage(currentPage);
      }
    });

    nextBtn.addEventListener("click", () => {
      if (currentPage < totalPages) {
        currentPage++;
        renderPage(currentPage);
      }
    });

    // Modal close logic
    modalClose.addEventListener("click", () => {
      modal.style.display = "none";
    });

    window.addEventListener("click", (event) => {
      if (event.target === modal) {
        modal.style.display = "none";
      }
    });

    // Initial render
    renderPage(currentPage);
  })
  .catch((error) => console.error("Failed to load Therdex JSON:", error));
