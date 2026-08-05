import { useEffect, useState } from "react";
import { getExperimentById } from "../api/experimentApi";
import type { ExperimentDetails } from "../types/experiment";

export function useExperiment(id: string) {

    const [experiment, setExperiment] = useState<ExperimentDetails | null>(null);
    const [loading, setLoading] = useState(true);
    const [error, setError] = useState<string | null>(null);

    async function fetchExperiment(experimentId: string) {

        try {
            setLoading(true);
            const response = await getExperimentById(experimentId);
            setExperiment(response);
            setError(null);
        } catch (err) {
            setError("Unable to load experiment.");
        } finally {
            setLoading(false);
        }
    }

    useEffect(() => {
        if (!id) return;
        fetchExperiment(id);
    }, [id]);

    return {
        experiment,
        loading,
        error,
        refresh: () => fetchExperiment(id)
    };
}