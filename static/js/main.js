// Small frontend enhancement: dismiss message banners after clicking.
document.querySelectorAll(".message").forEach((message) => {
  message.addEventListener("click", () => message.remove());
});
