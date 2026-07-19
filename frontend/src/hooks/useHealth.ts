import { useEffect, useState } from "react";
import { getHealth } from "../api/healthApi";
import type { HealthResponse } from "../api/healthApi";

export function useHealth() {

    const [health, setHealth] =
        useState<HealthResponse | null>(null);

    const [loading, setLoading] =
        useState(true);

    const [error, setError] =
        useState<string | null>(null);

    useEffect(() => {
        async function load() {
            try {
                const data = await getHealth();
                setHealth(data);
            } catch {
                setError("Unable to reach backend.");
            } finally {
                setLoading(false);
            }
        }
        load();
    }, []);

    return {
        health,
        loading,
        error
    };
}