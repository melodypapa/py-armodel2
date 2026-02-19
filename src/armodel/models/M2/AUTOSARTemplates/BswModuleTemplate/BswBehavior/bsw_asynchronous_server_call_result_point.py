"""BswAsynchronousServerCallResultPoint AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf (page 80)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_BswModuleTemplate_BswBehavior.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional, Any
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.BswModuleTemplate.BswBehavior.bsw_module_call_point import (
    BswModuleCallPoint,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject


class BswAsynchronousServerCallResultPoint(BswModuleCallPoint):
    """AUTOSAR BswAsynchronousServerCallResultPoint."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    asynchronous: Optional[Any]
    def __init__(self) -> None:
        """Initialize BswAsynchronousServerCallResultPoint."""
        super().__init__()
        self.asynchronous: Optional[Any] = None
    @classmethod
    def deserialize(cls, element: ET.Element) -> "BswAsynchronousServerCallResultPoint":
        """Deserialize XML element to BswAsynchronousServerCallResultPoint object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized BswAsynchronousServerCallResultPoint object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(BswAsynchronousServerCallResultPoint, cls).deserialize(element)

        # Parse asynchronous
        child = ARObject._find_child_element(element, "ASYNCHRONOUS")
        if child is not None:
            asynchronous_value = child.text
            obj.asynchronous = asynchronous_value

        return obj



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
