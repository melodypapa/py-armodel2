"""EthTcpIpIcmpProps AUTOSAR element."""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET
from armodel.serialization import XMLMember

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject


class EthTcpIpIcmpProps(ARElement):
    """AUTOSAR EthTcpIpIcmpProps."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: dict[str, XMLMember] for declarative metadata
    _xml_members: dict[str, "XMLMember"] = {
    }

    def __init__(self) -> None:
        """Initialize EthTcpIpIcmpProps."""
        super().__init__()


class EthTcpIpIcmpPropsBuilder:
    """Builder for EthTcpIpIcmpProps."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: EthTcpIpIcmpProps = EthTcpIpIcmpProps()

    def build(self) -> EthTcpIpIcmpProps:
        """Build and return EthTcpIpIcmpProps object.

        Returns:
            EthTcpIpIcmpProps instance
        """
        # TODO: Add validation
        return self._obj
