"""NotAvailableValueSpecification AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 440)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_CommonStructure_Constants.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.CommonStructure.Constants.value_specification import (
    ValueSpecification,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    PositiveInteger,
)


class NotAvailableValueSpecification(ValueSpecification):
    """AUTOSAR NotAvailableValueSpecification."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    default_pattern: Optional[PositiveInteger]
    def __init__(self) -> None:
        """Initialize NotAvailableValueSpecification."""
        super().__init__()
        self.default_pattern: Optional[PositiveInteger] = None
    @classmethod
    def deserialize(cls, element: ET.Element) -> "NotAvailableValueSpecification":
        """Deserialize XML element to NotAvailableValueSpecification object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized NotAvailableValueSpecification object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(NotAvailableValueSpecification, cls).deserialize(element)

        # Parse default_pattern
        child = ARObject._find_child_element(element, "DEFAULT-PATTERN")
        if child is not None:
            default_pattern_value = child.text
            obj.default_pattern = default_pattern_value

        return obj



class NotAvailableValueSpecificationBuilder:
    """Builder for NotAvailableValueSpecification."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: NotAvailableValueSpecification = NotAvailableValueSpecification()

    def build(self) -> NotAvailableValueSpecification:
        """Build and return NotAvailableValueSpecification object.

        Returns:
            NotAvailableValueSpecification instance
        """
        # TODO: Add validation
        return self._obj
