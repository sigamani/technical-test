"""
Defines Paths class used across the utils module to handle filepaths.
"""
from typing import Optional

import pathlib
from pathlib import Path


class Paths:
    """Class to reliably handle file paths relative to the root directory path.

    Attributes:
        root_path: The root path of the directory, which serves as the basis for all dynamically created filepaths.
    """

    def __init__(self) -> None:
        """Initializes Paths instance.

        Finds the root path as the directory two levels upwards of where this file is located.
        Prints out the detected root path.
        """
        self.root_path = Path(__file__).resolve().parent.parent
        print(f"Root path is detected to be {self.root_path}\n")

    @staticmethod
    def safe_return(path: pathlib.Path, mkdir: bool) -> pathlib.Path:
        """Safely return a path by optionally creating the parent directories to avoid errors when writing to the path.

        Args:
            path: Path to optionally create and return.
            mkdir: If True, creates the parent directories. If False, it has no effect.

        Returns:
            Input path.
        """
        if mkdir:
            path.parent.mkdir(parents=True, exist_ok=True)
        return path

    def data_weighting_report(
        self, research_name: str, mkdir: bool, weight_name: Optional[str] = None
    ) -> pathlib.Path:
        """Returns path to weighting report of the specified poll.

        Args:
            research_name: The poll to create the path for.
            mkdir: If True, creates parent directories for safe writing. If False, won't create parents.
            weight_name: If a value is passed, will append " (weight_name).xlsx" to the path for reading the report in.
                If None is passed, won't append anything as quantipy3 appends the snippet automatically.

        Returns:
            Path to weighting report of the specified poll.
        """
        if weight_name:  # for reading the report back in
            last_part = f"{research_name}_weight_report ({weight_name}).xlsx"
        else:  # for writing the report, where quantipy3 appends the weight name and the .xlsx file extenstion automatically
            last_part = f"{research_name}_weight_report"
        return self.safe_return(
            self.root_path
            / "data"
            / "processed_data"
            / "response_data"
            / "weighting_reports"
            / last_part,
            mkdir=mkdir,
        )