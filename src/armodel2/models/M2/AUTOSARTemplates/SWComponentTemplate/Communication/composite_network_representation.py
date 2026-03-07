"""CompositeNetworkRepresentation AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 181)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SWComponentTemplate_Communication.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional, Any
import xml.etree.ElementTree as ET

from armodel2.models.M2.builder_base import BuilderBase
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel2.serialization import SerializationHelper


class CompositeNetworkRepresentation(ARObject):
    """AUTOSAR CompositeNetworkRepresentation."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    _XML_TAG = "COMPOSITE-NETWORK-REPRESENTATION"


    leaf_element_element_in_port_interface_instance_ref: Optional[Any]
    network_representation: Optional[Any]
    _DESERIALIZE_DISPATCH = {
        "LEAF-ELEMENT-ELEMENT-IN-PORT-INTERFACE-INSTANCE-REF": lambda obj, elem: setattr(obj, "leaf_element_element_in_port_interface_instance_ref", SerializationHelper.deserialize_by_tag(elem, "any (ApplicationComposite)")),
        "NETWORK-REPRESENTATION": lambda obj, elem: setattr(obj, "network_representation", SerializationHelper.deserialize_by_tag(elem, "any (SwDataDefPropsRepresentation)")),
    }


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
        # Use pre-computed _XML_TAG constant
        elem = ET.Element(self._XML_TAG)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(CompositeNetworkRepresentation, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize leaf_element_element_in_port_interface_instance_ref
        if self.leaf_element_element_in_port_interface_instance_ref is not None:
            serialized = SerializationHelper.serialize_item(self.leaf_element_element_in_port_interface_instance_ref, "Any")
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
            serialized = SerializationHelper.serialize_item(self.network_representation, "Any")
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
        # First, call parent's deserialize to handle inherited attributes
        obj = super(CompositeNetworkRepresentation, cls).deserialize(element)

        # Single-pass deserialization with if-elif-else chain
        ns_split = '}'
        for child in element:
            tag = child.tag.split(ns_split, 1)[1] if child.tag.startswith('{') else child.tag
            if tag == "LEAF-ELEMENT-ELEMENT-IN-PORT-INTERFACE-INSTANCE-REF":
                setattr(obj, "leaf_element_element_in_port_interface_instance_ref", SerializationHelper.deserialize_by_tag(child, "any (ApplicationComposite)"))
            elif tag == "NETWORK-REPRESENTATION":
                setattr(obj, "network_representation", SerializationHelper.deserialize_by_tag(child, "any (SwDataDefPropsRepresentation)"))

        return obj



class CompositeNetworkRepresentationBuilder(BuilderBase):
    """Builder for CompositeNetworkRepresentation with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: CompositeNetworkRepresentation = CompositeNetworkRepresentation()


    def with_leaf_element_element_in_port_interface_instance_ref(self, value: Optional[Any]) -> "CompositeNetworkRepresentationBuilder":
        """Set leaf_element_element_in_port_interface_instance_ref attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute 'leaf_element_element_in_port_interface_instance_ref' is required and cannot be None")
        self._obj.leaf_element_element_in_port_interface_instance_ref = value
        return self

    def with_network_representation(self, value: Optional[Any]) -> "CompositeNetworkRepresentationBuilder":
        """Set network_representation attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute 'network_representation' is required and cannot be None")
        self._obj.network_representation = value
        return self



    # Pre-computed validation constants (generated from JSON schema)
    _OPTIONAL_ATTRIBUTES = {
        "leafElementElementInPortInterfaceInstanceRef",
        "networkRepresentation",
    }


    def _validate_instance(self) -> None:
        """Validate the built instance based on settings."""
        from armodel2.core import GlobalSettingsManager, BuilderValidationMode

        settings = GlobalSettingsManager()
        mode = settings.builder_validation

        if mode == BuilderValidationMode.DISABLED:
            return

        # No required attributes to validate (all are optional)


    def build(self) -> CompositeNetworkRepresentation:
        """Build and return the CompositeNetworkRepresentation instance with validation."""
        self._validate_instance()
        return self._obj