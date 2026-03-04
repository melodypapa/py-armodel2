"""DiagnosticParameterIdentifier AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (page 149)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_DiagnosticExtract_CommonDiagnostics.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel2.models.M2.AUTOSARTemplates.DiagnosticExtract.CommonDiagnostics.diagnostic_common_element import (
    DiagnosticCommonElement,
)
from armodel2.models.M2.builder_base import BuilderBase
from armodel2.models.M2.AUTOSARTemplates.DiagnosticExtract.CommonDiagnostics.diagnostic_common_element import DiagnosticCommonElementBuilder
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    PositiveInteger,
)
from armodel2.models.M2.AUTOSARTemplates.DiagnosticExtract.CommonDiagnostics.diagnostic_parameter import (
    DiagnosticParameter,
)
from armodel2.models.M2.AUTOSARTemplates.DiagnosticExtract.CommonDiagnostics.diagnostic_support_info_byte import (
    DiagnosticSupportInfoByte,
)
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel2.serialization import SerializationHelper


class DiagnosticParameterIdentifier(DiagnosticCommonElement):
    """AUTOSAR DiagnosticParameterIdentifier."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    _XML_TAG = "DIAGNOSTIC-PARAMETER-IDENTIFIER"


    data_elements: list[DiagnosticParameter]
    id: Optional[PositiveInteger]
    pid_size: Optional[PositiveInteger]
    support_info_byte: Optional[DiagnosticSupportInfoByte]
    _DESERIALIZE_DISPATCH = {
        "DATA-ELEMENTS": lambda obj, elem: obj.data_elements.append(SerializationHelper.deserialize_by_tag(elem, "DiagnosticParameter")),
        "ID": lambda obj, elem: setattr(obj, "id", SerializationHelper.deserialize_by_tag(elem, "PositiveInteger")),
        "PID-SIZE": lambda obj, elem: setattr(obj, "pid_size", SerializationHelper.deserialize_by_tag(elem, "PositiveInteger")),
        "SUPPORT-INFO-BYTE": lambda obj, elem: setattr(obj, "support_info_byte", SerializationHelper.deserialize_by_tag(elem, "DiagnosticSupportInfoByte")),
    }


    def __init__(self) -> None:
        """Initialize DiagnosticParameterIdentifier."""
        super().__init__()
        self.data_elements: list[DiagnosticParameter] = []
        self.id: Optional[PositiveInteger] = None
        self.pid_size: Optional[PositiveInteger] = None
        self.support_info_byte: Optional[DiagnosticSupportInfoByte] = None

    def serialize(self) -> ET.Element:
        """Serialize DiagnosticParameterIdentifier to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Use pre-computed _XML_TAG constant
        elem = ET.Element(self._XML_TAG)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(DiagnosticParameterIdentifier, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize data_elements (list to container "DATA-ELEMENTS")
        if self.data_elements:
            wrapper = ET.Element("DATA-ELEMENTS")
            for item in self.data_elements:
                serialized = SerializationHelper.serialize_item(item, "DiagnosticParameter")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize id
        if self.id is not None:
            serialized = SerializationHelper.serialize_item(self.id, "PositiveInteger")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("ID")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize pid_size
        if self.pid_size is not None:
            serialized = SerializationHelper.serialize_item(self.pid_size, "PositiveInteger")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("PID-SIZE")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize support_info_byte
        if self.support_info_byte is not None:
            serialized = SerializationHelper.serialize_item(self.support_info_byte, "DiagnosticSupportInfoByte")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("SUPPORT-INFO-BYTE")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "DiagnosticParameterIdentifier":
        """Deserialize XML element to DiagnosticParameterIdentifier object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized DiagnosticParameterIdentifier object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(DiagnosticParameterIdentifier, cls).deserialize(element)

        # Single-pass deserialization with if-elif-else chain
        ns_split = '}'
        for child in element:
            tag = child.tag.split(ns_split, 1)[1] if child.tag.startswith('{') else child.tag
            if tag == "DATA-ELEMENTS":
                # Iterate through wrapper children
                for item_elem in child:
                    obj.data_elements.append(SerializationHelper.deserialize_by_tag(item_elem, "DiagnosticParameter"))
            elif tag == "ID":
                setattr(obj, "id", SerializationHelper.deserialize_by_tag(child, "PositiveInteger"))
            elif tag == "PID-SIZE":
                setattr(obj, "pid_size", SerializationHelper.deserialize_by_tag(child, "PositiveInteger"))
            elif tag == "SUPPORT-INFO-BYTE":
                setattr(obj, "support_info_byte", SerializationHelper.deserialize_by_tag(child, "DiagnosticSupportInfoByte"))

        return obj



class DiagnosticParameterIdentifierBuilder(DiagnosticCommonElementBuilder):
    """Builder for DiagnosticParameterIdentifier with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: DiagnosticParameterIdentifier = DiagnosticParameterIdentifier()


    def with_data_elements(self, items: list[DiagnosticParameter]) -> "DiagnosticParameterIdentifierBuilder":
        """Set data_elements list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.data_elements = list(items) if items else []
        return self

    def with_id(self, value: Optional[PositiveInteger]) -> "DiagnosticParameterIdentifierBuilder":
        """Set id attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.id = value
        return self

    def with_pid_size(self, value: Optional[PositiveInteger]) -> "DiagnosticParameterIdentifierBuilder":
        """Set pid_size attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.pid_size = value
        return self

    def with_support_info_byte(self, value: Optional[DiagnosticSupportInfoByte]) -> "DiagnosticParameterIdentifierBuilder":
        """Set support_info_byte attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.support_info_byte = value
        return self


    def add_data_element(self, item: DiagnosticParameter) -> "DiagnosticParameterIdentifierBuilder":
        """Add a single item to data_elements list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.data_elements.append(item)
        return self

    def clear_data_elements(self) -> "DiagnosticParameterIdentifierBuilder":
        """Clear all items from data_elements list.

        Returns:
            self for method chaining
        """
        self._obj.data_elements = []
        return self


    # Pre-computed validation constants (generated from JSON schema)
    _OPTIONAL_ATTRIBUTES = {
        "dataElement",
        "id",
        "pidSize",
        "supportInfoByte",
    }


    def _validate_instance(self) -> None:
        """Validate the built instance based on settings."""
        from armodel2.core import GlobalSettingsManager, BuilderValidationMode

        settings = GlobalSettingsManager()
        mode = settings.builder_validation

        if mode == BuilderValidationMode.DISABLED:
            return

        # No required attributes to validate (all are optional)


    def build(self) -> DiagnosticParameterIdentifier:
        """Build and return the DiagnosticParameterIdentifier instance with validation."""
        self._validate_instance()
        return self._obj