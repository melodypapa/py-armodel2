"""EthTcpIpProps AUTOSAR element."""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET
from armodel.serialization import XMLMember

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject


class EthTcpIpProps(ARElement):
    """AUTOSAR EthTcpIpProps."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: dict[str, XMLMember] for declarative metadata
    _xml_members: dict[str, "XMLMember"] = {
    }

    def __init__(self) -> None:
        """Initialize EthTcpIpProps."""
        super().__init__()


class EthTcpIpPropsBuilder:
    """Builder for EthTcpIpProps."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: EthTcpIpProps = EthTcpIpProps()

    def build(self) -> EthTcpIpProps:
        """Build and return EthTcpIpProps object.

        Returns:
            EthTcpIpProps instance
        """
        # TODO: Add validation
        return self._obj
