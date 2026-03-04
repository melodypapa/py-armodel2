"""BinaryManifestItemPointerValue AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 922)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_SoftwareCluster_BinaryManifest.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel2.models.M2.AUTOSARTemplates.SystemTemplate.SoftwareCluster.BinaryManifest.binary_manifest_item_value import (
    BinaryManifestItemValue,
)
from armodel2.models.M2.builder_base import BuilderBase
from armodel2.models.M2.AUTOSARTemplates.SystemTemplate.SoftwareCluster.BinaryManifest.binary_manifest_item_value import BinaryManifestItemValueBuilder
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Address,
    SymbolString,
)
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel2.serialization import SerializationHelper


class BinaryManifestItemPointerValue(BinaryManifestItemValue):
    """AUTOSAR BinaryManifestItemPointerValue."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    _XML_TAG = "BINARY-MANIFEST-ITEM-POINTER-VALUE"


    address: Optional[Address]
    symbol: Optional[SymbolString]
    _DESERIALIZE_DISPATCH = {
        "ADDRESS": lambda obj, elem: setattr(obj, "address", SerializationHelper.deserialize_by_tag(elem, "Address")),
        "SYMBOL": lambda obj, elem: setattr(obj, "symbol", SerializationHelper.deserialize_by_tag(elem, "SymbolString")),
    }


    def __init__(self) -> None:
        """Initialize BinaryManifestItemPointerValue."""
        super().__init__()
        self.address: Optional[Address] = None
        self.symbol: Optional[SymbolString] = None

    def serialize(self) -> ET.Element:
        """Serialize BinaryManifestItemPointerValue to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Use pre-computed _XML_TAG constant
        elem = ET.Element(self._XML_TAG)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(BinaryManifestItemPointerValue, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize address
        if self.address is not None:
            serialized = SerializationHelper.serialize_item(self.address, "Address")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("ADDRESS")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize symbol
        if self.symbol is not None:
            serialized = SerializationHelper.serialize_item(self.symbol, "SymbolString")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("SYMBOL")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "BinaryManifestItemPointerValue":
        """Deserialize XML element to BinaryManifestItemPointerValue object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized BinaryManifestItemPointerValue object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(BinaryManifestItemPointerValue, cls).deserialize(element)

        # Single-pass deserialization with if-elif-else chain
        ns_split = '}'
        for child in element:
            tag = child.tag.split(ns_split, 1)[1] if child.tag.startswith('{') else child.tag
            if tag == "ADDRESS":
                setattr(obj, "address", SerializationHelper.deserialize_by_tag(child, "Address"))
            elif tag == "SYMBOL":
                setattr(obj, "symbol", SerializationHelper.deserialize_by_tag(child, "SymbolString"))

        return obj



class BinaryManifestItemPointerValueBuilder(BinaryManifestItemValueBuilder):
    """Builder for BinaryManifestItemPointerValue with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: BinaryManifestItemPointerValue = BinaryManifestItemPointerValue()


    def with_address(self, value: Optional[Address]) -> "BinaryManifestItemPointerValueBuilder":
        """Set address attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.address = value
        return self

    def with_symbol(self, value: Optional[SymbolString]) -> "BinaryManifestItemPointerValueBuilder":
        """Set symbol attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.symbol = value
        return self



    # Pre-computed validation constants (generated from JSON schema)
    _OPTIONAL_ATTRIBUTES = {
        "address",
        "symbol",
    }


    def _validate_instance(self) -> None:
        """Validate the built instance based on settings."""
        from armodel2.core import GlobalSettingsManager, BuilderValidationMode

        settings = GlobalSettingsManager()
        mode = settings.builder_validation

        if mode == BuilderValidationMode.DISABLED:
            return

        # No required attributes to validate (all are optional)


    def build(self) -> BinaryManifestItemPointerValue:
        """Build and return the BinaryManifestItemPointerValue instance with validation."""
        self._validate_instance()
        return self._obj