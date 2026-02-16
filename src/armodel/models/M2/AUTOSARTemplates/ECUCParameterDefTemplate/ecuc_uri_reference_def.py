"""EcucUriReferenceDef AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.ECUCParameterDefTemplate.ecuc_abstract_internal_reference_def import (
    EcucAbstractInternalReferenceDef,
)
from armodel.models.M2.AUTOSARTemplates.ECUCParameterDefTemplate.ecuc_destination_uri_def import (
    EcucDestinationUriDef,
)


class EcucUriReferenceDef(EcucAbstractInternalReferenceDef):
    """AUTOSAR EcucUriReferenceDef."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("destination_uri", None, False, False, EcucDestinationUriDef),  # destinationUri
    ]

    def __init__(self) -> None:
        """Initialize EcucUriReferenceDef."""
        super().__init__()
        self.destination_uri: Optional[EcucDestinationUriDef] = None

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert EcucUriReferenceDef to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "EcucUriReferenceDef":
        """Create EcucUriReferenceDef from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            EcucUriReferenceDef instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to EcucUriReferenceDef since parent returns ARObject
        return cast("EcucUriReferenceDef", obj)


class EcucUriReferenceDefBuilder:
    """Builder for EcucUriReferenceDef."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: EcucUriReferenceDef = EcucUriReferenceDef()

    def build(self) -> EcucUriReferenceDef:
        """Build and return EcucUriReferenceDef object.

        Returns:
            EcucUriReferenceDef instance
        """
        # TODO: Add validation
        return self._obj
