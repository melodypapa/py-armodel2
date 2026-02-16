"""TargetIPduRef AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Multiplatform.pdu_mapping_default_value import (
    PduMappingDefaultValue,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreCommunication.pdu_triggering import (
    PduTriggering,
)


class TargetIPduRef(ARObject):
    """AUTOSAR TargetIPduRef."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("default_value", None, False, False, PduMappingDefaultValue),  # defaultValue
        ("target_i_pdu", None, False, False, PduTriggering),  # targetIPdu
    ]

    def __init__(self) -> None:
        """Initialize TargetIPduRef."""
        super().__init__()
        self.default_value: Optional[PduMappingDefaultValue] = None
        self.target_i_pdu: Optional[PduTriggering] = None

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert TargetIPduRef to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "TargetIPduRef":
        """Create TargetIPduRef from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            TargetIPduRef instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to TargetIPduRef since parent returns ARObject
        return cast("TargetIPduRef", obj)


class TargetIPduRefBuilder:
    """Builder for TargetIPduRef."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: TargetIPduRef = TargetIPduRef()

    def build(self) -> TargetIPduRef:
        """Build and return TargetIPduRef object.

        Returns:
            TargetIPduRef instance
        """
        # TODO: Add validation
        return self._obj
