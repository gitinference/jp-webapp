
function downloadCSV(frec, lev, api) {
    const apienv = window.API_URL;
    
    let frequency = "";
    let frequencyLower = "";
    let levelLower = "";
    let apiurl = "";
    let baseUrl = "";
    if (frec != "") {

        frequency = document.getElementById(frec).value;
        frequencyLower = frequency.toLowerCase();
    }
    if (lev != "") {

        levelLower = lev.toLowerCase();
    }
    apiurl = api;
    baseUrl = apienv+apiurl+"/?";
    
    let params = [];
    if (frequencyLower) params.push("time_frame=" + encodeURIComponent(frequencyLower));
    if (levelLower)    params.push("level=" + encodeURIComponent(levelLower));

    url = baseUrl + params.join("&");
    const a = document.createElement('a');
    a.href = url;
    document.body.appendChild(a);
    a.click();
    document.body.removeChild(a);
}

function downloadAwardsCategoryCSV(frec, sec, thrd, cat, api) {
    const apienv = window.API_URL;
    
    let frequency = "";
    let second_dropdown = "";
    let category = "";
    let third_dropdown = "";

    let apiurl = "";
    let baseUrl = "";
    if (frec != "" && sec != "" && cat != "") {
        frequency = document.getElementById(frec).value;
        second_dropdown = document.getElementById(sec).value;
        category = document.getElementById(cat).value;
    }

    if (frec == 'yearly') {
        if (thrd != "") {
            third_dropdown = document.getElementById(thrd).value;
        }
    }

    apiurl = api;
    baseUrl = apienv+apiurl+"/?";
    
    let params = [];
    if (frequency) params.push("time_frame=" + encodeURIComponent(frequency));
    if (category) params.push("third_dropdown=" + encodeURIComponent(category));

    if (frequency == "yearly") {
        if (second_dropdown) params.push("dropdown=" + encodeURIComponent(second_dropdown));
    } else {
        if (third_dropdown) params.push("dropdown=" + encodeURIComponent(third_dropdown));
        if (second_dropdown) params.push("second_dropdown=" + encodeURIComponent(second_dropdown));
    }

    url = baseUrl + params.join("&");
    const a = document.createElement('a');
    a.href = url;
    document.body.appendChild(a);
    a.click();
    document.body.removeChild(a);
}

window.downloadAwardsCategoryCSV = downloadAwardsCategoryCSV;
window.downloadCSV = downloadCSV;