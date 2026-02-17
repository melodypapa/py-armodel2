"""SwBitRepresentation AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 333)

JSON Source: docs/json/packages/M2_MSR_DataDictionary_DataDefProperties.classes.json"""

from typing import Optional
import xml.etree.ElementTree as ET
from armodel.serialization import XMLMember

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Integer,
)


class SwBitRepresentation(ARObject):
    """AUTOSAR SwBitRepresentation."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: dict[str, XMLMember] for declarative metadata
    _xml_members: dict[str, "XMLMember"] = {
        "bit_position": XMLMember(
            xml_tag=None,
            is_attribute=True,
            multiplicity="0..1",
        ),  # bitPosition
        "number_of_bits": XMLMember(
            xml_tag=None,
            is_attribute=True,
            multiplicity="0..1",
        ),  # numberOfBits
    }

    def __init__(self) -> None:
        """Initialize SwBitRepresentation."""
        super().__init__()
        self.bit_position: Optional[Integer] = None
        self.number_of_bits: Optional[Integer] = None


class SwBitRepresentationBuilder:
    """Builder for SwBitRepresentation."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: SwBitRepresentation = SwBitRepresentation()

    def build(self) -> SwBitRepresentation:
        """Build and return SwBitRepresentation object.

        Returns:
            SwBitRepresentation instance
        """
        # TODO: Add validation
        return self._obj
