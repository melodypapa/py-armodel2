"""TransmissionModeDeclaration AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 392)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_Fibex_FibexCore_CoreCommunication_Timing.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional, Any
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.serialization import SerializationHelper
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreCommunication.Timing.mode_driven_transmission_mode_condition import (
    ModeDrivenTransmissionModeCondition,
)


class TransmissionModeDeclaration(ARObject):
    """AUTOSAR TransmissionModeDeclaration."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    mode_drivens: list[ModeDrivenTransmissionModeCondition]
    transmission: Optional[Any]
    def __init__(self) -> None:
        """Initialize TransmissionModeDeclaration."""
        super().__init__()
        self.mode_drivens: list[ModeDrivenTransmissionModeCondition] = []
        self.transmission: Optional[Any] = None

    def serialize(self) -> ET.Element:
        """Serialize TransmissionModeDeclaration to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = SerializationHelper.get_xml_tag(self.__class__)
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(TransmissionModeDeclaration, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize mode_drivens (list to container "MODE-DRIVENS")
        if self.mode_drivens:
            wrapper = ET.Element("MODE-DRIVENS")
            for item in self.mode_drivens:
                serialized = SerializationHelper.serialize_item(item, "ModeDrivenTransmissionModeCondition")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize transmission
        if self.transmission is not None:
            serialized = SerializationHelper.serialize_item(self.transmission, "Any")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("TRANSMISSION")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "TransmissionModeDeclaration":
        """Deserialize XML element to TransmissionModeDeclaration object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized TransmissionModeDeclaration object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(TransmissionModeDeclaration, cls).deserialize(element)

        # Parse mode_drivens (list from container "MODE-DRIVENS")
        obj.mode_drivens = []
        container = SerializationHelper.find_child_element(element, "MODE-DRIVENS")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = SerializationHelper.deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.mode_drivens.append(child_value)

        # Parse transmission
        child = SerializationHelper.find_child_element(element, "TRANSMISSION")
        if child is not None:
            transmission_value = child.text
            obj.transmission = transmission_value

        return obj



class TransmissionModeDeclarationBuilder:
    """Builder for TransmissionModeDeclaration."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: TransmissionModeDeclaration = TransmissionModeDeclaration()

    def build(self) -> TransmissionModeDeclaration:
        """Build and return TransmissionModeDeclaration object.

        Returns:
            TransmissionModeDeclaration instance
        """
        # TODO: Add validation
        return self._obj
