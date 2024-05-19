// Function to display form errors
function displayFormErrors(errorsHtml) {
    // Assuming you have an element to display the overall form error
    // Replace 'form-error-container' with the actual ID or class of your error container
    const formErrorContainer = document.getElementById('form-error-container');

    // Clear existing error messages
    formErrorContainer.innerHTML = '';

    // Create a temporary div to parse the HTML
    const tempDiv = document.createElement('div');
    tempDiv.innerHTML = errorsHtml;

    // Extract and display the overall form error
    const formError = tempDiv.querySelector('.errorlist');
    if (formError) {
        formErrorContainer.innerHTML = formError.innerHTML;
    }

    // Display errors for individual fields
    displayFieldErrors(tempDiv, 'country', 'country-error-container');
    displayFieldErrors(tempDiv, 'city_name', 'city-error-container');
}

// Function to display errors for individual fields
function displayFieldErrors(tempDiv, fieldName, containerId) {
    const fieldErrorContainer = document.getElementById(containerId);
    const fieldErrorList = tempDiv.querySelector(`#${fieldName}-error-container .errorlist`);

    // Clear existing field error messages
    fieldErrorContainer.innerHTML = '';

    if (fieldErrorList) {
        // Display errors for the specific field
        fieldErrorContainer.innerHTML = fieldErrorList.innerHTML;
    }
}
