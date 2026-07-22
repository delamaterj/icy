import type { DatasetSummary } from "../../types/dataset";
import DatasetRow from "./DatasetRow"; 

interface DatasetTableProps {
    datasets: DatasetSummary[];
}

export default function DatasetTable({
    datasets}: DatasetTableProps) {
    return (
        <>
            <table>
                <thead>
                    <tr>
                        <th>Filename</th>
                        <th>Status</th>
                        <th>Rows</th>
                        <th>Columns</th>
                        <th>Uploaded</th>
                    </tr>
                </thead>
                <tbody>
                    {datasets.map(dataset => (
                    <DatasetRow
                        key={dataset.id}
                        dataset={dataset}
                    />
                    ))}
                </tbody>
            </table>
        </>
    );
}