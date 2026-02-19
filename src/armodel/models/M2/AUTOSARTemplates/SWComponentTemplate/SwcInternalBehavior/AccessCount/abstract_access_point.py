"""AbstractAccessPoint AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf (page 57)
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 562)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SWComponentTemplate_SwcInternalBehavior_AccessCount.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.identifiable import (
    Identifiable,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.SwcInternalBehavior.AccessCount import (
    RteApiReturnValueProvisionEnum,
)
from abc import ABC, abstractmethod


class AbstractAccessPoint(Identifiable, ABC):
    """AUTOSAR AbstractAccessPoint."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            True for abstract classes
        """
        return True

    return_value: Optional[RteApiReturnValueProvisionEnum]
    def __init__(self) -> None:
        """Initialize AbstractAccessPoint."""
        super().__init__()
        self.return_value: Optional[RteApiReturnValueProvisionEnum] = None
    @classmethod
    def deserialize(cls, element: ET.Element) -> "AbstractAccessPoint":
        """Deserialize XML element to AbstractAccessPoint object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized AbstractAccessPoint object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(AbstractAccessPoint, cls).deserialize(element)

        # Parse return_value
        child = ARObject._find_child_element(element, "RETURN-VALUE")
        if child is not None:
            return_value_value = RteApiReturnValueProvisionEnum.deserialize(child)
            obj.return_value = return_value_value

        return obj



class AbstractAccessPointBuilder:
    """Builder for AbstractAccessPoint."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: AbstractAccessPoint = AbstractAccessPoint()

    def build(self) -> AbstractAccessPoint:
        """Build and return AbstractAccessPoint object.

        Returns:
            AbstractAccessPoint instance
        """
        # TODO: Add validation
        return self._obj
