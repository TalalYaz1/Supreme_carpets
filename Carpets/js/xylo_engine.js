fetch("../json/xylo_engine.json")
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

      items.forEach((item) => {
        const card = document.createElement("div");
        card.className = "card";
        card.innerHTML = `
          <div class="image-container">
            <img src="${item.image_url}" alt="${item.name}" class="main-img">
          </div>
          <div class="card-name">${item.name}</div>
        `;

        // Modal logic
        card.addEventListener("click", () => {
          modal.style.display = "block";
          modalImg.src = item.image_url;
          modalName.textContent = item.name;
          modalInfo.innerHTML = `
            <ul>
              <li><a href="${item.url}" target="_blank">View Product</a></li>
            </ul>
          `;
        });

        grid.appendChild(card);
      });

      // Update pagination
      pageIndicator.textContent = `Page ${currentPage} of ${totalPages}`;
      prevBtn.disabled = currentPage === 1;
      nextBtn.disabled = currentPage === totalPages;
    }

    // Pagination events
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

    // Modal close
    modalClose.addEventListener("click", () => {
      modal.style.display = "none";
    });

    window.addEventListener("click", (e) => {
      if (e.target === modal) {
        modal.style.display = "none";
      }
    });

    // Initial render
    renderPage(currentPage);
  })
  .catch((err) => console.error("❌ Failed to load JSON:", err));
