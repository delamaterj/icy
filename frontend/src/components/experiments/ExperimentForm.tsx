import { useState } from "react";
import type { CreateExperimentRequest, ExperimentModel } from "../../types/experiment";
import { Link } from "react-router-dom";

interface Props {
    initialDatasetId : string
    onSubmit:
    (data: CreateExperimentRequest) => void;
    loading: boolean;
}

const models: {
    value: ExperimentModel;
    label: string;
}[] = [
    {
        value: "LOGISTIC_REGRESSION",
        label: "Logistic Regression"
    },
    {
        value: "DECISION_TREE",
        label: "Decision Tree"
    },
    {
        value: "RANDOM_FOREST",
        label: "Random Forest"
    }
];

export default function ExperimentForm({
    initialDatasetId,
    onSubmit,
    loading
}: Props) {

    const datasetId = initialDatasetId;
    const [name, setName] = useState("");
    const [description, setDescription] = useState("");
    const [model, setModel] = useState<ExperimentModel>("RANDOM_FOREST");
    const [targetColumn, setTargetColumn] = useState("");

    function handleSubmit(
        event: React.FormEvent
    ) {
        event.preventDefault();

        onSubmit({
            dataset_id: datasetId,
            name,
            description: description || undefined,
            model,
            target_column: targetColumn,
        });
    }

    return (
        <form onSubmit={handleSubmit}>
            <Link to={`/datasets/${initialDatasetId}`} target="_blank" rel="noopener nofererrer">
                Dataset
            </Link>
            <br/>

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
            <br/>
            <label>
                Description
            </label>
            <textarea
                value={description}
                onChange={(e) =>
                    setDescription(e.target.value)
                }
            />
            <br/>
            <label htmlFor="model">
                Model
            </label>
            <select
            id="model"
            value={model}
            onChange={(event) =>
                setModel(event.target.value as ExperimentModel)
            }
            required>
                {models.map((option) => (
                    <option
                    key={option.value}
                    value={option.value}>
                        {option.label}
                    </option>
                ))}
            </select>
            <br/>
            <label htmlFor="target-column">
                Target Column
            </label>
            <input
            id="target-column"
            type="text"
            value={targetColumn}
            onChange={(event) =>
                setTargetColumn(event.target.value)
            }
            placeholder="e.g. Label"
            required/>
            <br/>
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