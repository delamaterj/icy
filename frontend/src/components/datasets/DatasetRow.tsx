import type { DatasetSummary } from "../../types/dataset";
import { Link } from "react-router-dom"

interface DatasetRowProps {
    dataset: DatasetSummary;
}

export default function DatasetRow({
    dataset}: DatasetRowProps) {
    return (
        <>
            <tr>
                <td><Link to={`/datasets/${dataset.id}`}>{dataset.original_filename}</Link></td>
                <td>{dataset.status}</td>
                <td>{dataset.row_count ?? "-"}</td>
                <td>{dataset.column_count ?? "-"}</td>
                <td>
                    {new Date(
                        dataset.uploaded_at
                    ).toLocaleDateString()}
                </td>
            </tr>
        </>
    );
}