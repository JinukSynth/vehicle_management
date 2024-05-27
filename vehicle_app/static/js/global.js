function adjustScrollbarVisibility() {
    const scrollSection = document.getElementById("scrollSection");
    const containerWidth = scrollSection.offsetWidth;
    const contentWidth = scrollSection.scrollWidth;

    if (contentWidth > containerWidth) {
      scrollSection.style.overflowX = "auto";
    } else {
      scrollSection.style.overflowX = "hidden";
    }
  }
  window.onload = adjustScrollbarVisibility;
  window.onresize = adjustScrollbarVisibility;
  