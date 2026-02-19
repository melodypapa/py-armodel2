"""MacSecGlobalKayProps AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 174)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_SecureCommunication.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage.ar_element import (
    ARElement,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    PositiveInteger,
)


class MacSecGlobalKayProps(ARElement):
    """AUTOSAR MacSecGlobalKayProps."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    bypass_ether: PositiveInteger
    bypass_vlan: PositiveInteger
    def __init__(self) -> None:
        """Initialize MacSecGlobalKayProps."""
        super().__init__()
        self.bypass_ether: PositiveInteger = None
        self.bypass_vlan: PositiveInteger = None
    @classmethod
    def deserialize(cls, element: ET.Element) -> "MacSecGlobalKayProps":
        """Deserialize XML element to MacSecGlobalKayProps object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized MacSecGlobalKayProps object
        """
        # Create instance and initialize with default values
        obj = cls.__new__(cls)
        obj.__init__()

        # Parse bypass_ether
        child = ARObject._find_child_element(element, "BYPASS-ETHER")
        if child is not None:
            bypass_ether_value = child.text
            obj.bypass_ether = bypass_ether_value

        # Parse bypass_vlan
        child = ARObject._find_child_element(element, "BYPASS-VLAN")
        if child is not None:
            bypass_vlan_value = child.text
            obj.bypass_vlan = bypass_vlan_value

        return obj



class MacSecGlobalKayPropsBuilder:
    """Builder for MacSecGlobalKayProps."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: MacSecGlobalKayProps = MacSecGlobalKayProps()

    def build(self) -> MacSecGlobalKayProps:
        """Build and return MacSecGlobalKayProps object.

        Returns:
            MacSecGlobalKayProps instance
        """
        # TODO: Add validation
        return self._obj
