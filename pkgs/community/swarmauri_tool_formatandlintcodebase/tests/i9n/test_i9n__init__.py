import pytest
import logging
from swarmauri_tool_formatandlintcodebase import __init__ as package_init

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

@pytest.mark.i9n
def test_package_initializer() -> None:
    """Test the package initializer for swarmauri_tool_formatandlintcodebase.

    This test ensures that the __init__.py in the source folder loads
    correctly without any import errors.
    """
    try:
        # Attempt to access the package attributes to ensure they are loaded
        assert hasattr(package_init, '__version__'), "Package version attribute is missing."
        logger.info("Package version loaded successfully: %s", package_init.__version__)
        
        # Check if any expected classes or functions are accessible
        # For example, if there's a class called FormatAndLintCodebaseTool
        assert hasattr(package_init, 'FormatAndLintCodebaseTool'), "FormatAndLintCodebaseTool is missing."
        logger.info("FormatAndLintCodebaseTool class loaded successfully.")

    except Exception as e:
        logger.error("Error loading package initializer: %s", str(e))
        pytest.fail(f"Package initializer failed to load: {str(e)}")