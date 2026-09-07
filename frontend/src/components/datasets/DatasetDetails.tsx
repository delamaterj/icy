import type { DatasetDetails } from "../../types/dataset";
import { Link } from "react-router-dom";

interface DatasetDetailsProps {
    dataset: DatasetDetails;
}

export default function DatasetDetails({dataset}: 
DatasetDetailsProps) {
    return (
        <>
            <h2>Dataset Details</h2>

            <div className="details-grid">
            <div className="detail-item">
                <strong>Original Filename: </strong>
                <span>{dataset.original_filename}</span>
            </div>

            <div className="detail-item">
                <strong>Stored Filename: </strong>
                <span>{dataset.stored_filename}</span>
            </div>

            <div className="detail-item">
                <strong>Status: </strong>
                <span>{dataset.status}</span>
            </div>

            <div className="detail-item">
                <strong>File Type: </strong>
                <span>{dataset.file_type}</span>
            </div>

            <div className="detail-item">
                <strong>File Size: </strong>
                <span>{dataset.file_size_bytes}</span>
            </div>

            <div className="detail-item">
                <strong>Rows: </strong>
                <span>{dataset.row_count ?? "Unknown"}</span>
            </div>

            <div className="detail-item">
                <strong>Columns: </strong>
                <span>{dataset.column_count ?? "Unknown"}</span>
            </div>

            <div className="detail-item">
                <strong>Checksum:  </strong>
                <span>{dataset.checksum}</span>
            </div>

            <div className="detail-item">
                <strong>Version: </strong>
                <span>{dataset.version}</span>
            </div>

            <div className="detail-item">
                <strong>Uploaded: </strong>
                <span>{dataset.uploaded_at}</span>
            </div>
            </div>

            {dataset.status === "READY" 
            && <Link to={`/experiments/create/${dataset.id}`}>Create experiment from this dataset</Link>}

        </>
    );
}