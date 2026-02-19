"""SystemSignalGroup AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 324)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_Fibex_FibexCore_CoreCommunication.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage.ar_element import (
    ARElement,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreCommunication.system_signal import (
    SystemSignal,
)


class SystemSignalGroup(ARElement):
    """AUTOSAR SystemSignalGroup."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    system_signals: list[SystemSignal]
    transforming: Optional[SystemSignal]
    def __init__(self) -> None:
        """Initialize SystemSignalGroup."""
        super().__init__()
        self.system_signals: list[SystemSignal] = []
        self.transforming: Optional[SystemSignal] = None
    @classmethod
    def deserialize(cls, element: ET.Element) -> "SystemSignalGroup":
        """Deserialize XML element to SystemSignalGroup object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized SystemSignalGroup object
        """
        # Create instance and initialize with default values
        obj = cls.__new__(cls)
        obj.__init__()

        # Parse system_signals (list)
        obj.system_signals = []
        for child in ARObject._find_all_child_elements(element, "SYSTEM-SIGNALS"):
            system_signals_value = ARObject._deserialize_by_tag(child, "SystemSignal")
            obj.system_signals.append(system_signals_value)

        # Parse transforming
        child = ARObject._find_child_element(element, "TRANSFORMING")
        if child is not None:
            transforming_value = ARObject._deserialize_by_tag(child, "SystemSignal")
            obj.transforming = transforming_value

        return obj



class SystemSignalGroupBuilder:
    """Builder for SystemSignalGroup."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: SystemSignalGroup = SystemSignalGroup()

    def build(self) -> SystemSignalGroup:
        """Build and return SystemSignalGroup object.

        Returns:
            SystemSignalGroup instance
        """
        # TODO: Add validation
        return self._obj
