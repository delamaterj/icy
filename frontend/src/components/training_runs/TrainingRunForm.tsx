import { useState } from "react";
import { useCreateTrainingRun } from "../../hooks/useCreateTrainingRun";

interface CreateTrainingRunFormProps {
    experimentId: string;
    onSuccess?: () => void;
}

const generateRandomSeed = (): number => {
    return Math.floor(Math.random() * 1_000_000);
};

export default function CreateTrainingRunForm({
    experimentId,
}: CreateTrainingRunFormProps) {

    const [testSize, setTestSize] = useState("0.2");
    const [randomSeed, setRandomSeed] = useState("42");

    const { createTrainingRun, loading, error } =
        useCreateTrainingRun();

    const handleRandomizeSeed = () => {
        setRandomSeed(generateRandomSeed().toString());
    };

    async function handleSubmit(event: React.FormEvent<HTMLFormElement>) {

        event.preventDefault();
        try {
            const response = await createTrainingRun(
                experimentId, 
                {
                    test_size: Number(testSize),
                    random_seed: Number(randomSeed)
                }
            );
            console.log(response)
        }
        catch (err) {
            console.log(err);
        }
    };

    return (
        <form onSubmit={handleSubmit}>
            
            <div>
                <label htmlFor="test-size">
                    Test Size
                </label>

                <input
                    id="test-size"
                    type="number"
                    min="0.1"
                    max="0.9"
                    step="0.05"
                    value={testSize}
                    onChange={(event) =>
                        setTestSize(event.target.value)
                    }
                    required
                />

                <small>
                    Proportion of the dataset used for testing.
                </small>
            </div>

            <div>
                <label htmlFor="random-seed">
                    Random Seed
                </label>

                <input
                    id="random-seed"
                    type="number"
                    value={randomSeed}
                    onChange={(event) =>
                        setRandomSeed(event.target.value)
                    }
                    required
                />

                <button
                    type="button"
                    onClick={handleRandomizeSeed}
                >
                    Randomize Seed
                </button>
            </div>

            {error && (
                <p>
                    {error}
                </p>
            )}

            <button
                type="submit"
                disabled={loading}
            >
                {loading ? "Creating..." : "Create Training Run"}
            </button>

        </form>
    );
}