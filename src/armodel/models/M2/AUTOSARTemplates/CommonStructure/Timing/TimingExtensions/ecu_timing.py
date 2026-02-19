"""EcuTiming AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_TimingExtensions.pdf (page 30)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_CommonStructure_Timing_TimingExtensions.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.CommonStructure.Timing.TimingExtensions.timing_extension import (
    TimingExtension,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel.models.M2.AUTOSARTemplates.ECUCDescriptionTemplate.ecuc_value_collection import (
    EcucValueCollection,
)


class EcuTiming(TimingExtension):
    """AUTOSAR EcuTiming."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    ecu_ref: Optional[ARRef]
    def __init__(self) -> None:
        """Initialize EcuTiming."""
        super().__init__()
        self.ecu_ref: Optional[ARRef] = None
    @classmethod
    def deserialize(cls, element: ET.Element) -> "EcuTiming":
        """Deserialize XML element to EcuTiming object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized EcuTiming object
        """
        # Create instance and initialize with default values
        obj = cls.__new__(cls)
        obj.__init__()

        # Parse ecu_ref
        child = ARObject._find_child_element(element, "ECU")
        if child is not None:
            ecu_ref_value = ARObject._deserialize_by_tag(child, "EcucValueCollection")
            obj.ecu_ref = ecu_ref_value

        return obj



class EcuTimingBuilder:
    """Builder for EcuTiming."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: EcuTiming = EcuTiming()

    def build(self) -> EcuTiming:
        """Build and return EcuTiming object.

        Returns:
            EcuTiming instance
        """
        # TODO: Add validation
        return self._obj
