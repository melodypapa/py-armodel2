"""CpSoftwareClusterCommunicationResourceProps AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ar_object import ARObject


class CpSoftwareClusterCommunicationResourceProps(ARObject):
    """AUTOSAR CpSoftwareClusterCommunicationResourceProps."""
    """Abstract base class - do not instantiate directly."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
    ]

    def __init__(self) -> None:
        """Initialize CpSoftwareClusterCommunicationResourceProps."""
        super().__init__()

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert CpSoftwareClusterCommunicationResourceProps to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "CpSoftwareClusterCommunicationResourceProps":
        """Create CpSoftwareClusterCommunicationResourceProps from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            CpSoftwareClusterCommunicationResourceProps instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to CpSoftwareClusterCommunicationResourceProps since parent returns ARObject
        return cast("CpSoftwareClusterCommunicationResourceProps", obj)


class CpSoftwareClusterCommunicationResourcePropsBuilder:
    """Builder for CpSoftwareClusterCommunicationResourceProps."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: CpSoftwareClusterCommunicationResourceProps = CpSoftwareClusterCommunicationResourceProps()

    def build(self) -> CpSoftwareClusterCommunicationResourceProps:
        """Build and return CpSoftwareClusterCommunicationResourceProps object.

        Returns:
            CpSoftwareClusterCommunicationResourceProps instance
        """
        # TODO: Add validation
        return self._obj
