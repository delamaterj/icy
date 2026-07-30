import { useEffect, useState } from "react";
import { getDatasetId } from "../api/datasetApi";
import type { DatasetDetails } from "../types/dataset";

export function useDataset(id : string) {

    const [dataset, setDataset] =
        useState<DatasetDetails | null>(null);

    const [loading, setLoading] =
        useState(true);

    const [error, setError] =
        useState<string | null>(null);

    async function fetchDataset(id : string) {

        try {

            setLoading(true);

            const response =
                await getDatasetId(id);

            setDataset(response);

            setError(null);

        } catch {

            setError("Unable to load dataset.");

        } finally {

            setLoading(false);

        }
    }

    useEffect(() => {

        fetchDataset(id);

    }, [id]);

    return {
        dataset,
        loading,
        error,
        refresh: () => fetchDataset(id)
    };
}