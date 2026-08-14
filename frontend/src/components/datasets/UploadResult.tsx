import type { UploadDatasetResponse } from "../../types/dataset";
import { Link } from "react-router-dom";

interface UploadResultProps {
    result: UploadDatasetResponse | null | undefined;
    error: string | null;
}

export default function UploadResult({
    result,
    error
}: UploadResultProps) {

    if (error) {

        return (
            <div>
                <h2>Upload Failed</h2>
                <p>{error}</p>
            </div>
        );

    }

    if (!result) {
        return null;
    }

    if (result.passed) {

        return (
            <div>
                <h2>Dataset Uploaded Successfully</h2>
                <p>View new dataset<Link to={`/datasets/${result.dataset_id}`}>here</Link></p>
            </div>
        );
    }

    return (
        <div>
            <h2>Dataset Validation Failed</h2>
            <p>Validation Errors:</p>
            <ul>
                {
                    result.errors.map((error, index) => (
                        <li key={index}>{error}</li>
                    ))
                }
            </ul>
        </div>
    );
}