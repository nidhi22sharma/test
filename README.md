var dropdowns = document.querySelectorAll('select[name="consolidation"]');  // Get all matches
tc.log("Number of dropdowns found: " + dropdowns.length, "standard");

if (dropdowns.length > 0) {
    var dropdown = dropdowns[0];  // Use the first match
    tc.log("Dropdown found", "standard");
    
    // Log all options in the dropdown
    Array.from(dropdown.options).forEach(function(option, index) {
        tc.log("Option " + index + ": " + option.textContent, "standard");  // Log each option's text
    });
    
    // Find and select the option that contains 'TCR'
    var optionToSelect = Array.from(dropdown.options).find(function(opt) {
        return opt.textContent.includes("TCR");
    });

    if (optionToSelect) {
        optionToSelect.selected = true;  // Select the option containing 'TCR'
        dropdown.dispatchEvent(new Event('change'));  // Trigger change event
        tc.log("Option containing 'TCR' selected", "standard");
    } else {
        tc.log("No option containing 'TCR' found", "error");
    }
} else {
    tc.log("No dropdowns found", "error");
}