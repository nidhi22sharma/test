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