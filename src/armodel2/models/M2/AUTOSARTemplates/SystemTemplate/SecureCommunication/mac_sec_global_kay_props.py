"""MacSecGlobalKayProps AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 174)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_SecureCommunication.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage.ar_element import (
    ARElement,
)
from armodel2.models.M2.builder_base import BuilderBase
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage.ar_element import ARElementBuilder
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    PositiveInteger,
)
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel2.serialization import SerializationHelper


class MacSecGlobalKayProps(ARElement):
    """AUTOSAR MacSecGlobalKayProps."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    _XML_TAG = "MAC-SEC-GLOBAL-KAY-PROPS"


    bypass_ether: PositiveInteger
    bypass_vlan: PositiveInteger
    _DESERIALIZE_DISPATCH = {
        "BYPASS-ETHER": lambda obj, elem: setattr(obj, "bypass_ether", SerializationHelper.deserialize_by_tag(elem, "PositiveInteger")),
        "BYPASS-VLAN": lambda obj, elem: setattr(obj, "bypass_vlan", SerializationHelper.deserialize_by_tag(elem, "PositiveInteger")),
    }


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
        # Use pre-computed _XML_TAG constant
        elem = ET.Element(self._XML_TAG)

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

        # Single-pass deserialization with if-elif-else chain
        ns_split = '}'
        for child in element:
            tag = child.tag.split(ns_split, 1)[1] if child.tag.startswith('{') else child.tag
            if tag == "BYPASS-ETHER":
                setattr(obj, "bypass_ether", SerializationHelper.deserialize_by_tag(child, "PositiveInteger"))
            elif tag == "BYPASS-VLAN":
                setattr(obj, "bypass_vlan", SerializationHelper.deserialize_by_tag(child, "PositiveInteger"))

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



    # Pre-computed validation constants (generated from JSON schema)
    _REQUIRED_ATTRIBUTES = {
        "bypassEther",
        "bypassVlan",
    }


    def _validate_instance(self) -> None:
        """Validate the built instance based on settings."""
        from armodel2.core import GlobalSettingsManager, BuilderValidationMode

        settings = GlobalSettingsManager()
        mode = settings.builder_validation

        if mode == BuilderValidationMode.DISABLED:
            return

        # Validate required attributes using pre-computed constants (O(1) lookup)
        # This is much faster than calling get_type_hints() at runtime
        if getattr(self._obj, "bypassEther", None) is None:
            if mode == BuilderValidationMode.STRICT:
                raise ValueError("Required attribute 'bypassEther' is None")
            elif mode == BuilderValidationMode.LENIENT:
                import warnings
                warnings.warn("Required attribute 'bypassEther' is None", UserWarning)
        if getattr(self._obj, "bypassVlan", None) is None:
            if mode == BuilderValidationMode.STRICT:
                raise ValueError("Required attribute 'bypassVlan' is None")
            elif mode == BuilderValidationMode.LENIENT:
                import warnings
                warnings.warn("Required attribute 'bypassVlan' is None", UserWarning)


    def build(self) -> MacSecGlobalKayProps:
        """Build and return the MacSecGlobalKayProps instance with validation."""
        self._validate_instance()
        return self._obj