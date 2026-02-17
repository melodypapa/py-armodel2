"""AsynchronousServerCallResultPoint AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf (page 304)
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 581)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SWComponentTemplate_SwcInternalBehavior_ServerCall.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET
from armodel.serialization import XMLMember

from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.SwcInternalBehavior.AccessCount.abstract_access_point import (
    AbstractAccessPoint,
)


class AsynchronousServerCallResultPoint(AbstractAccessPoint):
    """AUTOSAR AsynchronousServerCallResultPoint."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: dict[str, XMLMember] for declarative metadata
    _xml_members: dict[str, "XMLMember"] = {
        "asynchronous_server": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=any (AsynchronousServer),
        ),  # asynchronousServer
    }

    def __init__(self) -> None:
        """Initialize AsynchronousServerCallResultPoint."""
        super().__init__()
        self.asynchronous_server: Optional[Any] = None


class AsynchronousServerCallResultPointBuilder:
    """Builder for AsynchronousServerCallResultPoint."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: AsynchronousServerCallResultPoint = AsynchronousServerCallResultPoint()

    def build(self) -> AsynchronousServerCallResultPoint:
        """Build and return AsynchronousServerCallResultPoint object.

        Returns:
            AsynchronousServerCallResultPoint instance
        """
        # TODO: Add validation
        return self._obj
