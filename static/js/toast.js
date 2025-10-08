function showToast(message, type = 'success', duration = 3000) {
    const toast = document.createElement('div');

    // Base styling (abu-abu gelap + teks putih untuk netral / sukses)
    let bgClass = 'bg-gray-800 text-white border border-gray-700'; 

    // Override jika error
    if (type === 'error') {
        bgClass = 'bg-red-600 text-white border border-red-700';
    }

    toast.className = `
        fixed top-6 left-1/2 transform -translate-x-1/2 px-4 py-3 rounded-md shadow-lg transition-all duration-500 
        opacity-0 -translate-y-6 ${bgClass} z-[9999]
    `;

    toast.innerText = message;
    document.body.appendChild(toast);

    // Munculkan toast
    requestAnimationFrame(() => {
        toast.classList.remove('opacity-0', 'translate-y-6');
        toast.classList.add('opacity-100', 'translate-y-0');
    });

    // Hilangkan toast
    setTimeout(() => {
        toast.classList.remove('opacity-100', 'translate-y-0');
        toast.classList.add('opacity-0', 'translate-y-6');
        setTimeout(() => toast.remove(), 1500);
    }, duration);
}
