"""MacSecGlobalKayProps AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 174)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_SecureCommunication.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage.ar_element import (
    ARElement,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.serialization import SerializationHelper
from armodel.models.M2.builder_base import BuilderBase
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage.ar_element import ARElementBuilder
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    PositiveInteger,
)


class MacSecGlobalKayProps(ARElement):
    """AUTOSAR MacSecGlobalKayProps."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    bypass_ether: PositiveInteger
    bypass_vlan: PositiveInteger
    def __init__(self) -> None:
        """Initialize MacSecGlobalKayProps."""
        super().__init__()
        self.bypass_ether: PositiveInteger = None
        self.bypass_vlan: PositiveInteger = None

    def serialize(self) -> ET.Element:
        """Serialize MacSecGlobalKayProps to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = SerializationHelper.get_xml_tag(self.__class__)
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(MacSecGlobalKayProps, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize bypass_ether
        if self.bypass_ether is not None:
            serialized = SerializationHelper.serialize_item(self.bypass_ether, "PositiveInteger")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("BYPASS-ETHER")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize bypass_vlan
        if self.bypass_vlan is not None:
            serialized = SerializationHelper.serialize_item(self.bypass_vlan, "PositiveInteger")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("BYPASS-VLAN")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "MacSecGlobalKayProps":
        """Deserialize XML element to MacSecGlobalKayProps object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized MacSecGlobalKayProps object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(MacSecGlobalKayProps, cls).deserialize(element)

        # Parse bypass_ether
        child = SerializationHelper.find_child_element(element, "BYPASS-ETHER")
        if child is not None:
            bypass_ether_value = child.text
            obj.bypass_ether = bypass_ether_value

        # Parse bypass_vlan
        child = SerializationHelper.find_child_element(element, "BYPASS-VLAN")
        if child is not None:
            bypass_vlan_value = child.text
            obj.bypass_vlan = bypass_vlan_value

        return obj



class MacSecGlobalKayPropsBuilder(ARElementBuilder):
    """Builder for MacSecGlobalKayProps with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: MacSecGlobalKayProps = MacSecGlobalKayProps()


    def with_bypass_ether(self, value: PositiveInteger) -> "MacSecGlobalKayPropsBuilder":
        """Set bypass_ether attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not False:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.bypass_ether = value
        return self

    def with_bypass_vlan(self, value: PositiveInteger) -> "MacSecGlobalKayPropsBuilder":
        """Set bypass_vlan attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not False:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.bypass_vlan = value
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


    def build(self) -> MacSecGlobalKayProps:
        """Build and return the MacSecGlobalKayProps instance with validation."""
        self._validate_instance()
        pass
        return self._obj