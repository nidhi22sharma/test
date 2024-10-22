var axis_id = TC.getParam('axis_id');  // Retrieve the parameter value

// Get the dropdown element using querySelector
var drpdown = document.querySelector('select[formcontrolname="batchIdFormControl"]');

// Check if the dropdown exists
if (drpdown) {
    var valueExists = false;  // Initialize a flag to check if value exists

    // Loop through the options to check if the value already exists
    for (var i = 0; i < drpdown.options.length; i++) {
        if (drpdown.options[i].value === axis_id) {
            valueExists = true;
            drpdown.selectedIndex = i;  // Select the option if it exists
            break;  // No need to continue if we found the value
        }
    }

    // If the value doesn't exist, create a new option and add it
    if (!valueExists) {
        var newoption = document.createElement('option');  // Create a new option element
        newoption.text = axis_id;  // Set the visible text for the option
        newoption.value = axis_id;  // Set the internal value for the option

        drpdown.add(newoption);  // Add the new option to the dropdown
        drpdown.selectedIndex = drpdown.options.length - 1;  // Select the newly added option
    }
} else {
    console.log("Dropdown not found!");
}