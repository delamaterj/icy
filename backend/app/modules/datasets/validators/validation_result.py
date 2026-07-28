from dataclasses import dataclass, field

@dataclass
class ValidationResult:
    passed: bool = True
    errors: list[str] = field(default_factory=list)

    def add_error(self, message: str):
        self.passed = False
        self.errors.append(message)