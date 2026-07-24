import type { DatasetSummary } from "../../types/dataset";

interface DatasetRowProps {
    dataset: DatasetSummary;
}

export default function DatasetRow({
    dataset}: DatasetRowProps) {
    return (
        <>
            <tr>
                <td>{dataset.original_filename}</td>
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