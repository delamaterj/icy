import type { DatasetDetails } from "../../types/dataset";

interface DatasetDetailsProps {
    dataset: DatasetDetails;
}

export default function DatasetDetails({dataset}: 
DatasetDetailsProps) {
    return (
        <>
            <h2>Dataset Details</h2>

            <p>
                <strong>Original Filename:</strong>{" "}
                {dataset.original_filename}
            </p>

            <p>
                <strong>Stored Filename:</strong>{" "}
                {dataset.stored_filename}
            </p>

            <p>
                <strong>Status:</strong>{" "}
                {dataset.status}
            </p>

            <p>
                <strong>File Type:</strong>{" "}
                {dataset.file_type}
            </p>

            <p>
                <strong>File Size:</strong>{" "}
                {dataset.file_size_bytes}
            </p>

            <p>
                <strong>Rows:</strong>{" "}
                {dataset.row_count ?? "Unknown"}
            </p>

            <p>
                <strong>Columns:</strong>{" "}
                {dataset.column_count ?? "Unknown"}
            </p>

            <p>
                <strong>Checksum:</strong>{" "}
                {dataset.checksum}
            </p>

            <p>
                <strong>Version:</strong>{" "}
                {dataset.version}
            </p>

            <p>
                <strong>Uploaded:</strong>{" "}
                {dataset.uploaded_at}
            </p>
        </>
    );
}