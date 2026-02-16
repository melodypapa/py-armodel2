"""DataDumpEntry AUTOSAR element."""

from typing import Optional
import xml.etree.ElementTree as ET
from armodel.serialization import XMLMember

from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Lin.LinCommunication.lin_configuration_entry import (
    LinConfigurationEntry,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Integer,
)


class DataDumpEntry(LinConfigurationEntry):
    """AUTOSAR DataDumpEntry."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: dict[str, XMLMember] for declarative metadata
    _xml_members: dict[str, "XMLMember"] = {
        "byte_values": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="*",
        ),  # byteValues
    }

    def __init__(self) -> None:
        """Initialize DataDumpEntry."""
        super().__init__()
        self.byte_values: list[Integer] = []


class DataDumpEntryBuilder:
    """Builder for DataDumpEntry."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: DataDumpEntry = DataDumpEntry()

    def build(self) -> DataDumpEntry:
        """Build and return DataDumpEntry object.

        Returns:
            DataDumpEntry instance
        """
        # TODO: Add validation
        return self._obj
