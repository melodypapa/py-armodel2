"""RPortInCompositionInstanceRef AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 952)
  - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (page 459)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SWComponentTemplate_Composition_InstanceRefs.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Composition.InstanceRefs.port_in_composition_type_instance_ref import (
    PortInCompositionTypeInstanceRef,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.serialization import SerializationHelper
from armodel.models.M2.builder_base import BuilderBase
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Composition.InstanceRefs.port_in_composition_type_instance_ref import PortInCompositionTypeInstanceRefBuilder
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Components.abstract_required_port_prototype import (
    AbstractRequiredPortPrototype,
)
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Composition.sw_component_prototype import (
    SwComponentPrototype,
)


class RPortInCompositionInstanceRef(PortInCompositionTypeInstanceRef):
    """AUTOSAR RPortInCompositionInstanceRef."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    context_component_ref: Optional[ARRef]
    target_r_port_ref: Optional[ARRef]
    def __init__(self) -> None:
        """Initialize RPortInCompositionInstanceRef."""
        super().__init__()
        self.context_component_ref: Optional[ARRef] = None
        self.target_r_port_ref: Optional[ARRef] = None

    def serialize(self) -> ET.Element:
        """Serialize RPortInCompositionInstanceRef to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = SerializationHelper.get_xml_tag(self.__class__)
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(RPortInCompositionInstanceRef, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize context_component_ref
        if self.context_component_ref is not None:
            serialized = SerializationHelper.serialize_item(self.context_component_ref, "SwComponentPrototype")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("CONTEXT-COMPONENT-REF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize target_r_port_ref
        if self.target_r_port_ref is not None:
            serialized = SerializationHelper.serialize_item(self.target_r_port_ref, "AbstractRequiredPortPrototype")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("TARGET-R-PORT-REF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "RPortInCompositionInstanceRef":
        """Deserialize XML element to RPortInCompositionInstanceRef object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized RPortInCompositionInstanceRef object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(RPortInCompositionInstanceRef, cls).deserialize(element)

        # Parse context_component_ref
        child = SerializationHelper.find_child_element(element, "CONTEXT-COMPONENT-REF")
        if child is not None:
            context_component_ref_value = ARRef.deserialize(child)
            obj.context_component_ref = context_component_ref_value

        # Parse target_r_port_ref
        child = SerializationHelper.find_child_element(element, "TARGET-R-PORT-REF")
        if child is not None:
            target_r_port_ref_value = ARRef.deserialize(child)
            obj.target_r_port_ref = target_r_port_ref_value

        return obj



class RPortInCompositionInstanceRefBuilder(PortInCompositionTypeInstanceRefBuilder):
    """Builder for RPortInCompositionInstanceRef with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: RPortInCompositionInstanceRef = RPortInCompositionInstanceRef()


    def with_context_component(self, value: Optional[SwComponentPrototype]) -> "RPortInCompositionInstanceRefBuilder":
        """Set context_component attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.context_component = value
        return self

    def with_target_r_port(self, value: Optional[AbstractRequiredPortPrototype]) -> "RPortInCompositionInstanceRefBuilder":
        """Set target_r_port attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.target_r_port = value
        return self




    def _validate_instance(self) -> None:
        """Validate the built instance based on settings."""
        from typing import get_type_hints
        from armodel.core import GlobalSettingsManager, BuilderValidationMode

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


    def build(self) -> RPortInCompositionInstanceRef:
        """Build and return the RPortInCompositionInstanceRef instance with validation."""
        self._validate_instance()
        pass
        return self._obj