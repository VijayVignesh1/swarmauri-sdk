import os
import subprocess
import logging
from typing import Dict, List, Literal, Optional

from pydantic import ConfigDict
from swarmauri_base.tools.Parameter import Parameter
from swarmauri_base.tools.ToolBase import ToolBase
from swarmauri_base.ComponentBase import ComponentBase


@ComponentBase.register_type(ToolBase, "FormatAndLintCodebaseTool")
class FormatAndLintCodebaseTool(ToolBase):
    """
    A tool for formatting and linting a codebase to ensure consistency and compliance with coding standards.

    Attributes:
        version (str): The version of the tool.
        name (str): The name of the tool.
        type (Literal["FormatAndLintCodebaseTool"]): The type of the tool.
        description (str): A brief description of what the tool does.
        parameters (List[Parameter]): The parameters for configuring the tool.
    """

    version: str = "0.1.dev1"
    name: str = "FormatAndLintCodebaseTool"
    type: Literal["FormatAndLintCodebaseTool"] = "FormatAndLintCodebaseTool"
    description: str = (
        "Formats the codebase to ensure consistency and compliance with coding standards."
    )
    parameters: List[Parameter] = [
        Parameter(
            name="directory",
            input_type="string",
            description="The directory of the codebase to format and lint.",
            required=True,
        ),
        Parameter(
            name="preview",
            input_type="boolean",
            description="Whether to show a preview of the changes before applying.",
            required=False,
            default=False,
        ),
        Parameter(
            name="formatter",
            input_type="string",
            description="The formatter to use (e.g., 'black', 'prettier').",
            required=False,
            default="black",
        ),
        Parameter(
            name="linter",
            input_type="string",
            description="The linter to use (e.g., 'eslint').",
            required=False,
            default="eslint",
        ),
    ]
    model_config = ConfigDict(arbitrary_types_allowed=True)

    def __call__(self, directory: str, preview: Optional[bool] = False, formatter: Optional[str] = "black", linter: Optional[str] = "eslint") -> Dict[str, str]:
        """
        Executes the formatting and linting of the codebase.

        Parameters:
            directory (str): The directory of the codebase to format and lint.
            preview (bool): Whether to show a preview of the changes before applying.
            formatter (str): The formatter to use.
            linter (str): The linter to use.

        Returns:
            Dict[str, str]: The results of the formatting and linting process.
        """
        if not os.path.isdir(directory):
            raise ValueError(f"The specified directory '{directory}' does not exist.")
        
        results = {}
        if preview:
            results['formatter_preview'] = self.preview_formatting(directory, formatter)
            results['linter_preview'] = self.preview_linting(directory, linter)
        else:
            self.apply_formatting(directory, formatter)
            self.apply_linting(directory, linter)
            results['status'] = "Formatting and linting applied successfully."

        return results

    def preview_formatting(self, directory: str, formatter: str) -> str:
        """
        Previews the changes that would be made by the formatter.

        Parameters:
            directory (str): The directory of the codebase to format.
            formatter (str): The formatter to use.

        Returns:
            str: The preview of the changes.
        """
        try:
            result = subprocess.run([formatter, directory, '--check'], capture_output=True, text=True)
            logging.info("Preview formatting executed successfully.")
            return result.stdout
        except Exception as e:
            logging.error(f"Error during formatting preview: {e}")
            return str(e)

    def apply_formatting(self, directory: str, formatter: str) -> None:
        """
        Applies the formatter to the codebase.

        Parameters:
            directory (str): The directory of the codebase to format.
            formatter (str): The formatter to use.
        """
        try:
            subprocess.run([formatter, directory], check=True)
            logging.info("Formatting applied successfully.")
        except subprocess.CalledProcessError as e:
            logging.error(f"Error during formatting: {e}")
            raise

    def preview_linting(self, directory: str, linter: str) -> str:
        """
        Previews the changes that would be made by the linter.

        Parameters:
            directory (str): The directory of the codebase to lint.
            linter (str): The linter to use.

        Returns:
            str: The preview of the linting results.
        """
        try:
            result = subprocess.run([linter, directory, '--fix-dry-run'], capture_output=True, text=True)
            logging.info("Preview linting executed successfully.")
            return result.stdout
        except Exception as e:
            logging.error(f"Error during linting preview: {e}")
            return str(e)

    def apply_linting(self, directory: str, linter: str) -> None:
        """
        Applies the linter to the codebase.

        Parameters:
            directory (str): The directory of the codebase to lint.
            linter (str): The linter to use.
        """
        try:
            subprocess.run([linter, directory], check=True)
            logging.info("Linting applied successfully.")
        except subprocess.CalledProcessError as e:
            logging.error(f"Error during linting: {e}")
            raise