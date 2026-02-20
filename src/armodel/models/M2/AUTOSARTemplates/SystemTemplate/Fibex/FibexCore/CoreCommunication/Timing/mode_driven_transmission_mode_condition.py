"""ModeDrivenTransmissionModeCondition AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 393)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_Fibex_FibexCore_CoreCommunication_Timing.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.CommonStructure.ModeDeclaration.mode_declaration import (
    ModeDeclaration,
)


class ModeDrivenTransmissionModeCondition(ARObject):
    """AUTOSAR ModeDrivenTransmissionModeCondition."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    modes: list[ModeDeclaration]
    def __init__(self) -> None:
        """Initialize ModeDrivenTransmissionModeCondition."""
        super().__init__()
        self.modes: list[ModeDeclaration] = []

    def serialize(self) -> ET.Element:
        """Serialize ModeDrivenTransmissionModeCondition to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = self._get_xml_tag()
        elem = ET.Element(tag)

        # Serialize modes (list to container "MODES")
        if self.modes:
            wrapper = ET.Element("MODES")
            for item in self.modes:
                serialized = ARObject._serialize_item(item, "ModeDeclaration")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "ModeDrivenTransmissionModeCondition":
        """Deserialize XML element to ModeDrivenTransmissionModeCondition object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized ModeDrivenTransmissionModeCondition object
        """
        # Create instance and initialize with default values
        obj = cls.__new__(cls)
        obj.__init__()

        # Parse modes (list from container "MODES")
        obj.modes = []
        container = ARObject._find_child_element(element, "MODES")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = ARObject._deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.modes.append(child_value)

        return obj



class ModeDrivenTransmissionModeConditionBuilder:
    """Builder for ModeDrivenTransmissionModeCondition."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: ModeDrivenTransmissionModeCondition = ModeDrivenTransmissionModeCondition()

    def build(self) -> ModeDrivenTransmissionModeCondition:
        """Build and return ModeDrivenTransmissionModeCondition object.

        Returns:
            ModeDrivenTransmissionModeCondition instance
        """
        # TODO: Add validation
        return self._obj
