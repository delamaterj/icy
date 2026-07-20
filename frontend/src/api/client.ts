const API_BASE_URL =
    import.meta.env.VITE_API_BASE_URL ??
    "http://localhost:5000";

export async function apiFetch<T>(endpoint: string): Promise<T> {

    const response = await fetch(`${API_BASE_URL}${endpoint}`);

    if (!response.ok) {
        throw new Error(`Request failed (${response.status})`);
    }

    return response.json();
}