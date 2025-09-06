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

// For hamburger toggle
const menuToggle = document.querySelector(".navbar__toggle");
const menu = document.querySelector(".off-screen");
const overlay = document.querySelector(".overlay");

menuToggle.addEventListener("click", () => {
  menuToggle.classList.toggle("active");
  console.log("hello");
  menu.classList.toggle("active");
  overlay.classList.toggle("active");
});

overlay.addEventListener("click", () => {
  menuToggle.classList.remove("active");
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
const reviewBoxDesktop = document.getElementById("review-box");
const reviewBoxMobile = document.getElementById("review-box-mobile");

function showReview(index) {
  const { author_name, rating, text, time_description } =
    reviewData.reviews[index];

  let stars = "";
  for (let i = 1; i <= 5; i++) {
    stars += i <= rating ? "★" : "☆";
  }

  const reviewHTML = `
    <div class="review-author">${author_name}</div>
    <div class="review-stars">${stars}</div>
    <div class="review-text">"${text}"</div>
    <div class="review-time">${time_description}</div>
  `;

  if (reviewBoxDesktop) reviewBoxDesktop.innerHTML = reviewHTML;
  if (reviewBoxMobile) reviewBoxMobile.innerHTML = reviewHTML;
}

// Initial display
showReview(currentReviewIndex);
reviewBoxDesktop?.classList.add("visible");
reviewBoxMobile?.classList.add("visible");

// Rotate reviews every 10s
setInterval(() => {
  reviewBoxDesktop?.classList.remove("visible");
  reviewBoxMobile?.classList.remove("visible");

  setTimeout(() => {
    currentReviewIndex = (currentReviewIndex + 1) % reviewData.reviews.length;
    showReview(currentReviewIndex);
    reviewBoxDesktop?.classList.add("visible");
    reviewBoxMobile?.classList.add("visible");
  }, 500);
}, 10000);

// Accordion toggle logic (if you're still using it)
document.querySelectorAll(".accordion .item").forEach((item) => {
  item.addEventListener("click", () => {
    const openItem = document.querySelector(".accordion .item.open");

    if (openItem && openItem !== item) {
      openItem.classList.remove("open");
    }

    item.classList.toggle("open");
  });
});

document.addEventListener("DOMContentLoaded", function () {
  const videos = document.querySelectorAll(".video-hover");

  videos.forEach((video) => {
    video.addEventListener("mouseenter", () => {
      video.loop = true;
      video.play();
    });

    video.addEventListener("mouseleave", () => {
      video.pause();
      video.currentTime = 0; // rewind to start
    });
  });
});
