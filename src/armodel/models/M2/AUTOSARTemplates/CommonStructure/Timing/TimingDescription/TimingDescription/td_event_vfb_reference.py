"""TDEventVfbReference AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_TimingExtensions.pdf (page 52)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_CommonStructure_Timing_TimingDescription_TimingDescription.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.CommonStructure.Timing.TimingDescription.TimingDescription.td_event_vfb import (
    TDEventVfb,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject


class TDEventVfbReference(TDEventVfb):
    """AUTOSAR TDEventVfbReference."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    referenced_td_event_vfb: Optional[TDEventVfb]
    def __init__(self) -> None:
        """Initialize TDEventVfbReference."""
        super().__init__()
        self.referenced_td_event_vfb: Optional[TDEventVfb] = None
    @classmethod
    def deserialize(cls, element: ET.Element) -> "TDEventVfbReference":
        """Deserialize XML element to TDEventVfbReference object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized TDEventVfbReference object
        """
        # Create instance and initialize with default values
        obj = cls.__new__(cls)
        obj.__init__()

        # Parse referenced_td_event_vfb
        child = ARObject._find_child_element(element, "REFERENCED-TD-EVENT-VFB")
        if child is not None:
            referenced_td_event_vfb_value = ARObject._deserialize_by_tag(child, "TDEventVfb")
            obj.referenced_td_event_vfb = referenced_td_event_vfb_value

        return obj



class TDEventVfbReferenceBuilder:
    """Builder for TDEventVfbReference."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: TDEventVfbReference = TDEventVfbReference()

    def build(self) -> TDEventVfbReference:
        """Build and return TDEventVfbReference object.

        Returns:
            TDEventVfbReference instance
        """
        # TODO: Add validation
        return self._obj
