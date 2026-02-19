"""ImplementationProps AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf (page 86)
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 287)
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 2033)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_CommonStructure_Implementation.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.referrable import (
    Referrable,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    CIdentifier,
)
from abc import ABC, abstractmethod


class ImplementationProps(Referrable, ABC):
    """AUTOSAR ImplementationProps."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            True for abstract classes
        """
        return True

    symbol: Optional[CIdentifier]
    def __init__(self) -> None:
        """Initialize ImplementationProps."""
        super().__init__()
        self.symbol: Optional[CIdentifier] = None
    @classmethod
    def deserialize(cls, element: ET.Element) -> "ImplementationProps":
        """Deserialize XML element to ImplementationProps object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized ImplementationProps object
        """
        # Create instance and initialize with default values
        obj = cls.__new__(cls)
        obj.__init__()

        # Parse symbol
        child = ARObject._find_child_element(element, "SYMBOL")
        if child is not None:
            symbol_value = child.text
            obj.symbol = symbol_value

        return obj



class ImplementationPropsBuilder:
    """Builder for ImplementationProps."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: ImplementationProps = ImplementationProps()

    def build(self) -> ImplementationProps:
        """Build and return ImplementationProps object.

        Returns:
            ImplementationProps instance
        """
        # TODO: Add validation
        return self._obj
