"""E2EProfileCompatibilityProps AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 202)
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 807)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_Transformer.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage.ar_element import (
    ARElement,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Boolean,
)


class E2EProfileCompatibilityProps(ARElement):
    """AUTOSAR E2EProfileCompatibilityProps."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    transit_to_invalid: Optional[Boolean]
    def __init__(self) -> None:
        """Initialize E2EProfileCompatibilityProps."""
        super().__init__()
        self.transit_to_invalid: Optional[Boolean] = None
    @classmethod
    def deserialize(cls, element: ET.Element) -> "E2EProfileCompatibilityProps":
        """Deserialize XML element to E2EProfileCompatibilityProps object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized E2EProfileCompatibilityProps object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(E2EProfileCompatibilityProps, cls).deserialize(element)

        # Parse transit_to_invalid
        child = ARObject._find_child_element(element, "TRANSIT-TO-INVALID")
        if child is not None:
            transit_to_invalid_value = child.text
            obj.transit_to_invalid = transit_to_invalid_value

        return obj



class E2EProfileCompatibilityPropsBuilder:
    """Builder for E2EProfileCompatibilityProps."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: E2EProfileCompatibilityProps = E2EProfileCompatibilityProps()

    def build(self) -> E2EProfileCompatibilityProps:
        """Build and return E2EProfileCompatibilityProps object.

        Returns:
            E2EProfileCompatibilityProps instance
        """
        # TODO: Add validation
        return self._obj
