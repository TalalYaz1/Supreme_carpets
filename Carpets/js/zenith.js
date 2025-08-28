fetch("../json/zenith_carpets.json")
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
      grid.innerHTML = "";

      const start = (page - 1) * itemsPerPage;
      const end = start + itemsPerPage;
      const items = data.slice(start, end);

      items.forEach((carpet) => {
        const card = document.createElement("div");
        card.className = "card" + (carpet.hover_image ? " has-hover" : "");
        card.innerHTML = `
          <div class="image-container">
            <img src="${carpet.image}" alt="${carpet.name}" class="main-img">
            ${
              carpet.hover_image
                ? `<img src="${carpet.hover_image}" alt="${carpet.name} hover" class="hover-img">`
                : ""
            }
          </div>
          <div class="card-name">${carpet.name}</div>
        `;

        // Modal logic
        card.addEventListener("click", () => {
          modal.style.display = "block";
          modalImg.src = carpet.image;
          modalName.textContent = carpet.name;
          modalInfo.innerHTML = `
            <ul>
              <li>${carpet.info}</li>
              <li><a href="${carpet.url}" target="_blank">View Product</a></li>
            </ul>
          `;
        });

        grid.appendChild(card);
      });

      pageIndicator.textContent = `Page ${currentPage} of ${totalPages}`;
      prevBtn.disabled = currentPage === 1;
      nextBtn.disabled = currentPage === totalPages;
    }

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

    modalClose.addEventListener("click", () => {
      modal.style.display = "none";
    });

    window.addEventListener("click", (event) => {
      if (event.target === modal) {
        modal.style.display = "none";
      }
    });

    renderPage(currentPage);
  })
  .catch((error) => console.error("❌ Failed to load Zenith JSON:", error));
