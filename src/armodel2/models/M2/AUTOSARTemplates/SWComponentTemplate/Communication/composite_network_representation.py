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
        tag = SerializationHelper.get_xml_tag(self.__class__)
        elem = ET.Element(tag)

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

        # Parse leaf_element_element_in_port_interface_instance_ref
        child = SerializationHelper.find_child_element(element, "LEAF-ELEMENT-ELEMENT-IN-PORT-INTERFACE-INSTANCE-REF")
        if child is not None:
            leaf_element_element_in_port_interface_instance_ref_value = child.text
            obj.leaf_element_element_in_port_interface_instance_ref = leaf_element_element_in_port_interface_instance_ref_value

        # Parse network_representation
        child = SerializationHelper.find_child_element(element, "NETWORK-REPRESENTATION")
        if child is not None:
            network_representation_value = child.text
            obj.network_representation = network_representation_value

        return obj



class CompositeNetworkRepresentationBuilder(BuilderBase):
    """Builder for CompositeNetworkRepresentation with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: CompositeNetworkRepresentation = CompositeNetworkRepresentation()


    def with_leaf_element_element_in_port_interface_instance_ref(self, value: Optional[any (ApplicationComposite)]) -> "CompositeNetworkRepresentationBuilder":
        """Set leaf_element_element_in_port_interface_instance_ref attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.leaf_element_element_in_port_interface_instance_ref = value
        return self

    def with_network_representation(self, value: Optional[any (SwDataDefPropsRepresentation)]) -> "CompositeNetworkRepresentationBuilder":
        """Set network_representation attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.network_representation = value
        return self




    def _validate_instance(self) -> None:
        """Validate the built instance based on settings."""
        from typing import get_type_hints
        from armodel2.core import GlobalSettingsManager, BuilderValidationMode

        settings = GlobalSettingsManager()
        mode = settings.builder_validation

        if mode == BuilderValidationMode.DISABLED:
            return

        # Get type hints for the class
        try:
            type_hints_dict = get_type_hints(type(self._obj))
        except Exception:
            # Cannot resolve type hints (e.g., forward references), skip validation
            return

        for attr_name, attr_type in type_hints_dict.items():
            if attr_name.startswith("_"):
                continue

            value = getattr(self._obj, attr_name)

            # Check required fields (not Optional)
            if value is None and not self._is_optional_type(attr_type):
                if mode == BuilderValidationMode.STRICT:
                    raise ValueError(
                        f"Required attribute '{attr_name}' is None"
                    )
                elif mode == BuilderValidationMode.LENIENT:
                    import warnings
                    warnings.warn(
                        f"Required attribute '{attr_name}' is None",
                        UserWarning
                    )

    @staticmethod
    def _is_optional_type(type_hint: Any) -> bool:
        """Check if a type hint is Optional.

        Args:
            type_hint: Type hint to check

        Returns:
            True if type is Optional, False otherwise
        """
        origin = getattr(type_hint, "__origin__", None)
        return origin is Union

    @staticmethod
    def _get_expected_type(type_hint: Any) -> type:
        """Extract expected type from type hint.

        Args:
            type_hint: Type hint to extract from

        Returns:
            Expected type
        """
        if isinstance(type_hint, str):
            return object
        origin = getattr(type_hint, "__origin__", None)
        if origin is Union:
            args = getattr(type_hint, "__args__", [])
            for arg in args:
                if arg is not type(None):
                    return arg
        elif origin is list:
            args = getattr(type_hint, "__args__", [object])
            return args[0] if args else object
        return type_hint if isinstance(type_hint, type) else object


    def build(self) -> CompositeNetworkRepresentation:
        """Build and return the CompositeNetworkRepresentation instance with validation."""
        self._validate_instance()
        pass
        return self._obj