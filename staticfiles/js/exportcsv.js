
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
window.downloadCSV = downloadCSV;