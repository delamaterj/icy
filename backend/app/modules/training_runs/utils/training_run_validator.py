class TrainingRunValidator:

    @staticmethod
    def validate_training_run(data):

        errors = []
        
        test_size = data.get("test_size", 0.20)
        if not isinstance(test_size, (int, float)) or isinstance(test_size, bool):
            errors.append("test_size must be a number.")
        elif not 0 < test_size < 1:
            errors.append("test_size must be greater than 0 and less than 1.")  

        random_seed = data.get("random_seed", 42)
        if not isinstance(random_seed, int) or isinstance(random_seed, bool):
            errors.append("random_seed must be an integer.")

        return errors
                
