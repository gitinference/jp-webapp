function downloadCSV(frec, lev) {
    const frequency = document.getElementById(frec).value.trim();
    const allowedFrequencies = ['quarterly', 'monthly'];
    let frequencyLower = frequency.toLowerCase();
    if (!allowedFrequencies.includes(frequencyLower)) {
        console.error('Invalid frequency value');
        return;
    }
    if (frequencyLower === 'quarterly') {
        frequencyLower = 'qrt';
    }
    const levelLower = lev.toLowerCase().trim();
    const allowedLevels = ['low', 'medium', 'high']; // Example allowed values
    if (!allowedLevels.includes(levelLower)) {
        console.error('Invalid level value');
        return;
    }
    const url = `http://192.168.50.24:7001/files/trade/jp/?level=${encodeURIComponent(levelLower)}&time_frame=${encodeURIComponent(frequencyLower)}&agr=false&group=false`;
    //alert(url)

    const a = document.createElement('a');
    a.href = url;
    a.download = `importaciones_${frequencyLower}.csv`;
    document.body.appendChild(a);
    a.click();
    document.body.removeChild(a);
}
window.downloadCSV = downloadCSV;