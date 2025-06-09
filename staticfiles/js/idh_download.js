function downloadIDHCSV() {
  fetch("/idh-index/csv/")
    .then(res => {
      if (!res.ok) throw new Error("Error al descargar el archivo");
      return res.blob();
    })
    .then(blob => {
      const url = URL.createObjectURL(blob);
      const a = document.createElement("a");
      a.href = url;
      a.download = "idh_index.csv";
      document.body.appendChild(a);
      a.click();
      a.remove();
      URL.revokeObjectURL(url);
    })
    .catch(err => console.error(err));
}
window.downloadIDHCSV = downloadIDHCSV;
