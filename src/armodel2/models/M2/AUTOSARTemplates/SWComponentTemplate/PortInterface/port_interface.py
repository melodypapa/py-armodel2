"""PortInterface AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (page 326)
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 87)
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 2046)
  - AUTOSAR_FO_TPS_AbstractPlatformSpecification.pdf (page 27)
  - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (page 457)
  - AUTOSAR_FO_TPS_StandardizationTemplate.pdf (page 200)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SWComponentTemplate_PortInterface.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage.ar_element import (
    ARElement,
)
from armodel2.models.M2.builder_base import BuilderBase
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage.ar_element import ARElementBuilder
from armodel2.models.M2.AUTOSARTemplates.CommonStructure.ServiceNeeds import (
    ServiceProviderEnum,
)
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Boolean,
)
from abc import ABC, abstractmethod
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel2.serialization import SerializationHelper


class PortInterface(ARElement, ABC):
    """AUTOSAR PortInterface."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            True for abstract classes
        """
        return True

    is_service: Optional[Boolean]
    service_kind: Optional[ServiceProviderEnum]
    def __init__(self) -> None:
        """Initialize PortInterface."""
        super().__init__()
        self.is_service: Optional[Boolean] = None
        self.service_kind: Optional[ServiceProviderEnum] = None

    def serialize(self) -> ET.Element:
        """Serialize PortInterface to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = SerializationHelper.get_xml_tag(self.__class__)
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(PortInterface, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize is_service
        if self.is_service is not None:
            serialized = SerializationHelper.serialize_item(self.is_service, "Boolean")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("IS-SERVICE")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize service_kind
        if self.service_kind is not None:
            serialized = SerializationHelper.serialize_item(self.service_kind, "ServiceProviderEnum")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("SERVICE-KIND")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "PortInterface":
        """Deserialize XML element to PortInterface object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized PortInterface object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(PortInterface, cls).deserialize(element)

        # Parse is_service
        child = SerializationHelper.find_child_element(element, "IS-SERVICE")
        if child is not None:
            is_service_value = child.text
            obj.is_service = is_service_value

        # Parse service_kind
        child = SerializationHelper.find_child_element(element, "SERVICE-KIND")
        if child is not None:
            service_kind_value = ServiceProviderEnum.deserialize(child)
            obj.service_kind = service_kind_value

        return obj



class PortInterfaceBuilder(ARElementBuilder):
    """Builder for PortInterface with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: PortInterface = PortInterface()


    def with_is_service(self, value: Optional[Boolean]) -> "PortInterfaceBuilder":
        """Set is_service attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.is_service = value
        return self

    def with_service_kind(self, value: Optional[ServiceProviderEnum]) -> "PortInterfaceBuilder":
        """Set service_kind attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.service_kind = value
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


    @abstractmethod
    def build(self) -> PortInterface:
        """Build and return the PortInterface instance (abstract)."""
        raise NotImplementedError