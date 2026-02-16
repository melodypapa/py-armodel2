"""CompositeNetworkRepresentation AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ar_object import ARObject


class CompositeNetworkRepresentation(ARObject):
    """AUTOSAR CompositeNetworkRepresentation."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("leaf_element_element_in_port_interface_instance_ref", None, False, False, any (ApplicationComposite)),  # leafElementElementInPortInterfaceInstanceRef
        ("network_representation", None, False, False, any (SwDataDefPropsRepresentation)),  # networkRepresentation
    ]

    def __init__(self) -> None:
        """Initialize CompositeNetworkRepresentation."""
        super().__init__()
        self.leaf_element_element_in_port_interface_instance_ref: Optional[Any] = None
        self.network_representation: Optional[Any] = None

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert CompositeNetworkRepresentation to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "CompositeNetworkRepresentation":
        """Create CompositeNetworkRepresentation from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            CompositeNetworkRepresentation instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to CompositeNetworkRepresentation since parent returns ARObject
        return cast("CompositeNetworkRepresentation", obj)


class CompositeNetworkRepresentationBuilder:
    """Builder for CompositeNetworkRepresentation."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: CompositeNetworkRepresentation = CompositeNetworkRepresentation()

    def build(self) -> CompositeNetworkRepresentation:
        """Build and return CompositeNetworkRepresentation object.

        Returns:
            CompositeNetworkRepresentation instance
        """
        # TODO: Add validation
        return self._obj
