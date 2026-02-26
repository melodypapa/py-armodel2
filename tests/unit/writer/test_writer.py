"""Unit tests for ARXMLWriter class."""

import pytest

from armodel2.writer import ARXMLWriter
from armodel2.models.M2.AUTOSARTemplates.AutosarTopLevelStructure.autosar import AUTOSAR


class TestARXMLWriter:
    """Unit tests for ARXMLWriter class."""

    @pytest.fixture(autouse=True)
    def setup(self):
        """Setup test fixtures."""
        self.autosar = AUTOSAR()
        self.writer = ARXMLWriter(pretty_print=True)
        self.writer_compact = ARXMLWriter(pretty_print=False)
