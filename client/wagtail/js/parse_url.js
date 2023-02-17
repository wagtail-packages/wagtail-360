window.onload = function () {
    const urlField = document.getElementById("id_maps_url");
    const urlFieldDefaultStyle = window.getComputedStyle(urlField);
    const urlFieldHelp = urlField.parentElement.nextElementSibling.childNodes[1];
    const urlFieldHelpDefaultText = urlFieldHelp.textContent;
    const urlError = document.getElementById("url-error");

    /* 
    if the urlField has a value, e.g. when editing an existing page 
    parse the url and ste the value to "" as it could be wrongly formatted
    this means the page cannot be saved until the url is corrected
    */
    parseUrl(urlField.value, true);

    urlField.addEventListener("keyup", function () {
        urlError.innerHTML = "";
        parseUrl(urlField.value);
    }); 

    urlField.addEventListener("keydown", function () {
        urlField.style = urlFieldDefaultStyle;
    });

    function showError() {
        urlError.innerHTML = "Invalid URL format";
        urlField.style.borderColor = "red";
        urlField.style.backgroundColor = "rgba(255, 0, 0, 0.1)";
        urlError.style.color = "red";
        urlError.style.marginBottom = "0.5rem";
        urlFieldHelp.textContent = urlFieldHelpDefaultText;
    }

    function showSuccess() {
        urlField.style.borderColor = "green";
        urlField.style.backgroundColor = "rgba(0, 255, 0, 0.1)";
        urlFieldHelp.textContent = "URL is valid";
    }

    function parseUrl(url, editing) {
        /* 
        example url
        https://www.google.com/maps/place/place-name/@52.3185489,-2.117426,3a,90y,164.89h,87.42t/data=nothing-passed-here-is-useful
        */

        if (!url.length > 0) {
            urlFieldHelp.textContent = urlFieldHelpDefaultText;
            return;
        }

        if (!url.includes("@")) {
            showError();
            document.getElementById("id_lat").value = "";
            document.getElementById("id_lng").value = "";
            document.getElementById("id_heading").value = "";
            document.getElementById("id_elevation").value = "";
            document.getElementById("id_zoom_level").value = "";
        } else {

            const parts = url.split("@")[1].split(",");
            const zooms = ["90", "45", "15"]  // refers to 3 zoom levels 0, 1, 3

            if (parts.length == 6) {
                showSuccess();
                if (!editing) {
                    document.getElementById("id_lat").value = parts[0] * 1;
                    document.getElementById("id_lng").value = parts[1] * 1;
                    document.getElementById("id_heading").value = parts[4].replace("h", "") * 1;
                    document.getElementById("id_elevation").value = parts[5].split("/")[0].replace("t", "") * 1 - 90;
                    document.getElementById("id_zoom_level").value = zooms.indexOf(parts[3].replace("y", ""));
                }
            } else {
                showError();
            }
        }
    };
};
