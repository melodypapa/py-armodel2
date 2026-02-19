"""RptServicePoint AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf (page 206)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_CommonStructure_MeasurementCalibrationSupport_RptSupport.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.identifiable import (
    Identifiable,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    CIdentifier,
    PositiveInteger,
)


class RptServicePoint(Identifiable):
    """AUTOSAR RptServicePoint."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    service_id: Optional[PositiveInteger]
    symbol: Optional[CIdentifier]
    def __init__(self) -> None:
        """Initialize RptServicePoint."""
        super().__init__()
        self.service_id: Optional[PositiveInteger] = None
        self.symbol: Optional[CIdentifier] = None
    @classmethod
    def deserialize(cls, element: ET.Element) -> "RptServicePoint":
        """Deserialize XML element to RptServicePoint object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized RptServicePoint object
        """
        # Create instance and initialize with default values
        obj = cls.__new__(cls)
        obj.__init__()

        # Parse service_id
        child = ARObject._find_child_element(element, "SERVICE-ID")
        if child is not None:
            service_id_value = child.text
            obj.service_id = service_id_value

        # Parse symbol
        child = ARObject._find_child_element(element, "SYMBOL")
        if child is not None:
            symbol_value = child.text
            obj.symbol = symbol_value

        return obj



class RptServicePointBuilder:
    """Builder for RptServicePoint."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: RptServicePoint = RptServicePoint()

    def build(self) -> RptServicePoint:
        """Build and return RptServicePoint object.

        Returns:
            RptServicePoint instance
        """
        # TODO: Add validation
        return self._obj
