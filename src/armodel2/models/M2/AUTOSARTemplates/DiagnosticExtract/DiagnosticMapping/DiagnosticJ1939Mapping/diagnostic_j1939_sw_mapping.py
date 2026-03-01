"""DiagnosticJ1939SwMapping AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (page 268)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_DiagnosticExtract_DiagnosticMapping_DiagnosticJ1939Mapping.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel2.models.M2.AUTOSARTemplates.DiagnosticExtract.DiagnosticMapping.diagnostic_sw_mapping import (
    DiagnosticSwMapping,
)
from armodel2.models.M2.builder_base import BuilderBase
from armodel2.models.M2.AUTOSARTemplates.DiagnosticExtract.DiagnosticMapping.diagnostic_sw_mapping import DiagnosticSwMappingBuilder
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel2.models.M2.AUTOSARTemplates.DiagnosticExtract.J1939.diagnostic_j1939_node import (
    DiagnosticJ1939Node,
)
from armodel2.models.M2.AUTOSARTemplates.SWComponentTemplate.Composition.sw_component_prototype import (
    SwComponentPrototype,
)
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel2.serialization import SerializationHelper


class DiagnosticJ1939SwMapping(DiagnosticSwMapping):
    """AUTOSAR DiagnosticJ1939SwMapping."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    _XML_TAG = "DIAGNOSTIC-J1939-SW-MAPPING"


    node_ref: Optional[ARRef]
    sw_component_prototype_composition_instance_ref: Optional[ARRef]
    _DESERIALIZE_DISPATCH = {
        "NODE-REF": lambda obj, elem: setattr(obj, "node_ref", ARRef.deserialize(elem)),
        "SW-COMPONENT-PROTOTYPE-COMPOSITION-INSTANCE-REF-REF": lambda obj, elem: setattr(obj, "sw_component_prototype_composition_instance_ref", ARRef.deserialize(elem)),
    }


    def __init__(self) -> None:
        """Initialize DiagnosticJ1939SwMapping."""
        super().__init__()
        self.node_ref: Optional[ARRef] = None
        self.sw_component_prototype_composition_instance_ref: Optional[ARRef] = None

    def serialize(self) -> ET.Element:
        """Serialize DiagnosticJ1939SwMapping to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Use pre-computed _XML_TAG constant
        elem = ET.Element(self._XML_TAG)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(DiagnosticJ1939SwMapping, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize node_ref
        if self.node_ref is not None:
            serialized = SerializationHelper.serialize_item(self.node_ref, "DiagnosticJ1939Node")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("NODE-REF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize sw_component_prototype_composition_instance_ref
        if self.sw_component_prototype_composition_instance_ref is not None:
            serialized = SerializationHelper.serialize_item(self.sw_component_prototype_composition_instance_ref, "SwComponentPrototype")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("SW-COMPONENT-PROTOTYPE-COMPOSITION-INSTANCE-REF-REF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "DiagnosticJ1939SwMapping":
        """Deserialize XML element to DiagnosticJ1939SwMapping object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized DiagnosticJ1939SwMapping object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(DiagnosticJ1939SwMapping, cls).deserialize(element)

        # Single-pass deserialization with if-elif-else chain
        ns_split = '}'
        for child in element:
            tag = child.tag.split(ns_split, 1)[1] if child.tag.startswith('{') else child.tag
            child_tag = tag  # Alias for polymorphic type checking
            if tag == "NODE-REF":
                setattr(obj, "node_ref", ARRef.deserialize(child))
            elif tag == "SW-COMPONENT-PROTOTYPE-COMPOSITION-INSTANCE-REF-REF":
                setattr(obj, "sw_component_prototype_composition_instance_ref", ARRef.deserialize(child))

        return obj



class DiagnosticJ1939SwMappingBuilder(DiagnosticSwMappingBuilder):
    """Builder for DiagnosticJ1939SwMapping with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: DiagnosticJ1939SwMapping = DiagnosticJ1939SwMapping()


    def with_node(self, value: Optional[DiagnosticJ1939Node]) -> "DiagnosticJ1939SwMappingBuilder":
        """Set node attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.node = value
        return self

    def with_sw_component_prototype_composition_instance_ref(self, value: Optional[SwComponentPrototype]) -> "DiagnosticJ1939SwMappingBuilder":
        """Set sw_component_prototype_composition_instance_ref attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.sw_component_prototype_composition_instance_ref = value
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


    def build(self) -> DiagnosticJ1939SwMapping:
        """Build and return the DiagnosticJ1939SwMapping instance with validation."""
        self._validate_instance()
        pass
        return self._obj