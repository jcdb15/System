// Wait for the DOM to fully load before running the script
document.addEventListener('DOMContentLoaded', function() {
    // Get the button element by its ID
    const downloadBtn = document.getElementById('downloadBtn');
    
    // Add a click event listener to the button
    downloadBtn.addEventListener('click', function() {
        // Create an anchor (<a>) element
        const link = document.createElement('a');
        
        // Set the href attribute to the server endpoint that generates the Excel file
        link.href = 'http://localhost:3000/download-excel';  // Change this URL to match your server's route
        
        // Set the download attribute to suggest the filename for the Excel file
        link.download = 'members_list.xlsx';
        
        // Append the link to the DOM (it doesn't need to be visible)
        document.body.appendChild(link);
        
        // Programmatically click the link to trigger the download
        link.click();
        
        // Remove the link element from the DOM after the click
        document.body.removeChild(link);
    });
});
