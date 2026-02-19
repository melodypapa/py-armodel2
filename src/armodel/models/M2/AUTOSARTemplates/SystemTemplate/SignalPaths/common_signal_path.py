"""CommonSignalPath AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 253)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_SignalPaths.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional, Any
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.SystemTemplate.SignalPaths.signal_path_constraint import (
    SignalPathConstraint,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.SignalPaths.swc_to_swc_signal import (
    SwcToSwcSignal,
)


class CommonSignalPath(SignalPathConstraint):
    """AUTOSAR CommonSignalPath."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    operations: list[Any]
    signals: list[SwcToSwcSignal]
    def __init__(self) -> None:
        """Initialize CommonSignalPath."""
        super().__init__()
        self.operations: list[Any] = []
        self.signals: list[SwcToSwcSignal] = []
    @classmethod
    def deserialize(cls, element: ET.Element) -> "CommonSignalPath":
        """Deserialize XML element to CommonSignalPath object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized CommonSignalPath object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(CommonSignalPath, cls).deserialize(element)

        # Parse operations (list from container "OPERATIONS")
        obj.operations = []
        container = ARObject._find_child_element(element, "OPERATIONS")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = ARObject._deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.operations.append(child_value)

        # Parse signals (list from container "SIGNALS")
        obj.signals = []
        container = ARObject._find_child_element(element, "SIGNALS")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = ARObject._deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.signals.append(child_value)

        return obj



class CommonSignalPathBuilder:
    """Builder for CommonSignalPath."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: CommonSignalPath = CommonSignalPath()

    def build(self) -> CommonSignalPath:
        """Build and return CommonSignalPath object.

        Returns:
            CommonSignalPath instance
        """
        # TODO: Add validation
        return self._obj
