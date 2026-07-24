export interface DatasetSummary {
    id: string;
    original_filename: string;
    status: string;
    row_count: number | null;
    column_count: number | null;
    uploaded_at: string;
}

export interface DatasetDetails extends DatasetSummary {
    stored_filename: string;
    checksum: string;
    file_type: string;
    file_size_bytes: number;
}