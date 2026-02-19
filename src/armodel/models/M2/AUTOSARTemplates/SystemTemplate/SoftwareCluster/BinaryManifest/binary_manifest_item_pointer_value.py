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
    @classmethod
    def deserialize(cls, element: ET.Element) -> "BinaryManifestItemPointerValue":
        """Deserialize XML element to BinaryManifestItemPointerValue object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized BinaryManifestItemPointerValue object
        """
        # Create instance and initialize with default values
        obj = cls.__new__(cls)
        obj.__init__()

        # Parse address
        child = ARObject._find_child_element(element, "ADDRESS")
        if child is not None:
            address_value = child.text
            obj.address = address_value

        # Parse symbol
        child = ARObject._find_child_element(element, "SYMBOL")
        if child is not None:
            symbol_value = child.text
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
