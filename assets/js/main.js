// Traumeri guide — small UI helpers
document.addEventListener('DOMContentLoaded', function () {
  // Smooth-scroll handled via CSS html{scroll-behavior:smooth}, this just
  // accounts for the sticky nav height when jumping to an anchor.
  document.querySelectorAll('a[href^="#"]').forEach(function (link) {
    link.addEventListener('click', function (e) {
      var id = link.getAttribute('href').slice(1);
      var target = document.getElementById(id);
      if (!target) return;
      e.preventDefault();
      var navH = document.querySelector('.nav') ? document.querySelector('.nav').offsetHeight : 0;
      var top = target.getBoundingClientRect().top + window.pageYOffset - navH - 12;
      window.scrollTo({ top: top, behavior: 'smooth' });
    });
  });

  // Photo placeholders: if a real image fails (or is missing), the
  // graceful fallback icon already sits behind it — just hide the broken img.
  document.querySelectorAll('.ph img').forEach(function (img) {
    img.addEventListener('error', function () {
      img.style.display = 'none';
    });
  });
});
