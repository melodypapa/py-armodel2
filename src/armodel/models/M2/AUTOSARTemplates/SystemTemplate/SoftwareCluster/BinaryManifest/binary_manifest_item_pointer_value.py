"""BinaryManifestItemPointerValue AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 922)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_SoftwareCluster_BinaryManifest.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.SystemTemplate.SoftwareCluster.BinaryManifest.binary_manifest_item_value import (
    BinaryManifestItemValue,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.serialization import SerializationHelper
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Address,
    SymbolString,
)


class BinaryManifestItemPointerValue(BinaryManifestItemValue):
    """AUTOSAR BinaryManifestItemPointerValue."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    address: Optional[Address]
    symbol: Optional[SymbolString]
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
        # Get XML tag name for this class
        tag = SerializationHelper.get_xml_tag(self.__class__)
        elem = ET.Element(tag)

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

        # Parse address
        child = SerializationHelper.find_child_element(element, "ADDRESS")
        if child is not None:
            address_value = child.text
            obj.address = address_value

        # Parse symbol
        child = SerializationHelper.find_child_element(element, "SYMBOL")
        if child is not None:
            symbol_value = SerializationHelper.deserialize_by_tag(child, "SymbolString")
            obj.symbol = symbol_value

        return obj



class BinaryManifestItemPointerValueBuilder:
    """Builder for BinaryManifestItemPointerValue."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: BinaryManifestItemPointerValue = BinaryManifestItemPointerValue()

    def build(self) -> BinaryManifestItemPointerValue:
        """Build and return BinaryManifestItemPointerValue object.

        Returns:
            BinaryManifestItemPointerValue instance
        """
        # TODO: Add validation
        return self._obj
