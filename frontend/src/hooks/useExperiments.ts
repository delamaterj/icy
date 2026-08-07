import { useEffect, useState } from "react";
import { getExperiments } from "../api/experimentApi";
import type { ExperimentSummary } from "../types/experiment";

export function useExperiments() {

    const [experiments, setExperiments] = useState<ExperimentSummary[]>([]);
    const [loading, setLoading] = useState(true);
    const [error, setError] = useState<string | null>(null);

    async function fetchExperiments() {

        try {
            setLoading(true);
            const response = await getExperiments();
            setExperiments(response);
            setError(null);
        } catch (err) {
            setError("Unable to load experiments.");
        } finally {
            setLoading(false);
        }
    }

    useEffect(() => {
        fetchExperiments();
    }, []);

    return {
        experiments,
        loading,
        error,
        refresh: fetchExperiments
    };
}