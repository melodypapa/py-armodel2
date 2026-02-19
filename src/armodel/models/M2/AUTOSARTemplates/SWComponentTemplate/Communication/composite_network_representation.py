"""CompositeNetworkRepresentation AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 181)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SWComponentTemplate_Communication.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional, Any
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject


class CompositeNetworkRepresentation(ARObject):
    """AUTOSAR CompositeNetworkRepresentation."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    leaf_element_element_in_port_interface_instance_ref: Optional[Any]
    network_representation: Optional[Any]
    def __init__(self) -> None:
        """Initialize CompositeNetworkRepresentation."""
        super().__init__()
        self.leaf_element_element_in_port_interface_instance_ref: Optional[Any] = None
        self.network_representation: Optional[Any] = None
    def serialize(self) -> ET.Element:
        """Serialize CompositeNetworkRepresentation to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = self._get_xml_tag()
        elem = ET.Element(tag)

        # Serialize leaf_element_element_in_port_interface_instance_ref
        if self.leaf_element_element_in_port_interface_instance_ref is not None:
            serialized = ARObject._serialize_item(self.leaf_element_element_in_port_interface_instance_ref, "Any")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("LEAF-ELEMENT-ELEMENT-IN-PORT-INTERFACE-INSTANCE-REF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize network_representation
        if self.network_representation is not None:
            serialized = ARObject._serialize_item(self.network_representation, "Any")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("NETWORK-REPRESENTATION")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "CompositeNetworkRepresentation":
        """Deserialize XML element to CompositeNetworkRepresentation object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized CompositeNetworkRepresentation object
        """
        # Create instance and initialize with default values
        obj = cls.__new__(cls)
        obj.__init__()

        # Parse leaf_element_element_in_port_interface_instance_ref
        child = ARObject._find_child_element(element, "LEAF-ELEMENT-ELEMENT-IN-PORT-INTERFACE-INSTANCE-REF")
        if child is not None:
            leaf_element_element_in_port_interface_instance_ref_value = child.text
            obj.leaf_element_element_in_port_interface_instance_ref = leaf_element_element_in_port_interface_instance_ref_value

        # Parse network_representation
        child = ARObject._find_child_element(element, "NETWORK-REPRESENTATION")
        if child is not None:
            network_representation_value = child.text
            obj.network_representation = network_representation_value

        return obj



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
