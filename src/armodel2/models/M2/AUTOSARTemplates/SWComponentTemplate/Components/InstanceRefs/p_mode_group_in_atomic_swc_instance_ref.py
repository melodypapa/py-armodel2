"""PModeGroupInAtomicSwcInstanceRef AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 949)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SWComponentTemplate_Components_InstanceRefs.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel2.models.M2.AUTOSARTemplates.SWComponentTemplate.Components.InstanceRefs.mode_group_in_atomic_swc_instance_ref import (
    ModeGroupInAtomicSwcInstanceRef,
)
from armodel2.models.M2.builder_base import BuilderBase
from armodel2.models.M2.AUTOSARTemplates.SWComponentTemplate.Components.InstanceRefs.mode_group_in_atomic_swc_instance_ref import ModeGroupInAtomicSwcInstanceRefBuilder
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel2.models.M2.AUTOSARTemplates.SWComponentTemplate.Components.abstract_provided_port_prototype import (
    AbstractProvidedPortPrototype,
)
from armodel2.models.M2.AUTOSARTemplates.CommonStructure.ModeDeclaration.mode_declaration_group import (
    ModeDeclarationGroup,
)
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel2.serialization import SerializationHelper


class PModeGroupInAtomicSwcInstanceRef(ModeGroupInAtomicSwcInstanceRef):
    """AUTOSAR PModeGroupInAtomicSwcInstanceRef."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    _XML_TAG = "P-MODE-GROUP-IN-ATOMIC-SWC-INSTANCE-REF"


    context_p_port_ref: Optional[ARRef]
    target_mode_ref: Optional[ARRef]
    _DESERIALIZE_DISPATCH = {
        "CONTEXT-P-PORT-REF": ("_POLYMORPHIC", "context_p_port_ref", ["PPortPrototype", "PRPortPrototype"]),
        "TARGET-MODE-REF": lambda obj, elem: setattr(obj, "target_mode_ref", ARRef.deserialize(elem)),
    }


    def __init__(self) -> None:
        """Initialize PModeGroupInAtomicSwcInstanceRef."""
        super().__init__()
        self.context_p_port_ref: Optional[ARRef] = None
        self.target_mode_ref: Optional[ARRef] = None

    def serialize(self) -> ET.Element:
        """Serialize PModeGroupInAtomicSwcInstanceRef to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Use pre-computed _XML_TAG constant
        elem = ET.Element(self._XML_TAG)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(PModeGroupInAtomicSwcInstanceRef, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize context_p_port_ref
        if self.context_p_port_ref is not None:
            serialized = SerializationHelper.serialize_item(self.context_p_port_ref, "AbstractProvidedPortPrototype")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("CONTEXT-P-PORT-REF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize target_mode_ref
        if self.target_mode_ref is not None:
            serialized = SerializationHelper.serialize_item(self.target_mode_ref, "ModeDeclarationGroup")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("TARGET-MODE-REF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "PModeGroupInAtomicSwcInstanceRef":
        """Deserialize XML element to PModeGroupInAtomicSwcInstanceRef object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized PModeGroupInAtomicSwcInstanceRef object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(PModeGroupInAtomicSwcInstanceRef, cls).deserialize(element)

        # Single-pass deserialization with if-elif-else chain
        ns_split = '}'
        for child in element:
            tag = child.tag.split(ns_split, 1)[1] if child.tag.startswith('{') else child.tag
            if tag == "CONTEXT-P-PORT-REF":
                setattr(obj, "context_p_port_ref", ARRef.deserialize(child))
            elif tag == "TARGET-MODE-REF":
                setattr(obj, "target_mode_ref", ARRef.deserialize(child))

        return obj



class PModeGroupInAtomicSwcInstanceRefBuilder(ModeGroupInAtomicSwcInstanceRefBuilder):
    """Builder for PModeGroupInAtomicSwcInstanceRef with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: PModeGroupInAtomicSwcInstanceRef = PModeGroupInAtomicSwcInstanceRef()


    def with_context_p_port(self, value: Optional[AbstractProvidedPortPrototype]) -> "PModeGroupInAtomicSwcInstanceRefBuilder":
        """Set context_p_port attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.context_p_port = value
        return self

    def with_target_mode(self, value: Optional[ModeDeclarationGroup]) -> "PModeGroupInAtomicSwcInstanceRefBuilder":
        """Set target_mode attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.target_mode = value
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


    def build(self) -> PModeGroupInAtomicSwcInstanceRef:
        """Build and return the PModeGroupInAtomicSwcInstanceRef instance with validation."""
        self._validate_instance()
        pass
        return self._obj