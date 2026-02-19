"""BinaryManifestAddressableObject AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 920)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_SoftwareCluster_BinaryManifest.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.identifiable import (
    Identifiable,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Address,
    SymbolString,
)
from abc import ABC, abstractmethod


class BinaryManifestAddressableObject(Identifiable, ABC):
    """AUTOSAR BinaryManifestAddressableObject."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            True for abstract classes
        """
        return True

    address: Optional[Address]
    symbol: Optional[SymbolString]
    def __init__(self) -> None:
        """Initialize BinaryManifestAddressableObject."""
        super().__init__()
        self.address: Optional[Address] = None
        self.symbol: Optional[SymbolString] = None
    @classmethod
    def deserialize(cls, element: ET.Element) -> "BinaryManifestAddressableObject":
        """Deserialize XML element to BinaryManifestAddressableObject object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized BinaryManifestAddressableObject object
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



class BinaryManifestAddressableObjectBuilder:
    """Builder for BinaryManifestAddressableObject."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: BinaryManifestAddressableObject = BinaryManifestAddressableObject()

    def build(self) -> BinaryManifestAddressableObject:
        """Build and return BinaryManifestAddressableObject object.

        Returns:
            BinaryManifestAddressableObject instance
        """
        # TODO: Add validation
        return self._obj
