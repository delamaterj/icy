import { useState } from "react";
import type { CreateExperimentRequest } from "../../types/experiment";

interface Props {
    onSubmit:
    (data: CreateExperimentRequest) => void;
    loading: boolean;
}

export default function ExperimentForm({
    onSubmit,
    loading
}: Props) {

    const [datasetId, setDatasetId] = useState("");
    const [name, setName] = useState("");
    const [description, setDescription] = useState("");

    function handleSubmit(
        event: React.FormEvent
    ) {
        event.preventDefault();

        onSubmit({
            dataset_id: datasetId,
            name,
            description:
                description || undefined
        });
    }

    return (
        <form onSubmit={handleSubmit}>
            <label>
                Dataset ID
            </label>
            <input
                value={datasetId}
                onChange={(e) =>
                    setDatasetId(e.target.value)
                }
                required
            />
            <label>
                Experiment Name
            </label>
            <input
                value={name}
                onChange={(e) =>
                    setName(e.target.value)
                }
                required
            />
            <label>
                Description
            </label>
            <textarea
                value={description}
                onChange={(e) =>
                    setDescription(e.target.value)
                }
            />
            <button
                type="submit"
                disabled={loading}
            >
                {
                    loading
                        ? "Creating..."
                        : "Create Experiment"
                }
            </button>
        </form>
    );
}