var searchTerm = "{{dropdownOption}}";  // Using a parameter for dynamic values
var dropdown = document.querySelector('select');
var options = dropdown.options;

for (var i = 0; i < options.length; i++) {
    if (options[i].textContent.includes(searchTerm)) {
        dropdown.selectedIndex = i;
        dropdown.dispatchEvent(new Event('change'));
        break;
    }
}


var dropdown = document.querySelector('select'); // Adjust the selector to match your dropdown element
var option = Array.from(dropdown.options).find(opt => opt.textContent.includes("TCR")); // Find option that contains "TCR"

if (option) {
    option.selected = true;  // Select the option
    dropdown.dispatchEvent(new Event('change'));  // Trigger change event to ensure selection is registered
} else {
    tc.log("No option containing 'TCR' found", "error");  // Optional error log if option isn't found
}
