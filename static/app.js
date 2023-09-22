document.addEventListener("DOMContentLoaded", function () {
    document.getElementById("logoutButton").addEventListener("click", function () {
        // Function to get query parameters from URL
        const getQueryParam = (param) => {
            const urlParams = new URLSearchParams(window.location.search);
            return urlParams.get(param);
        };

        // Retrieve the JWT token and student ID from the URL query parameters
        const jwtToken = getQueryParam("token");
        const studentID = getQueryParam("student_id");

        if (jwtToken && studentID) {
            // Construct the URL with query parameters
            const logoutURL = `/v1/auth/logout?token=${encodeURIComponent(jwtToken)}&student_id=${encodeURIComponent(
                studentID
            )}`;

            // Redirect to the logout URL
            window.location.href = logoutURL;
        } else {
            console.error("Missing JWT token or student ID in URL.");
        }
    });
});
