"""ValueRestrictionWithSeverity AUTOSAR element.

References:
  - AUTOSAR_FO_TPS_StandardizationTemplate.pdf (page 87)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_CommonStructure_StandardizationTemplate_DataExchangePoint_Data.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.CommonStructure.StandardizationTemplate.DataExchangePoint.Common.restriction_with_severity import (
    RestrictionWithSeverity,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject


class ValueRestrictionWithSeverity(RestrictionWithSeverity):
    """AUTOSAR ValueRestrictionWithSeverity."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    def __init__(self) -> None:
        """Initialize ValueRestrictionWithSeverity."""
        super().__init__()
    @classmethod
    def deserialize(cls, element: ET.Element) -> "ValueRestrictionWithSeverity":
        """Deserialize XML element to ValueRestrictionWithSeverity object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized ValueRestrictionWithSeverity object
        """
        # Delegate to parent class to handle inherited attributes
        return super(ValueRestrictionWithSeverity, cls).deserialize(element)



class ValueRestrictionWithSeverityBuilder:
    """Builder for ValueRestrictionWithSeverity."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: ValueRestrictionWithSeverity = ValueRestrictionWithSeverity()

    def build(self) -> ValueRestrictionWithSeverity:
        """Build and return ValueRestrictionWithSeverity object.

        Returns:
            ValueRestrictionWithSeverity instance
        """
        # TODO: Add validation
        return self._obj
