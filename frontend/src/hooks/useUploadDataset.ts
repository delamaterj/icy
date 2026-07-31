import { useState } from "react";
import { uploadDataset } from "../api/datasetApi";
import type { UploadDatasetResponse } from "../types/dataset";

export function useUploadDataset() {

    const [result, setResult] =
        useState<UploadDatasetResponse | null>();

    const [loading, setLoading] =
        useState(false);

    const [error, setError] =
        useState<string | null>(null);

    async function upload(file: File) {

        try {

            setLoading(true);

            setError(null);

            const response =
                await uploadDataset(file);

            setResult(response);

            return response;

        } catch (err) {

            if (err instanceof Error) {
                setError(err.message);
            } else {
                setError("Unable to upload dataset.");
            }

        } finally {

            setLoading(false);

        }
    }
    
    return {
        upload,
        result,
        loading,
        error
    };
}