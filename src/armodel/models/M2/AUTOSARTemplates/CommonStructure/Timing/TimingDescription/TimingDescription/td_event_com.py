"""TDEventCom AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_TimingExtensions.pdf (page 65)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_CommonStructure_Timing_TimingDescription_TimingDescription.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.CommonStructure.Timing.TimingDescription.timing_description_event import (
    TimingDescriptionEvent,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreTopology.ecu_instance import (
    EcuInstance,
)
from abc import ABC, abstractmethod


class TDEventCom(TimingDescriptionEvent, ABC):
    """AUTOSAR TDEventCom."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            True for abstract classes
        """
        return True

    ecu_instance: Optional[EcuInstance]
    def __init__(self) -> None:
        """Initialize TDEventCom."""
        super().__init__()
        self.ecu_instance: Optional[EcuInstance] = None
    @classmethod
    def deserialize(cls, element: ET.Element) -> "TDEventCom":
        """Deserialize XML element to TDEventCom object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized TDEventCom object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(TDEventCom, cls).deserialize(element)

        # Parse ecu_instance
        child = ARObject._find_child_element(element, "ECU-INSTANCE")
        if child is not None:
            ecu_instance_value = ARObject._deserialize_by_tag(child, "EcuInstance")
            obj.ecu_instance = ecu_instance_value

        return obj



class TDEventComBuilder:
    """Builder for TDEventCom."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: TDEventCom = TDEventCom()

    def build(self) -> TDEventCom:
        """Build and return TDEventCom object.

        Returns:
            TDEventCom instance
        """
        # TODO: Add validation
        return self._obj
