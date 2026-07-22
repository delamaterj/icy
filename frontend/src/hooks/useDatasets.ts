import { useEffect, useState } from "react";
import { getDatasets } from "../api/datasetApi";
import type { DatasetSummary } from "../types/dataset";

export function useDatasets() {

    const [datasets, setDatasets] =
        useState<DatasetSummary[]>([]);

    const [loading, setLoading] =
        useState(true);

    const [error, setError] =
        useState<string | null>(null);

    async function fetchDatasets() {

        try {

            setLoading(true);

            const response =
                await getDatasets();

            setDatasets(response);

            setError(null);

        } catch (err) {

            setError("Unable to load datasets.");

        } finally {

            setLoading(false);

        }
    }

    useEffect(() => {

        fetchDatasets();

    }, []);

    return {
        datasets,
        loading,
        error,
        refresh: fetchDatasets
    };
}