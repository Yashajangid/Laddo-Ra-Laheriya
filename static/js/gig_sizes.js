document.addEventListener("DOMContentLoaded", function () {
  const wrapper = document.getElementById("sizes-wrapper");
  const addBtn = document.getElementById("add-size-btn");
  const stockField = document.getElementById("total-stock");

  function updateStock() {
    let total = 0;
    document.querySelectorAll(".qty-field").forEach(input => {
      total += parseInt(input.value || 0);
    });
    stockField.value = total;
  }

  addBtn.addEventListener("click", () => {
    const row = document.createElement("div");
    row.className = "size-row";

    row.innerHTML = `
      <select name="size[]" class="field select-field">
        <option value="">Select Size</option>
        <option value="S">Small (S)</option>
        <option value="M">Medium (M)</option>
        <option value="L">Large (L)</option>
        <option value="FREE">Free Size</option>
      </select>

      <input type="number"
             name="quantity[]"
             class="field qty-field"
             placeholder="Qty"
             min="1">
    `;

    wrapper.appendChild(row);

    row.querySelector(".qty-field").addEventListener("input", updateStock);
  });

  document.querySelectorAll(".qty-field").forEach(input => {
    input.addEventListener("input", updateStock);
  });
});
