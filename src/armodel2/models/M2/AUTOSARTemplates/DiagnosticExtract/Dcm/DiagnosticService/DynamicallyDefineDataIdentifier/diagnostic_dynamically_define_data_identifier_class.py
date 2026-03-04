"""DiagnosticDynamicallyDefineDataIdentifierClass AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (page 128)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_DiagnosticExtract_Dcm_DiagnosticService_DynamicallyDefineDataIdentifier.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional, Any
import xml.etree.ElementTree as ET

from armodel2.models.M2.AUTOSARTemplates.DiagnosticExtract.Dcm.DiagnosticService.CommonService.diagnostic_service_class import (
    DiagnosticServiceClass,
)
from armodel2.models.M2.builder_base import BuilderBase
from armodel2.models.M2.AUTOSARTemplates.DiagnosticExtract.Dcm.DiagnosticService.CommonService.diagnostic_service_class import DiagnosticServiceClassBuilder
from armodel2.models.M2.AUTOSARTemplates.DiagnosticExtract.Dcm.DiagnosticService.DynamicallyDefineData import (
    DiagnosticHandleDDDIConfigurationEnum,
)
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Boolean,
)
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel2.serialization import SerializationHelper


class DiagnosticDynamicallyDefineDataIdentifierClass(DiagnosticServiceClass):
    """AUTOSAR DiagnosticDynamicallyDefineDataIdentifierClass."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    _XML_TAG = "DIAGNOSTIC-DYNAMICALLY-DEFINE-DATA-IDENTIFIER-CLASS"


    check_per: Optional[Boolean]
    configuration: Optional[DiagnosticHandleDDDIConfigurationEnum]
    subfunctions: list[Any]
    _DESERIALIZE_DISPATCH = {
        "CHECK-PER": lambda obj, elem: setattr(obj, "check_per", SerializationHelper.deserialize_by_tag(elem, "Boolean")),
        "CONFIGURATION": lambda obj, elem: setattr(obj, "configuration", DiagnosticHandleDDDIConfigurationEnum.deserialize(elem)),
        "SUBFUNCTIONS": lambda obj, elem: obj.subfunctions.append(SerializationHelper.deserialize_by_tag(elem, "any (DiagnosticDynamically)")),
    }


    def __init__(self) -> None:
        """Initialize DiagnosticDynamicallyDefineDataIdentifierClass."""
        super().__init__()
        self.check_per: Optional[Boolean] = None
        self.configuration: Optional[DiagnosticHandleDDDIConfigurationEnum] = None
        self.subfunctions: list[Any] = []

    def serialize(self) -> ET.Element:
        """Serialize DiagnosticDynamicallyDefineDataIdentifierClass to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Use pre-computed _XML_TAG constant
        elem = ET.Element(self._XML_TAG)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(DiagnosticDynamicallyDefineDataIdentifierClass, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize check_per
        if self.check_per is not None:
            serialized = SerializationHelper.serialize_item(self.check_per, "Boolean")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("CHECK-PER")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize configuration
        if self.configuration is not None:
            serialized = SerializationHelper.serialize_item(self.configuration, "DiagnosticHandleDDDIConfigurationEnum")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("CONFIGURATION")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize subfunctions (list to container "SUBFUNCTIONS")
        if self.subfunctions:
            wrapper = ET.Element("SUBFUNCTIONS")
            for item in self.subfunctions:
                serialized = SerializationHelper.serialize_item(item, "Any")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "DiagnosticDynamicallyDefineDataIdentifierClass":
        """Deserialize XML element to DiagnosticDynamicallyDefineDataIdentifierClass object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized DiagnosticDynamicallyDefineDataIdentifierClass object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(DiagnosticDynamicallyDefineDataIdentifierClass, cls).deserialize(element)

        # Single-pass deserialization with if-elif-else chain
        ns_split = '}'
        for child in element:
            tag = child.tag.split(ns_split, 1)[1] if child.tag.startswith('{') else child.tag
            if tag == "CHECK-PER":
                setattr(obj, "check_per", SerializationHelper.deserialize_by_tag(child, "Boolean"))
            elif tag == "CONFIGURATION":
                setattr(obj, "configuration", DiagnosticHandleDDDIConfigurationEnum.deserialize(child))
            elif tag == "SUBFUNCTIONS":
                # Iterate through wrapper children
                for item_elem in child:
                    obj.subfunctions.append(SerializationHelper.deserialize_by_tag(item_elem, "any (DiagnosticDynamically)"))

        return obj



class DiagnosticDynamicallyDefineDataIdentifierClassBuilder(DiagnosticServiceClassBuilder):
    """Builder for DiagnosticDynamicallyDefineDataIdentifierClass with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: DiagnosticDynamicallyDefineDataIdentifierClass = DiagnosticDynamicallyDefineDataIdentifierClass()


    def with_check_per(self, value: Optional[Boolean]) -> "DiagnosticDynamicallyDefineDataIdentifierClassBuilder":
        """Set check_per attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.check_per = value
        return self

    def with_configuration(self, value: Optional[DiagnosticHandleDDDIConfigurationEnum]) -> "DiagnosticDynamicallyDefineDataIdentifierClassBuilder":
        """Set configuration attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.configuration = value
        return self

    def with_subfunctions(self, items: list[any (DiagnosticDynamically)]) -> "DiagnosticDynamicallyDefineDataIdentifierClassBuilder":
        """Set subfunctions list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.subfunctions = list(items) if items else []
        return self


    def add_subfunction(self, item: any (DiagnosticDynamically)) -> "DiagnosticDynamicallyDefineDataIdentifierClassBuilder":
        """Add a single item to subfunctions list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.subfunctions.append(item)
        return self

    def clear_subfunctions(self) -> "DiagnosticDynamicallyDefineDataIdentifierClassBuilder":
        """Clear all items from subfunctions list.

        Returns:
            self for method chaining
        """
        self._obj.subfunctions = []
        return self


    # Pre-computed validation constants (generated from JSON schema)
    _OPTIONAL_ATTRIBUTES = {
        "checkPer",
        "configuration",
        "subfunction",
    }


    def _validate_instance(self) -> None:
        """Validate the built instance based on settings."""
        from armodel2.core import GlobalSettingsManager, BuilderValidationMode

        settings = GlobalSettingsManager()
        mode = settings.builder_validation

        if mode == BuilderValidationMode.DISABLED:
            return

        # No required attributes to validate (all are optional)


    def build(self) -> DiagnosticDynamicallyDefineDataIdentifierClass:
        """Build and return the DiagnosticDynamicallyDefineDataIdentifierClass instance with validation."""
        self._validate_instance()
        return self._obj