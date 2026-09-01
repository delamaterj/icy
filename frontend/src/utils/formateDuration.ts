export function formatDuration(
    startedAt: string | null,
    completedAt: string | null
): string | null {
    if (!startedAt || !completedAt) {
        return null;
    }

    const start = new Date(startedAt);
    const end = new Date(completedAt);

    const durationMs = end.getTime() - start.getTime();
    const durationSeconds = Math.floor(durationMs / 1000);

    const minutes = Math.floor(durationSeconds / 60);
    const seconds = durationSeconds % 60;

    return `${minutes}m ${seconds}s`;
}