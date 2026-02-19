"""SpecElementScope AUTOSAR element.

References:
  - AUTOSAR_FO_TPS_StandardizationTemplate.pdf (page 84)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_CommonStructure_StandardizationTemplate_DataExchangePoint_Common.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.CommonStructure.StandardizationTemplate.DataExchangePoint.Common.spec_element_reference import (
    SpecElementReference,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Boolean,
)
from abc import ABC, abstractmethod


class SpecElementScope(SpecElementReference, ABC):
    """AUTOSAR SpecElementScope."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            True for abstract classes
        """
        return True

    in_scope: Optional[Boolean]
    def __init__(self) -> None:
        """Initialize SpecElementScope."""
        super().__init__()
        self.in_scope: Optional[Boolean] = None
    @classmethod
    def deserialize(cls, element: ET.Element) -> "SpecElementScope":
        """Deserialize XML element to SpecElementScope object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized SpecElementScope object
        """
        # Create instance and initialize with default values
        obj = cls.__new__(cls)
        obj.__init__()

        # Parse in_scope
        child = ARObject._find_child_element(element, "IN-SCOPE")
        if child is not None:
            in_scope_value = child.text
            obj.in_scope = in_scope_value

        return obj



class SpecElementScopeBuilder:
    """Builder for SpecElementScope."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: SpecElementScope = SpecElementScope()

    def build(self) -> SpecElementScope:
        """Build and return SpecElementScope object.

        Returns:
            SpecElementScope instance
        """
        # TODO: Add validation
        return self._obj
