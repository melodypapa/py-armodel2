"""OsTaskProxy AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 208)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_RteEventToOsTaskMapping.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage.ar_element import (
    ARElement,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.RteEventToOsTaskMapping import (
    OsTaskPreemptabilityEnum,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    PositiveInteger,
    TimeValue,
)


class OsTaskProxy(ARElement):
    """AUTOSAR OsTaskProxy."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    period: Optional[TimeValue]
    preemptability: Optional[OsTaskPreemptabilityEnum]
    priority: Optional[PositiveInteger]
    def __init__(self) -> None:
        """Initialize OsTaskProxy."""
        super().__init__()
        self.period: Optional[TimeValue] = None
        self.preemptability: Optional[OsTaskPreemptabilityEnum] = None
        self.priority: Optional[PositiveInteger] = None
    @classmethod
    def deserialize(cls, element: ET.Element) -> "OsTaskProxy":
        """Deserialize XML element to OsTaskProxy object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized OsTaskProxy object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(OsTaskProxy, cls).deserialize(element)

        # Parse period
        child = ARObject._find_child_element(element, "PERIOD")
        if child is not None:
            period_value = child.text
            obj.period = period_value

        # Parse preemptability
        child = ARObject._find_child_element(element, "PREEMPTABILITY")
        if child is not None:
            preemptability_value = OsTaskPreemptabilityEnum.deserialize(child)
            obj.preemptability = preemptability_value

        # Parse priority
        child = ARObject._find_child_element(element, "PRIORITY")
        if child is not None:
            priority_value = child.text
            obj.priority = priority_value

        return obj



class OsTaskProxyBuilder:
    """Builder for OsTaskProxy."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: OsTaskProxy = OsTaskProxy()

    def build(self) -> OsTaskProxy:
        """Build and return OsTaskProxy object.

        Returns:
            OsTaskProxy instance
        """
        # TODO: Add validation
        return self._obj
