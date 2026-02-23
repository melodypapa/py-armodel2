"""DelegationSwConnector AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 80)
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 2016)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SWComponentTemplate_Composition.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Composition.sw_connector import (
    SwConnector,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.serialization import SerializationHelper
from armodel.models.M2.builder_base import BuilderBase
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Composition.sw_connector import SwConnectorBuilder
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Composition.InstanceRefs.port_in_composition_type_instance_ref import (
    PortInCompositionTypeInstanceRef,
)
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Components.port_prototype import (
    PortPrototype,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.serialization import SerializationHelper


class DelegationSwConnector(SwConnector):
    """AUTOSAR DelegationSwConnector."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    inner_port_iref: Optional[PortInCompositionTypeInstanceRef]
    outer_port_ref: Optional[ARRef]
    def __init__(self) -> None:
        """Initialize DelegationSwConnector."""
        super().__init__()
        self.inner_port_iref: Optional[PortInCompositionTypeInstanceRef] = None
        self.outer_port_ref: Optional[ARRef] = None

    def serialize(self) -> ET.Element:
        """Serialize DelegationSwConnector to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = SerializationHelper.get_xml_tag(self.__class__)
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(DelegationSwConnector, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize inner_port_iref (instance reference with wrapper "INNER-PORT-IREF")
        if self.inner_port_iref is not None:
            serialized = SerializationHelper.serialize_item(self.inner_port_iref, "PortInCompositionTypeInstanceRef")
            if serialized is not None:
                # Wrap in IREF wrapper element
                iref_wrapper = ET.Element("INNER-PORT-IREF")
                # Append the serialized element as a child (don't flatten it)
                iref_wrapper.append(serialized)
                elem.append(iref_wrapper)

        # Serialize outer_port_ref
        if self.outer_port_ref is not None:
            serialized = SerializationHelper.serialize_item(self.outer_port_ref, "PortPrototype")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("OUTER-PORT-REF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "DelegationSwConnector":
        """Deserialize XML element to DelegationSwConnector object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized DelegationSwConnector object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(DelegationSwConnector, cls).deserialize(element)

        # Parse inner_port_iref (instance reference from wrapper "INNER-PORT-IREF")
        wrapper = SerializationHelper.find_child_element(element, "INNER-PORT-IREF")
        if wrapper is not None:
            # Get the first child element (the actual reference)
            children = list(wrapper)
            if children:
                inner_elem = children[0]
                inner_port_iref_value = SerializationHelper.deserialize_by_tag(inner_elem)
                obj.inner_port_iref = inner_port_iref_value

        # Parse outer_port_ref
        child = SerializationHelper.find_child_element(element, "OUTER-PORT-REF")
        if child is not None:
            outer_port_ref_value = ARRef.deserialize(child)
            obj.outer_port_ref = outer_port_ref_value

        return obj



class DelegationSwConnectorBuilder(SwConnectorBuilder):
    """Builder for DelegationSwConnector with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: DelegationSwConnector = DelegationSwConnector()


    def with_inner_port(self, value: Optional[PortInCompositionTypeInstanceRef]) -> "DelegationSwConnectorBuilder":
        """Set inner_port attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.inner_port = value
        return self

    def with_outer_port(self, value: Optional[PortPrototype]) -> "DelegationSwConnectorBuilder":
        """Set outer_port attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.outer_port = value
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


    def build(self) -> DelegationSwConnector:
        """Build and return the DelegationSwConnector instance with validation."""
        self._validate_instance()
        pass
        return self._obj