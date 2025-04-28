import pytest
from swarmauri_tool_formatandlintcodebase.FormatAndLintCodebaseTool import FormatAndLintCodebaseTool

@pytest.mark.unit
def test_format_and_lint_codebase_tool_initialization() -> None:
    """Tests the initialization of the FormatAndLintCodebaseTool class."""
    tool = FormatAndLintCodebaseTool()
    
    assert tool.version == "0.1.dev1"
    assert tool.name == "FormatAndLintCodebaseTool"
    assert tool.type == "FormatAndLintCodebaseTool"
    assert "directory" in [param.name for param in tool.parameters]
    assert tool.parameters[0].required is True

@pytest.mark.unit
@pytest.mark.parametrize("directory, expected", [
    ("./valid_directory", {}),  # Assuming this is a valid directory for testing
    ("./invalid_directory", "The specified directory './invalid_directory' does not exist."),
])
def test_call_method(directory: str, expected: str) -> None:
    """Tests the __call__ method of the FormatAndLintCodebaseTool class."""
    tool = FormatAndLintCodebaseTool()
    
    if expected == {}:
        result = tool(directory)
        assert "status" in result
    else:
        with pytest.raises(ValueError) as exc_info:
            tool(directory)
        assert str(exc_info.value) == expected

@pytest.mark.unit
def test_preview_formatting(mocker) -> None:
    """Tests the preview_formatting method."""
    mock_subprocess = mocker.patch("subprocess.run")
    mock_subprocess.return_value.stdout = "Formatted output preview."
    
    tool = FormatAndLintCodebaseTool()
    preview = tool.preview_formatting("./valid_directory", "black")
    
    assert preview == "Formatted output preview."
    mock_subprocess.assert_called_once_with(["black", "./valid_directory", '--check'], capture_output=True, text=True)

@pytest.mark.unit
def test_apply_formatting(mocker) -> None:
    """Tests the apply_formatting method."""
    mock_subprocess = mocker.patch("subprocess.run")
    
    tool = FormatAndLintCodebaseTool()
    tool.apply_formatting("./valid_directory", "black")
    
    mock_subprocess.assert_called_once_with(["black", "./valid_directory"], check=True)

@pytest.mark.unit
def test_preview_linting(mocker) -> None:
    """Tests the preview_linting method."""
    mock_subprocess = mocker.patch("subprocess.run")
    mock_subprocess.return_value.stdout = "Linting output preview."
    
    tool = FormatAndLintCodebaseTool()
    preview = tool.preview_linting("./valid_directory", "eslint")
    
    assert preview == "Linting output preview."
    mock_subprocess.assert_called_once_with(["eslint", "./valid_directory", '--fix-dry-run'], capture_output=True, text=True)

@pytest.mark.unit
def test_apply_linting(mocker) -> None:
    """Tests the apply_linting method."""
    mock_subprocess = mocker.patch("subprocess.run")
    
    tool = FormatAndLintCodebaseTool()
    tool.apply_linting("./valid_directory", "eslint")
    
    mock_subprocess.assert_called_once_with(["eslint", "./valid_directory"], check=True)