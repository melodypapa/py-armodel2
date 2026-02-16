"""BufferProperties AUTOSAR element."""

from typing import Optional
import xml.etree.ElementTree as ET
from armodel.serialization import XMLMember

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Boolean,
    Integer,
)


class BufferProperties(ARObject):
    """AUTOSAR BufferProperties."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: dict[str, XMLMember] for declarative metadata
    _xml_members: dict[str, "XMLMember"] = {
        "header_length": XMLMember(
            xml_tag=None,
            is_attribute=True,
            multiplicity="0..1",
        ),  # headerLength
        "in_place": XMLMember(
            xml_tag=None,
            is_attribute=True,
            multiplicity="0..1",
        ),  # inPlace
    }

    def __init__(self) -> None:
        """Initialize BufferProperties."""
        super().__init__()
        self.header_length: Optional[Integer] = None
        self.in_place: Optional[Boolean] = None


class BufferPropertiesBuilder:
    """Builder for BufferProperties."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: BufferProperties = BufferProperties()

    def build(self) -> BufferProperties:
        """Build and return BufferProperties object.

        Returns:
            BufferProperties instance
        """
        # TODO: Add validation
        return self._obj
