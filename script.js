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
      author_name: "Sarah K.",
      rating: 5,
      text: "Plumbers Pro installed a brand new boiler in our home, and the whole process was seamless. The team was punctual, friendly, and left everything spotless. Highly recommend for heating services!",
      time_description: "3 months ago",
    },
    {
      author_name: "Mark H.",
      rating: 5,
      text: "Had a leaking pipe under the kitchen sink and they arrived within the hour. Super efficient and professional. The plumber explained everything clearly and fixed it in no time.",
      time_description: "1 month ago",
    },
    {
      author_name: "Lina A.",
      rating: 5,
      text: "We used Plumbers Pro for a full bathroom renovation. From tiling to fitting the shower and toilet, everything was done to the highest standard. Can’t thank them enough!",
      time_description: "2 months ago",
    },
    {
      author_name: "David R.",
      rating: 5,
      text: "Excellent emergency service! Our radiator started leaking late at night and they were at our door in under 45 minutes. Really impressed with their quick response and professionalism.",
      time_description: "5 months ago",
    },
    {
      author_name: "Fatima Z.",
      rating: 5,
      text: "Had our entire central heating system upgraded by Plumbers Pro. The engineers were very knowledgeable and did a neat, tidy job. Great communication from start to finish.",
      time_description: "4 months ago",
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
