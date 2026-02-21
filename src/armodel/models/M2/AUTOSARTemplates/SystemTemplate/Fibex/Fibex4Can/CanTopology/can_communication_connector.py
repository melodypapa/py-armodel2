"""CanCommunicationConnector AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 74)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_Fibex_Fibex4Can_CanTopology.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Can.CanTopology.abstract_can_communication_connector import (
    AbstractCanCommunicationConnector,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.serialization import SerializationHelper
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    PositiveInteger,
    PositiveUnlimitedInteger,
)


class CanCommunicationConnector(AbstractCanCommunicationConnector):
    """AUTOSAR CanCommunicationConnector."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    pnc_wakeup_can: Optional[PositiveInteger]
    pnc_wakeup: Optional[PositiveUnlimitedInteger]
    pnc_wakeup_dlc: Optional[PositiveInteger]
    def __init__(self) -> None:
        """Initialize CanCommunicationConnector."""
        super().__init__()
        self.pnc_wakeup_can: Optional[PositiveInteger] = None
        self.pnc_wakeup: Optional[PositiveUnlimitedInteger] = None
        self.pnc_wakeup_dlc: Optional[PositiveInteger] = None

    def serialize(self) -> ET.Element:
        """Serialize CanCommunicationConnector to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = SerializationHelper.get_xml_tag(self.__class__)
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(CanCommunicationConnector, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize pnc_wakeup_can
        if self.pnc_wakeup_can is not None:
            serialized = SerializationHelper.serialize_item(self.pnc_wakeup_can, "PositiveInteger")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("PNC-WAKEUP-CAN")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize pnc_wakeup
        if self.pnc_wakeup is not None:
            serialized = SerializationHelper.serialize_item(self.pnc_wakeup, "PositiveUnlimitedInteger")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("PNC-WAKEUP")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize pnc_wakeup_dlc
        if self.pnc_wakeup_dlc is not None:
            serialized = SerializationHelper.serialize_item(self.pnc_wakeup_dlc, "PositiveInteger")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("PNC-WAKEUP-DLC")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "CanCommunicationConnector":
        """Deserialize XML element to CanCommunicationConnector object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized CanCommunicationConnector object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(CanCommunicationConnector, cls).deserialize(element)

        # Parse pnc_wakeup_can
        child = SerializationHelper.find_child_element(element, "PNC-WAKEUP-CAN")
        if child is not None:
            pnc_wakeup_can_value = child.text
            obj.pnc_wakeup_can = pnc_wakeup_can_value

        # Parse pnc_wakeup
        child = SerializationHelper.find_child_element(element, "PNC-WAKEUP")
        if child is not None:
            pnc_wakeup_value = child.text
            obj.pnc_wakeup = pnc_wakeup_value

        # Parse pnc_wakeup_dlc
        child = SerializationHelper.find_child_element(element, "PNC-WAKEUP-DLC")
        if child is not None:
            pnc_wakeup_dlc_value = child.text
            obj.pnc_wakeup_dlc = pnc_wakeup_dlc_value

        return obj



class CanCommunicationConnectorBuilder:
    """Builder for CanCommunicationConnector."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: CanCommunicationConnector = CanCommunicationConnector()

    def build(self) -> CanCommunicationConnector:
        """Build and return CanCommunicationConnector object.

        Returns:
            CanCommunicationConnector instance
        """
        # TODO: Add validation
        return self._obj
