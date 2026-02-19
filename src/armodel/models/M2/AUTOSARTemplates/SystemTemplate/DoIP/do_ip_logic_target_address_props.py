"""DoIpLogicTargetAddressProps AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 556)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_DoIP.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.SystemTemplate.DoIP.abstract_do_ip_logic_address_props import (
    AbstractDoIpLogicAddressProps,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject


class DoIpLogicTargetAddressProps(AbstractDoIpLogicAddressProps):
    """AUTOSAR DoIpLogicTargetAddressProps."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    def __init__(self) -> None:
        """Initialize DoIpLogicTargetAddressProps."""
        super().__init__()
    @classmethod
    def deserialize(cls, element: ET.Element) -> "DoIpLogicTargetAddressProps":
        """Deserialize XML element to DoIpLogicTargetAddressProps object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized DoIpLogicTargetAddressProps object
        """
        # Delegate to parent class to handle inherited attributes
        return super(DoIpLogicTargetAddressProps, cls).deserialize(element)



class DoIpLogicTargetAddressPropsBuilder:
    """Builder for DoIpLogicTargetAddressProps."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: DoIpLogicTargetAddressProps = DoIpLogicTargetAddressProps()

    def build(self) -> DoIpLogicTargetAddressProps:
        """Build and return DoIpLogicTargetAddressProps object.

        Returns:
            DoIpLogicTargetAddressProps instance
        """
        # TODO: Add validation
        return self._obj
