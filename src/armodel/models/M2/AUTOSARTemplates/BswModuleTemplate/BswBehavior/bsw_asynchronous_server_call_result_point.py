"""BswAsynchronousServerCallResultPoint AUTOSAR element."""

from typing import Optional
import xml.etree.ElementTree as ET
from armodel.serialization import XMLMember

from armodel.models.M2.AUTOSARTemplates.BswModuleTemplate.BswBehavior.bsw_module_call_point import (
    BswModuleCallPoint,
)


class BswAsynchronousServerCallResultPoint(BswModuleCallPoint):
    """AUTOSAR BswAsynchronousServerCallResultPoint."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: dict[str, XMLMember] for declarative metadata
    _xml_members: dict[str, "XMLMember"] = {
        "asynchronous": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=any (BswAsynchronous),
        ),  # asynchronous
    }

    def __init__(self) -> None:
        """Initialize BswAsynchronousServerCallResultPoint."""
        super().__init__()
        self.asynchronous: Optional[Any] = None


class BswAsynchronousServerCallResultPointBuilder:
    """Builder for BswAsynchronousServerCallResultPoint."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: BswAsynchronousServerCallResultPoint = BswAsynchronousServerCallResultPoint()

    def build(self) -> BswAsynchronousServerCallResultPoint:
        """Build and return BswAsynchronousServerCallResultPoint object.

        Returns:
            BswAsynchronousServerCallResultPoint instance
        """
        # TODO: Add validation
        return self._obj
