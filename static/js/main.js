document.addEventListener("DOMContentLoaded", function() {
  // Get modal elements
  const editBtn = document.getElementById("edit-profile-btn");
  const modal = document.getElementById("edit-profile-modal");
  const closeModalBtn = document.getElementById("close-modal-btn");
  const closeModalFooterBtn = document.getElementById("close-modal-footer-btn");
  const modalBackground = document.querySelector("#edit-profile-modal .modal-background");

  // Function to open the modal
  const openModal = () => {
    modal.classList.add("is-active");
  };

  // Function to close the modal
  const closeModal = () => {
    modal.classList.remove("is-active");
  };

  // Add event listeners to open and close modal
  editBtn.addEventListener("click", openModal);
  closeModalBtn.addEventListener("click", closeModal);
  closeModalFooterBtn.addEventListener("click", closeModal);
  modalBackground.addEventListener("click", closeModal);

  // Optional: Close the modal when pressing the "Escape" key
  window.addEventListener("keydown", function(event) {
    if (event.key === "Escape") {
      closeModal();
    }
  });
});

