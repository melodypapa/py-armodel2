"""StreamFilterPortRange AUTOSAR element."""

from typing import Optional
import xml.etree.ElementTree as ET
from armodel.serialization import XMLMember

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    PositiveInteger,
)


class StreamFilterPortRange(ARObject):
    """AUTOSAR StreamFilterPortRange."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: dict[str, XMLMember] for declarative metadata
    _xml_members: dict[str, "XMLMember"] = {
        "max": XMLMember(
            xml_tag=None,
            is_attribute=True,
            multiplicity="0..1",
        ),  # max
        "min": XMLMember(
            xml_tag=None,
            is_attribute=True,
            multiplicity="0..1",
        ),  # min
    }

    def __init__(self) -> None:
        """Initialize StreamFilterPortRange."""
        super().__init__()
        self.max: Optional[PositiveInteger] = None
        self.min: Optional[PositiveInteger] = None


class StreamFilterPortRangeBuilder:
    """Builder for StreamFilterPortRange."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: StreamFilterPortRange = StreamFilterPortRange()

    def build(self) -> StreamFilterPortRange:
        """Build and return StreamFilterPortRange object.

        Returns:
            StreamFilterPortRange instance
        """
        # TODO: Add validation
        return self._obj
