const preservePages = {
    "/indicadores-mensuales/": ["indicadores_frequency", "indicadores_dropdown"],
};

const currentPath = window.location.pathname;

if (!Object.keys(preservePages).includes(currentPath)) {
    const keysToReset = Object.values(preservePages).flat();

    keysToReset.forEach(key => {
        sessionStorage.removeItem(key);
    });
} else {
    const allowedKeys = preservePages[currentPath];
    const allKeys = Object.values(preservePages).flat();

    allKeys.forEach(key => {
        if (!allowedKeys.includes(key)) {
            sessionStorage.removeItem(key);
        }
    });
}