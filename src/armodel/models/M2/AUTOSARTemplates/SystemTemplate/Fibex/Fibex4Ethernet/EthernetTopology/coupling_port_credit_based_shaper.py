"""CouplingPortCreditBasedShaper AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 2013)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_Fibex_Fibex4Ethernet_EthernetTopology.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.identifiable import (
    Identifiable,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    PositiveInteger,
)


class CouplingPortCreditBasedShaper(Identifiable):
    """AUTOSAR CouplingPortCreditBasedShaper."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    idle_slope: Optional[PositiveInteger]
    lower_boundary: Optional[PositiveInteger]
    upper_boundary: Optional[PositiveInteger]
    def __init__(self) -> None:
        """Initialize CouplingPortCreditBasedShaper."""
        super().__init__()
        self.idle_slope: Optional[PositiveInteger] = None
        self.lower_boundary: Optional[PositiveInteger] = None
        self.upper_boundary: Optional[PositiveInteger] = None
    @classmethod
    def deserialize(cls, element: ET.Element) -> "CouplingPortCreditBasedShaper":
        """Deserialize XML element to CouplingPortCreditBasedShaper object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized CouplingPortCreditBasedShaper object
        """
        # Create instance and initialize with default values
        obj = cls.__new__(cls)
        obj.__init__()

        # Parse idle_slope
        child = ARObject._find_child_element(element, "IDLE-SLOPE")
        if child is not None:
            idle_slope_value = child.text
            obj.idle_slope = idle_slope_value

        # Parse lower_boundary
        child = ARObject._find_child_element(element, "LOWER-BOUNDARY")
        if child is not None:
            lower_boundary_value = child.text
            obj.lower_boundary = lower_boundary_value

        # Parse upper_boundary
        child = ARObject._find_child_element(element, "UPPER-BOUNDARY")
        if child is not None:
            upper_boundary_value = child.text
            obj.upper_boundary = upper_boundary_value

        return obj



class CouplingPortCreditBasedShaperBuilder:
    """Builder for CouplingPortCreditBasedShaper."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: CouplingPortCreditBasedShaper = CouplingPortCreditBasedShaper()

    def build(self) -> CouplingPortCreditBasedShaper:
        """Build and return CouplingPortCreditBasedShaper object.

        Returns:
            CouplingPortCreditBasedShaper instance
        """
        # TODO: Add validation
        return self._obj
