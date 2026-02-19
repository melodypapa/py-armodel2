"""AbstractDoIpLogicAddressProps AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 556)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_DoIP.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.identifiable import (
    Identifiable,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from abc import ABC, abstractmethod


class AbstractDoIpLogicAddressProps(Identifiable, ABC):
    """AUTOSAR AbstractDoIpLogicAddressProps."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            True for abstract classes
        """
        return True

    def __init__(self) -> None:
        """Initialize AbstractDoIpLogicAddressProps."""
        super().__init__()
    @classmethod
    def deserialize(cls, element: ET.Element) -> "AbstractDoIpLogicAddressProps":
        """Deserialize XML element to AbstractDoIpLogicAddressProps object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized AbstractDoIpLogicAddressProps object
        """
        # Create instance and initialize with default values
        obj = cls.__new__(cls)
        obj.__init__()

        return obj



class AbstractDoIpLogicAddressPropsBuilder:
    """Builder for AbstractDoIpLogicAddressProps."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: AbstractDoIpLogicAddressProps = AbstractDoIpLogicAddressProps()

    def build(self) -> AbstractDoIpLogicAddressProps:
        """Build and return AbstractDoIpLogicAddressProps object.

        Returns:
            AbstractDoIpLogicAddressProps instance
        """
        # TODO: Add validation
        return self._obj
