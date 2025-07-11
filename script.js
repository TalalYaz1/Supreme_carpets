const slides = document.querySelectorAll(".slide");
const slideshow = document.querySelector(".slideshow");
const cta = document.querySelector(".cta");
const reviews = document.querySelector(".reviews-container");

let current = 0;

// Auto-slide every 10 seconds
setInterval(() => {
  slides[current].classList.remove("active");
  current = (current + 1) % slides.length;
  slides[current].classList.add("active");
}, 10000);

// Parallax scroll effect
window.addEventListener("scroll", () => {
  const scrollY = window.scrollY;
  const speed = 0.5;
  slideshow.style.transform = `translateY(${scrollY * speed}px)`;
  cta.style.transform = `translateY(${scrollY * speed - 50}%)`; // offset to keep it centered
  reviews.style.transform = `translateY(${scrollY * speed - 50}%)`;
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

// Reviews

const reviewData = {
  reviews: [
    {
      author_name: "Monika S.",
      rating: 5,
      text: "Great service from start to finish. Rania was super professional and on top of all the requirements for our carpets, and Jamal fitted them beautifully. Very happy with the price and the quality of the job. Will definitely use this company again. Thank you!",
      time_description: "7 months ago",
    },
    {
      author_name: "Verified reviewer",
      rating: 5,
      text: "The team did an amazing job installing the carpet. They were punctual, professional, and efficient, leaving everything clean and perfectly finished. The results are flawless, and I couldn’t be happier. Highly recommend their services!",
      time_description: "10 months ago",
    },
    {
      author_name: "Omar Zidan",
      rating: 5,
      text: "Always delivering top work. Called for a flooring changes for our airbnb units, got it done with professional touch. Highly recommend!!!",
      time_description: "4 months ago",
    },
    {
      author_name: "Azad Arkwazi",
      rating: 5,
      text: "Adel and his team did a fantastic job and came in when I needed a reliable date for the work to be completed as I’ve just purchased the house. I need the house to become a home, and they’ve done a great job and I’m truly grateful. Highly recommend!!",
      time_description: "4 months ago",
    },
    {
      author_name: "Taimoor Rahim",
      rating: 5,
      text: "I recently used this company to get my living room and hallway fitted with laminate and the team carried out an extraordinary job! Not only were they quick in installing the laminate but also carried out a quality job. The hallway and corridor was completed in one piece leaving a super neat finish. Also the beading was cut and nailed with precision, overall a great job! Will certainly use this company in the future",
      time_description: "7 months ago",
    },
  ],
};

let currentReviewIndex = 0;
const reviewBox = document.getElementById("review-box");

function showReview(index) {
  const { author_name, rating, text, time_description } =
    reviewData.reviews[index];

  let stars = "";
  for (let i = 1; i <= 5; i++) {
    stars += i <= rating ? "★" : "☆";
  }

  reviewBox.innerHTML = `
      <div class="review-author">${author_name} <span class="review-stars">${stars}</span></div>
      <div class="review-text">"${text}"</div>
      <div class="review-time">${time_description}</div>
    `;
}

// Initial display
showReview(currentReviewIndex);

reviewBox.classList.add("visible");

// Review rotation with fade
setInterval(() => {
  // Fade out
  reviewBox.classList.remove("visible");

  setTimeout(() => {
    // Change content after fade-out
    currentReviewIndex = (currentReviewIndex + 1) % reviewData.reviews.length;
    showReview(currentReviewIndex);
    // Fade in
    reviewBox.classList.add("visible");
  }, 500); // match CSS transition duration
}, 10000);
