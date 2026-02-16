"""SenderRecArrayElementMapping AUTOSAR element."""

from typing import Optional
import xml.etree.ElementTree as ET
from armodel.serialization import XMLMember

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.DataMapping.indexed_array_element import (
    IndexedArrayElement,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.DataMapping.sender_rec_composite_type_mapping import (
    SenderRecCompositeTypeMapping,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreCommunication.system_signal import (
    SystemSignal,
)


class SenderRecArrayElementMapping(ARObject):
    """AUTOSAR SenderRecArrayElementMapping."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: dict[str, XMLMember] for declarative metadata
    _xml_members: dict[str, "XMLMember"] = {
        "complex_type": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=SenderRecCompositeTypeMapping,
        ),  # complexType
        "indexed_array": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=IndexedArrayElement,
        ),  # indexedArray
        "system_signal": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=SystemSignal,
        ),  # systemSignal
    }

    def __init__(self) -> None:
        """Initialize SenderRecArrayElementMapping."""
        super().__init__()
        self.complex_type: Optional[SenderRecCompositeTypeMapping] = None
        self.indexed_array: Optional[IndexedArrayElement] = None
        self.system_signal: Optional[SystemSignal] = None


class SenderRecArrayElementMappingBuilder:
    """Builder for SenderRecArrayElementMapping."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: SenderRecArrayElementMapping = SenderRecArrayElementMapping()

    def build(self) -> SenderRecArrayElementMapping:
        """Build and return SenderRecArrayElementMapping object.

        Returns:
            SenderRecArrayElementMapping instance
        """
        # TODO: Add validation
        return self._obj
