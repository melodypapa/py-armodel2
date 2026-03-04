"""TlvDataIdDefinitionSet AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 830)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_Transformer.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage.ar_element import (
    ARElement,
)
from armodel2.models.M2.builder_base import BuilderBase
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage.ar_element import ARElementBuilder
from armodel2.models.M2.AUTOSARTemplates.SystemTemplate.Transformer.tlv_data_id_definition import (
    TlvDataIdDefinition,
)
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel2.serialization import SerializationHelper


class TlvDataIdDefinitionSet(ARElement):
    """AUTOSAR TlvDataIdDefinitionSet."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    _XML_TAG = "TLV-DATA-ID-DEFINITION-SET"


    tlv_data_ids: list[TlvDataIdDefinition]
    _DESERIALIZE_DISPATCH = {
        "TLV-DATA-IDS": lambda obj, elem: obj.tlv_data_ids.append(SerializationHelper.deserialize_by_tag(elem, "TlvDataIdDefinition")),
    }


    def __init__(self) -> None:
        """Initialize TlvDataIdDefinitionSet."""
        super().__init__()
        self.tlv_data_ids: list[TlvDataIdDefinition] = []

    def serialize(self) -> ET.Element:
        """Serialize TlvDataIdDefinitionSet to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Use pre-computed _XML_TAG constant
        elem = ET.Element(self._XML_TAG)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(TlvDataIdDefinitionSet, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize tlv_data_ids (list to container "TLV-DATA-IDS")
        if self.tlv_data_ids:
            wrapper = ET.Element("TLV-DATA-IDS")
            for item in self.tlv_data_ids:
                serialized = SerializationHelper.serialize_item(item, "TlvDataIdDefinition")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "TlvDataIdDefinitionSet":
        """Deserialize XML element to TlvDataIdDefinitionSet object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized TlvDataIdDefinitionSet object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(TlvDataIdDefinitionSet, cls).deserialize(element)

        # Single-pass deserialization with if-elif-else chain
        ns_split = '}'
        for child in element:
            tag = child.tag.split(ns_split, 1)[1] if child.tag.startswith('{') else child.tag
            if tag == "TLV-DATA-IDS":
                # Iterate through wrapper children
                for item_elem in child:
                    obj.tlv_data_ids.append(SerializationHelper.deserialize_by_tag(item_elem, "TlvDataIdDefinition"))

        return obj



class TlvDataIdDefinitionSetBuilder(ARElementBuilder):
    """Builder for TlvDataIdDefinitionSet with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: TlvDataIdDefinitionSet = TlvDataIdDefinitionSet()


    def with_tlv_data_ids(self, items: list[TlvDataIdDefinition]) -> "TlvDataIdDefinitionSetBuilder":
        """Set tlv_data_ids list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.tlv_data_ids = list(items) if items else []
        return self


    def add_tlv_data_id(self, item: TlvDataIdDefinition) -> "TlvDataIdDefinitionSetBuilder":
        """Add a single item to tlv_data_ids list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.tlv_data_ids.append(item)
        return self

    def clear_tlv_data_ids(self) -> "TlvDataIdDefinitionSetBuilder":
        """Clear all items from tlv_data_ids list.

        Returns:
            self for method chaining
        """
        self._obj.tlv_data_ids = []
        return self


    # Pre-computed validation constants (generated from JSON schema)
    _OPTIONAL_ATTRIBUTES = {
        "tlvDataId",
    }


    def _validate_instance(self) -> None:
        """Validate the built instance based on settings."""
        from armodel2.core import GlobalSettingsManager, BuilderValidationMode

        settings = GlobalSettingsManager()
        mode = settings.builder_validation

        if mode == BuilderValidationMode.DISABLED:
            return

        # No required attributes to validate (all are optional)


    def build(self) -> TlvDataIdDefinitionSet:
        """Build and return the TlvDataIdDefinitionSet instance with validation."""
        self._validate_instance()
        return self._obj