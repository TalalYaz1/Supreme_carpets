fetch("riva_carpets.json")
  .then((res) => res.json())
  .then((data) => {
    const grid = document.getElementById("carpetGrid");
    data.forEach((carpet) => {
      const card = document.createElement("div");
      card.className = "card";
      card.innerHTML = `
      <img src="${carpet.image}" alt="${carpet.name}">
      <div class="card-name">${carpet.name}</div>
    `;
      grid.appendChild(card);
    });
  })
  .catch((error) => console.error("Failed to load carpet JSON:", error));
