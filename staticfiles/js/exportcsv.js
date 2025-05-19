function downloadCSV(frec, lev) {
    const frequency = document.getElementById(frec).value;
    frequencyLower = frequency.toLowerCase();
    if (frequencyLower === 'quarterly') {
        frequencyLower = 'qrt';
    }
    levelLower = lev.toLowerCase();
    let url = `http://192.168.50.24:7001/files/trade/jp/?level=${levelLower}&time_frame=${frequencyLower}&agr=false&group=false`;
    //alert(url)

    const a = document.createElement('a');
    a.href = url;
    a.download = `importaciones_${frequencyLower}.csv`;
    document.body.appendChild(a);
    a.click();
    document.body.removeChild(a);
}
window.downloadCSV = downloadCSV;