import { apiFetch } from "./client";
import type { DatasetSummary, DatasetDetails } from "../types/dataset";



export function getDatasets() {
    return apiFetch<DatasetSummary[]>("/datasets");
}

export function getDatasetId(id: string) {
    return apiFetch<DatasetDetails>(`/datasets/${id}`)
}