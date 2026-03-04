"""DiagnosticControlEnableMaskBit AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (page 119)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_DiagnosticExtract_Dcm_DiagnosticService_IOControl.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel2.models.M2.builder_base import BuilderBase
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    PositiveInteger,
)
from armodel2.models.M2.AUTOSARTemplates.DiagnosticExtract.CommonDiagnostics.diagnostic_data_element import (
    DiagnosticDataElement,
)
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel2.serialization import SerializationHelper


class DiagnosticControlEnableMaskBit(ARObject):
    """AUTOSAR DiagnosticControlEnableMaskBit."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    _XML_TAG = "DIAGNOSTIC-CONTROL-ENABLE-MASK-BIT"


    bit_number: Optional[PositiveInteger]
    controlled_data_refs: list[ARRef]
    _DESERIALIZE_DISPATCH = {
        "BIT-NUMBER": lambda obj, elem: setattr(obj, "bit_number", SerializationHelper.deserialize_by_tag(elem, "PositiveInteger")),
        "CONTROLLED-DATA-REFS": lambda obj, elem: [obj.controlled_data_refs.append(ARRef.deserialize(item_elem)) for item_elem in elem],
    }


    def __init__(self) -> None:
        """Initialize DiagnosticControlEnableMaskBit."""
        super().__init__()
        self.bit_number: Optional[PositiveInteger] = None
        self.controlled_data_refs: list[ARRef] = []

    def serialize(self) -> ET.Element:
        """Serialize DiagnosticControlEnableMaskBit to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Use pre-computed _XML_TAG constant
        elem = ET.Element(self._XML_TAG)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(DiagnosticControlEnableMaskBit, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize bit_number
        if self.bit_number is not None:
            serialized = SerializationHelper.serialize_item(self.bit_number, "PositiveInteger")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("BIT-NUMBER")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize controlled_data_refs (list to container "CONTROLLED-DATA-REFS")
        if self.controlled_data_refs:
            wrapper = ET.Element("CONTROLLED-DATA-REFS")
            for item in self.controlled_data_refs:
                serialized = SerializationHelper.serialize_item(item, "DiagnosticDataElement")
                if serialized is not None:
                    child_elem = ET.Element("CONTROLLED-DATA-REF")
                    if hasattr(serialized, 'attrib'):
                        child_elem.attrib.update(serialized.attrib)
                    if serialized.text:
                        child_elem.text = serialized.text
                    for child in serialized:
                        child_elem.append(child)
                    wrapper.append(child_elem)
            if len(wrapper) > 0:
                elem.append(wrapper)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "DiagnosticControlEnableMaskBit":
        """Deserialize XML element to DiagnosticControlEnableMaskBit object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized DiagnosticControlEnableMaskBit object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(DiagnosticControlEnableMaskBit, cls).deserialize(element)

        # Single-pass deserialization with if-elif-else chain
        ns_split = '}'
        for child in element:
            tag = child.tag.split(ns_split, 1)[1] if child.tag.startswith('{') else child.tag
            if tag == "BIT-NUMBER":
                setattr(obj, "bit_number", SerializationHelper.deserialize_by_tag(child, "PositiveInteger"))
            elif tag == "CONTROLLED-DATA-REFS":
                # Iterate through wrapper children
                for item_elem in child:
                    obj.controlled_data_refs.append(ARRef.deserialize(item_elem))

        return obj



class DiagnosticControlEnableMaskBitBuilder(BuilderBase):
    """Builder for DiagnosticControlEnableMaskBit with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: DiagnosticControlEnableMaskBit = DiagnosticControlEnableMaskBit()


    def with_bit_number(self, value: Optional[PositiveInteger]) -> "DiagnosticControlEnableMaskBitBuilder":
        """Set bit_number attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.bit_number = value
        return self

    def with_controlled_datas(self, items: list[DiagnosticDataElement]) -> "DiagnosticControlEnableMaskBitBuilder":
        """Set controlled_datas list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.controlled_datas = list(items) if items else []
        return self


    def add_controlled_data(self, item: DiagnosticDataElement) -> "DiagnosticControlEnableMaskBitBuilder":
        """Add a single item to controlled_datas list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.controlled_datas.append(item)
        return self

    def clear_controlled_datas(self) -> "DiagnosticControlEnableMaskBitBuilder":
        """Clear all items from controlled_datas list.

        Returns:
            self for method chaining
        """
        self._obj.controlled_datas = []
        return self


    # Pre-computed validation constants (generated from JSON schema)
    _OPTIONAL_ATTRIBUTES = {
        "bitNumber",
        "controlledData",
    }


    def _validate_instance(self) -> None:
        """Validate the built instance based on settings."""
        from armodel2.core import GlobalSettingsManager, BuilderValidationMode

        settings = GlobalSettingsManager()
        mode = settings.builder_validation

        if mode == BuilderValidationMode.DISABLED:
            return

        # No required attributes to validate (all are optional)


    def build(self) -> DiagnosticControlEnableMaskBit:
        """Build and return the DiagnosticControlEnableMaskBit instance with validation."""
        self._validate_instance()
        return self._obj