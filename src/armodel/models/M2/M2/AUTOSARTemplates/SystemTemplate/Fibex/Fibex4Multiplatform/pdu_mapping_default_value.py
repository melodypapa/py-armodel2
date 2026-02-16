"""PduMappingDefaultValue AUTOSAR element."""

from typing import Optional
import xml.etree.ElementTree as ET
from armodel.serialization import XMLMember

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Multiplatform.default_value_element import (
    DefaultValueElement,
)


class PduMappingDefaultValue(ARObject):
    """AUTOSAR PduMappingDefaultValue."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: dict[str, XMLMember] for declarative metadata
    _xml_members: dict[str, "XMLMember"] = {
        "default_values": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="*",
            element_class=DefaultValueElement,
        ),  # defaultValues
    }

    def __init__(self) -> None:
        """Initialize PduMappingDefaultValue."""
        super().__init__()
        self.default_values: list[DefaultValueElement] = []


class PduMappingDefaultValueBuilder:
    """Builder for PduMappingDefaultValue."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: PduMappingDefaultValue = PduMappingDefaultValue()

    def build(self) -> PduMappingDefaultValue:
        """Build and return PduMappingDefaultValue object.

        Returns:
            PduMappingDefaultValue instance
        """
        # TODO: Add validation
        return self._obj
