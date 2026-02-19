"""SpecElementReference AUTOSAR element.

References:
  - AUTOSAR_FO_TPS_StandardizationTemplate.pdf (page 82)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_CommonStructure_StandardizationTemplate_DataExchangePoint_Common.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.identifiable import (
    Identifiable,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    String,
)
from abc import ABC, abstractmethod


class SpecElementReference(Identifiable, ABC):
    """AUTOSAR SpecElementReference."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            True for abstract classes
        """
        return True

    alternative: Optional[String]
    def __init__(self) -> None:
        """Initialize SpecElementReference."""
        super().__init__()
        self.alternative: Optional[String] = None
    @classmethod
    def deserialize(cls, element: ET.Element) -> "SpecElementReference":
        """Deserialize XML element to SpecElementReference object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized SpecElementReference object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(SpecElementReference, cls).deserialize(element)

        # Parse alternative
        child = ARObject._find_child_element(element, "ALTERNATIVE")
        if child is not None:
            alternative_value = child.text
            obj.alternative = alternative_value

        return obj



class SpecElementReferenceBuilder:
    """Builder for SpecElementReference."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: SpecElementReference = SpecElementReference()

    def build(self) -> SpecElementReference:
        """Build and return SpecElementReference object.

        Returns:
            SpecElementReference instance
        """
        # TODO: Add validation
        return self._obj
