fetch("../json/amtico_products.json")
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

      items.forEach((item) => {
        const carpet = item["af-productcard"];

        const card = document.createElement("div");
        card.className = "card" + (carpet.hover_image_url ? " has-hover" : "");
        card.innerHTML = `
          <div class="image-container">
            <img src="${carpet.main_image_url}" alt="${
          carpet.name
        }" class="main-img">
            ${
              carpet.hover_image_url
                ? `<img src="${carpet.hover_image_url}" alt="${carpet.name} hover" class="hover-img">`
                : ""
            }
          </div>
          <div class="card-name">${carpet.name}</div>
        `;

        // Modal logic
        card.addEventListener("click", () => {
          modal.style.display = "block";
          modalImg.src = carpet.main_image_url;
          modalName.textContent = carpet.name;
          modalInfo.innerHTML = `
            <ul>
              <li>Code: ${carpet.code}</li>
              <li>Collection: ${carpet.collection}</li>
              <li><a href="${carpet.product_url}" target="_blank">View Product</a></li>
            </ul>
          `;
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
  .catch((error) => console.error("Failed to load carpet JSON:", error));
