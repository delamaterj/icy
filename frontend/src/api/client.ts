const API_BASE_URL =
    import.meta.env.VITE_API_BASE_URL ??
    "http://localhost:5000";

export async function apiFetch<T>(
    endpoint: string,
    options?: RequestInit
): Promise<T> {

    const response = await fetch(
        `${API_BASE_URL}${endpoint}`,
        options
    );

    const data = await response.json();

    if (!response.ok) {

        throw new Error(
            data.error ??
            `Request failed (${response.status})`
        );
    }

    return data;
}