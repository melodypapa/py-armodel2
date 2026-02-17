"""TcpIpIcmpv6Props AUTOSAR element."""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET
from armodel.serialization import XMLMember

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject


class TcpIpIcmpv6Props(ARObject):
    """AUTOSAR TcpIpIcmpv6Props."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: dict[str, XMLMember] for declarative metadata
    _xml_members: dict[str, "XMLMember"] = {
    }

    def __init__(self) -> None:
        """Initialize TcpIpIcmpv6Props."""
        super().__init__()


class TcpIpIcmpv6PropsBuilder:
    """Builder for TcpIpIcmpv6Props."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: TcpIpIcmpv6Props = TcpIpIcmpv6Props()

    def build(self) -> TcpIpIcmpv6Props:
        """Build and return TcpIpIcmpv6Props object.

        Returns:
            TcpIpIcmpv6Props instance
        """
        # TODO: Add validation
        return self._obj
