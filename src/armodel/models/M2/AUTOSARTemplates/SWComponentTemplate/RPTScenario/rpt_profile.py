"""RptProfile AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 853)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SWComponentTemplate_RPTScenario.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.identifiable import (
    Identifiable,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.CommonStructure.MeasurementCalibrationSupport.RptSupport import (
    RptEnablerImplTypeEnum,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    CIdentifier,
    PositiveInteger,
)


class RptProfile(Identifiable):
    """AUTOSAR RptProfile."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    max_service: Optional[PositiveInteger]
    min_service_point: Optional[PositiveInteger]
    service_point: Optional[CIdentifier]
    stim_enabler: Optional[RptEnablerImplTypeEnum]
    def __init__(self) -> None:
        """Initialize RptProfile."""
        super().__init__()
        self.max_service: Optional[PositiveInteger] = None
        self.min_service_point: Optional[PositiveInteger] = None
        self.service_point: Optional[CIdentifier] = None
        self.stim_enabler: Optional[RptEnablerImplTypeEnum] = None
    @classmethod
    def deserialize(cls, element: ET.Element) -> "RptProfile":
        """Deserialize XML element to RptProfile object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized RptProfile object
        """
        # Create instance and initialize with default values
        obj = cls.__new__(cls)
        obj.__init__()

        # Parse max_service
        child = ARObject._find_child_element(element, "MAX-SERVICE")
        if child is not None:
            max_service_value = child.text
            obj.max_service = max_service_value

        # Parse min_service_point
        child = ARObject._find_child_element(element, "MIN-SERVICE-POINT")
        if child is not None:
            min_service_point_value = child.text
            obj.min_service_point = min_service_point_value

        # Parse service_point
        child = ARObject._find_child_element(element, "SERVICE-POINT")
        if child is not None:
            service_point_value = child.text
            obj.service_point = service_point_value

        # Parse stim_enabler
        child = ARObject._find_child_element(element, "STIM-ENABLER")
        if child is not None:
            stim_enabler_value = child.text
            obj.stim_enabler = stim_enabler_value

        return obj



class RptProfileBuilder:
    """Builder for RptProfile."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: RptProfile = RptProfile()

    def build(self) -> RptProfile:
        """Build and return RptProfile object.

        Returns:
            RptProfile instance
        """
        # TODO: Add validation
        return self._obj
