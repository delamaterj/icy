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

        const message =
        data.errors?.join("\n")
        ?? data.message
        ?? `Request failed (${response.status})`;

        throw new Error(message);
    }

    return data;
}