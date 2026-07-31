import { apiFetch } from "./client";
import type { DatasetSummary, DatasetDetails, UploadDatasetResponse } from "../types/dataset";


export function getDatasets() {
    return apiFetch<DatasetSummary[]>("/datasets");
}

export function getDatasetId(id: string) {
    return apiFetch<DatasetDetails>(`/datasets/${id}`)
}

export function uploadDataset(file: File) {
   const formData = new FormData();

    formData.append("file", file);

    return apiFetch<UploadDatasetResponse>(
    "/datasets/upload", {
        method: "POST",
        body: formData
    });
}